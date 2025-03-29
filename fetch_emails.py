<<<<<<< HEAD
import os
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import re

# Forge the log stronghold
log_dir = r'C:\Users\digitalscorpyun\Anacostia\logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'fetch_emails_log.txt'),
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Inbox reaper awakens.")
print("Reaper’s live—war begins.")

# Auth strike - Locked path
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
flow = InstalledAppFlow.from_client_secrets_file('C:/Users/digitalscorpyun/Anacostia/credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
logging.info("Gmail gate shattered—auth locked.")
print("Auth strike lands—vault owns the inbox.")

# Build the Gmail strike force
service = build('gmail', 'v1', credentials=creds)
query = "is:unread -label:promotions -subject:TikTok"
results = service.users().messages().list(userId='me', q=query).execute()
messages = results.get('messages', [])

if not messages:
    logging.info("No targets—warzone’s silent.")
    print("No unread prey—vault rests.")
else:
    for msg in messages[:5]:  # First 5 hits
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
        if re.search(r'Python', subject, re.IGNORECASE):
            logging.info(f"Python strike: {subject}")
            print(f"Python hit: {subject}")
        else:
            logging.info(f"Non-Python noise: {subject}")
            print(f"Skipped: {subject}")

    # Vault sync
    with open(r'C:\Users\digitalscorpyun\Anacostia\notes\daily-notes-2025-03-14.md', 'a') as f:
        if not messages:
            f.write("\n- No unread emails—warzone silent.")
        else:
            f.write("\n## Email Strikes\n")
            for msg in messages[:5]:
                subject = next((h['value'] for h in msg_data['payload']['headers'] if h['name'] == 'Subject'), "No Subject")
                if re.search(r'Python', subject, re.IGNORECASE):
=======
import os
import logging
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import re

# Forge the log stronghold
log_dir = r'C:\Users\digitalscorpyun\Anacostia\logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_dir, 'fetch_emails_log.txt'),
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("Inbox reaper awakens.")
print("Reaper’s live—war begins.")

# Auth strike - Locked path
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
flow = InstalledAppFlow.from_client_secrets_file('C:/Users/digitalscorpyun/Anacostia/credentials.json', SCOPES)
creds = flow.run_local_server(port=0)
logging.info("Gmail gate shattered—auth locked.")
print("Auth strike lands—vault owns the inbox.")

# Build the Gmail strike force
service = build('gmail', 'v1', credentials=creds)
query = "is:unread -label:promotions -subject:TikTok"
results = service.users().messages().list(userId='me', q=query).execute()
messages = results.get('messages', [])

if not messages:
    logging.info("No targets—warzone’s silent.")
    print("No unread prey—vault rests.")
else:
    for msg in messages[:5]:  # First 5 hits
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()
        headers = msg_data['payload']['headers']
        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
        if re.search(r'Python', subject, re.IGNORECASE):
            logging.info(f"Python strike: {subject}")
            print(f"Python hit: {subject}")
        else:
            logging.info(f"Non-Python noise: {subject}")
            print(f"Skipped: {subject}")

    # Vault sync
    with open(r'C:\Users\digitalscorpyun\Anacostia\notes\daily-notes-2025-03-14.md', 'a') as f:
        if not messages:
            f.write("\n- No unread emails—warzone silent.")
        else:
            f.write("\n## Email Strikes\n")
            for msg in messages[:5]:
                subject = next((h['value'] for h in msg_data['payload']['headers'] if h['name'] == 'Subject'), "No Subject")
                if re.search(r'Python', subject, re.IGNORECASE):
>>>>>>> 769b11b2f1b8510b1da5db510583301e7c9784a9
                    f.write(f"- Python hit: {subject}\n")