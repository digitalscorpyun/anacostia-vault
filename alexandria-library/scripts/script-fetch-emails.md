### 🏴 **Script - Fetch Emails** 🏴

🔥 **Inbox Strike: Python Claws the Chaos** 🔥

**📜 Category:** Automation / Email Mastery

**Date Created:** 2025-03-14  
**Last Updated:** 2025-03-14

---

## ✊🏿 **Overview: fetch_emails.py – The Vault’s Mail Reaper**

**script-fetch-emails.md** unleashes **fetch_emails.py**, a **Python war blade** carved by digitalscorpyun to rip unread emails from Gmail, shredding TikTok noise and snagging Python gold. It’s a lethal arm of [[development-priorities]], syncing with [[anacostia-vault-execution]] to fuel your Obsidian vault and IBM AI Developer Cert grind. This ain’t just automation—it’s a **strike against inbox entropy**, locking your focus on justice and code.

> _"Emails bow—the vault reaps the truth." – Vault war cry._

---

## 🔥 **Key Pillars of Strike**

📬 **Auth Might** → Gmail bends to your will.  
⚔ **Filter Fury** → Noise dies, signal reigns.  
🐍 **Code Blade** → Python cuts the fat.  
📡 **Git Surge** → Victory pushed to the cloud.  
🚀 **Vault Power** → Automation feeds the fight.

---

## 🏆 **Script Commanders**

🧠 **Logic Core** → Precision drives the reap.  
🛠 **Tech Forge** → Scripts slay the mess.  
👤 **digitalscorpyun** → The warrior coder.

---

## 🌍 **Script Warzone**

🔹 **🛡 The Code – Fetch Emails Unleashed**  
- **Auth Strike**:  
  ```python
  from google_auth_oauthlib.flow import InstalledAppFlow
  SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
  flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
  creds = flow.run_local_server(port=0)
  ```  
  - **Debug Orders**: Verify `credentials.json`, smash firewall blocks, log errors with `logging`—[[python-overview]].  

- **Filter Slash**:  
  ```python
  import re
  query = "is:unread -label:promotions -subject:TikTok"
  if re.search(r'Python', msg['Subject']): print(f"Subject: {msg['Subject']}")
  ```  
  - **Tactic**: Rip out unread gems, ditch TikTok trash—Python regex cuts sharp—[[structure-note-python-libraries]].  

- **Git Victory**:  
  ```bash
  git add fetch_emails.py
  git commit -m "Enhanced filtering and auth"
  git push origin main
  ```  
  - **Push**: Lock wins in `virgin-repository`—[[github-virgin-repository]]—vault stays live.

🔹 **🔥 How It Strikes – The War Plan**  
- **Auth Forge**: OAuth cracks Gmail open—creds flow, no retreat.  
- **Filter Edge**: Query slices promotions, TikTok—Python focus locked—[[anacostia-vault-execution]].  
- **Log Might**: Errors bleed to logs—trace every kill—[[development-priorities]].  
- **Vault Sync**: Feeds [[show-grok]]—inbox fuels the fight.

---

## 🔗 **Connections in Your Zettelkasten**

📖 **[[00-index]]** → Vault’s war hub.  
🔥 **[[development-priorities]]** → Priority strike plan.  
✊🏿 **[[python-overview]]** → Code backbone.  
💻 **[[anacostia-vault-execution]]** → Execution core.  
🛠 **[[github-virgin-repository]]** → Code fortress.  
📋 **[[to-do-list]]** → Action forge.

---

🔥 **This ain’t a script—it’s your vault’s mail slayer.** 🔥  
🏴 **Every fetch is a strike for order.** 🏴  
🚀 **Run it, log it, rule the inbox.** 🚀

[[00-index]] | [[development-priorities]] | [[python-overview]] | [[anacostia-vault-execution]]

---

### 🏷️ **Tags**

#script_fetch_emails #email_automation #python_power #vault_order #justice_fuel

---

### 📖 **Action Commands**

- Debug OAuth—smash credential bugs—[[development-priorities]].  
- Push to GitHub—lock in `main`—[[github.com-digitalscorpyun-anacostia-vault]].  
- Link logs, track the war. Key placed [[show-grok]]

---

### Creation Notes
1. **Structure**: Forged in Matamba-style (🏴 Title, 🔥 Subtitle, ✊🏿 Overview)—fiery, unified strike.
2. **Tone**: Amped ScorpyunStyle™ heat (e.g., “war blade,” “strike against entropy”)—pure resistance fire.
3. **Content**: Expanded snippet into a full hub—auth, filter, git—vault-ready.
4. **Connections**: Tied to vault hubs (e.g., "[[anacostia-vault-execution]]")—deep roots.
5. **Backlinks**: Hyphenated (e.g., "[[python-overview]]")—vault-sharp, no slack.
6. **Tags**: Underscore_format (e.g., "script_fetch_emails")—fierce and clean.
7. **Focus**: Synced with your automation and justice grind—mission locked.
8. **Filename**: Set as "script-fetch-emails.md"—kebab-case lethal.

---

### Filename
Saved as **"script-fetch-emails.md"**, a new vault weapon.

---

This "script-fetch-emails.md" is your vault’s inbox reaper, forged to kill chaos. Want more heat (e.g., filter tweaks), deeper debug steps, or extra links? Hit me back! 🔥🚀

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

# Auth strike
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
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
                    f.write(f"- Python hit: {subject}\n")