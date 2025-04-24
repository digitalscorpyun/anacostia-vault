import os
import pickle
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import datetime
import email
from bs4 import BeautifulSoup
import logging

# Configuration
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']  # Allows read and modify
CRED_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'
VAULT_PATH = r'C:\Users\miker\OneDrive\Documents\Knowledge Hub\Inbox'  # Obsidian Inbox location
ALLOWED_SENDERS = []  # Empty for now, focusing on keywords
KEYWORD_FILTERS = ['Google Alert', 'Google Alerts']  # Fetch emails with these keywords

# Set up logging
logging.basicConfig(filename='fetch_emails.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def authenticate_gmail():
    """Authenticate with Gmail API."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            logging.info("Starting Gmail API authentication for fetch_emails...")
            flow = InstalledAppFlow.from_client_secrets_file(CRED_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
            logging.info("Gmail API authentication completed for fetch_emails.")
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)

    return build('gmail', 'v1', credentials=creds)

def get_email_body(message):
    """Extract the clean email body (first paragraph or key content) from the message data."""
    try:
        # Decode the payload if it's base64-encoded
        if 'payload' in message and 'body' in message['payload']:
            body_data = message['payload']['body'].get('data', '')
            if body_data:
                # Decode base64 data
                decoded_bytes = base64.urlsafe_b64decode(body_data.replace('-', '+').replace('_', '/'))
                # Parse the email content
                msg = email.message_from_bytes(decoded_bytes)
                # Extract text/plain part if multipart
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            body = part.get_payload(decode=True).decode('utf-8', errors='ignore')
                            # Clean up and get the first paragraph or key content
                            cleaned_body = clean_google_alert_body(body)
                            return cleaned_body if cleaned_body else "[No plain text body available]"
                else:
                    body = msg.get_payload(decode=True).decode('utf-8', errors='ignore')
                    cleaned_body = clean_google_alert_body(body)
                    return cleaned_body if cleaned_body else "[No body available]"
        # Check parts for HTML or plain text
        if 'parts' in message['payload']:
            for part in message['payload']['parts']:
                if part.get('mimeType') == 'text/plain' and 'body' in part and part['body'].get('data', ''):
                    decoded_bytes = base64.urlsafe_b64decode(part['body']['data'].replace('-', '+').replace('_', '/'))
                    body = decoded_bytes.decode('utf-8', errors='ignore')
                    cleaned_body = clean_google_alert_body(body)
                    return cleaned_body if cleaned_body else "[No plain text body available]"
                elif part.get('mimeType') == 'text/html' and 'body' in part and part['body'].get('data', ''):
                    decoded_bytes = base64.urlsafe_b64decode(part['body']['data'].replace('-', '+').replace('_', '/'))
                    body = decoded_bytes.decode('utf-8', errors='ignore')
                    # Convert HTML to plain text
                    soup = BeautifulSoup(body, 'html.parser')
                    plain_text = soup.get_text().strip()
                    cleaned_body = clean_google_alert_body(plain_text)
                    return cleaned_body if cleaned_body else "[No body available]"
        return "[No body available]"
    except Exception as e:
        logging.error(f"Error fetching email body: {str(e)}")
        return "[Error fetching body]"

def clean_google_alert_body(body):
    """Clean up Google Alerts email body to extract the first paragraph or key content, removing URLs and redundant lines."""
    if not body or body.strip() == "":
        return "[No body available]"
    
    # Split into lines and filter out URLs, empty lines, and redundant Google Alerts metadata
    lines = [line.strip() for line in body.split('\n') if line.strip()]
    cleaned_lines = []
    for line in lines:
        # Skip URLs, Google Alerts metadata, and repeated lines
        if not (line.startswith('http://') or line.startswith('https://') or 
                'google.com/alerts' in line.lower() or 
                'Sign in to manage your alerts' in line or 
                line in cleaned_lines):  # Avoid duplicates
            cleaned_lines.append(line)
    
    # Take the first non-empty paragraph (up to 3 lines or until a blank line/URL)
    result = []
    for line in cleaned_lines[:3]:  # Limit to first few lines for brevity
        if line and not (line.startswith('http://') or line.startswith('https://')):
            result.append(line)
        else:
            break
    return "\n".join(result) if result else "[No key content available]"

def fetch_specific_emails(service):
    """Fetch unread emails matching keywords, mark as read."""
    # Query for unread emails with "Google Alert" or "Google Alerts"
    query = 'is:unread ("Google Alert" OR "Google Alerts")'
    results = service.users().messages().list(userId='me', q=query).execute()
    messages = results.get('messages', [])

    if not messages:
        logging.info("No matching unread emails found for fetch_emails.")
        return []

    email_list = []
    for msg in messages:
        try:
            msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
            headers = msg_data['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            logging.debug(f"Processing email in fetch_emails: {subject}")
            if any(k.lower() in subject.lower() for k in KEYWORD_FILTERS):
                email_list.append({'id': msg['id'], 'subject': subject, 'message': msg_data})
                service.users().messages().modify(
                    userId='me', id=msg['id'], body={'removeLabelIds': ['UNREAD']}
                ).execute()
        except Exception as e:
            logging.error(f"Error processing email {msg.get('id', 'Unknown ID')} in fetch_emails: {str(e)}")
    return email_list

def save_to_obsidian(emails):
    """Save a single summary note with collapsible (closed by default) email subjects and cleaned bodies in the Obsidian vault, using standard <details> tags."""
    if not os.path.exists(VAULT_PATH):
        os.makedirs(VAULT_PATH)

    # Create a single summary note for all emails
    filename = "Fetched_Emails_Summary.md"
    filepath = os.path.join(VAULT_PATH, filename)

    # Structured single note template with collapsible (closed by default) sections for subjects and bodies
    content = f"""---
title: Fetched Google Alerts Emails - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
tags: [e_m_a_i_l, i_n_b_o_x]
---

# Fetched Google Alerts Emails

Below is a list of all emails fetched on {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} containing 'Google Alert' or 'Google Alerts':

"""
    for email in emails:
        try:
            logging.debug(f"Saving subject to note in fetch_emails: {email['subject']}")
            content += f"""<details><summary>{email['subject']}</summary>
{get_email_body(email['message'])}
</details>\n"""
        except Exception as e:
            logging.error(f"Error saving email {email['subject']} in fetch_emails: {str(e)}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    logging.info(f"Saved summary note in fetch_emails: {filename}")

def main():
    logging.info("Starting fetch_emails task...")
    try:
        service = authenticate_gmail()
        emails = fetch_specific_emails(service)
        if emails:
            save_to_obsidian(emails)
            logging.info(f"fetch_emails completed successfully. Processed {len(emails)} emails.")
            print(f"fetch_emails completed successfully. Processed {len(emails)} emails.")
        else:
            logging.info("fetch_emails completed with no emails to process.")
            print("fetch_emails completed with no emails to process.")
    except Exception as e:
        logging.error(f"fetch_emails failed: {str(e)}")
        print(f"fetch_emails failed: {str(e)}")
    finally:
        logging.info("fetch_emails task finished.")
        print("fetch_emails task finished.")

if __name__ == '__main__':
    main()

[[to-do-list]] | [[00-index]] | [[ai-ml-overview]] | [[the-lion-of-anacostia-roadmap-anacostia-vault]] | [[africana-studies-overview]]


