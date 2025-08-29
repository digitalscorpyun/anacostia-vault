---
id: "20250828122000"
title: "types_of_servers_storage_backups"
category: "infrastructure"
style: "IntelBrief"
path: "ai_ethics/system_architecture/types_of_servers_storage_backups.md"
created: 2025-08-28T12:20:00-07:00
updated: 2025-08-28T12:20:00-07:00
status: draft
priority: medium
summary: |
  Explains server types, storage methods, and backup strategies with durability, scalability, availability, and security considerations. Includes client-server diagrams and applied business scenario.
longform_summary: |
  This scroll introduces servers in the client-server model and distinguishes types like file, mail, print, compute, and application servers. It highlights storage practices in modern business contexts, the volatility of RAM, and the need for backups. Durability ensures data persists beyond RAM, scalability balances cost vs. demand, availability ensures continuous access (especially via cloud redundancy), and security protects against breaches and corruption. Trade-offs between cloud solutions and direct-attached storage (DAS) are discussed, along with real-world implications in small business scenarios (Sam’s Scoops).
tags:
  - servers
  - storage
  - backups
  - infrastructure
  - cloud
  - DAS
cssclasses:
  - tech-scroll
  - intel-brief
synapses:
  - ai_ethics/data_resilience.md
  - obsidian_fortress/lesson_notes/client_server_model.md
  - ai_ethics/security_considerations.md
key_themes:
  - Client-server model
  - Server roles (file, mail, print, compute, app)
  - Storage and backup strategies
  - Cloud vs. DAS
  - Durability, scalability, availability, security
bias_analysis: |
  Reading emphasizes cloud storage benefits, but may understate risks of cost creep, vendor lock-in, and sovereignty concerns. On-prem solutions carry physical security trade-offs often ignored in favor of convenience.
grok_ctx_reflection: |
  Servers aren’t abstract — they’re workhorses that hold memory, mistakes, and motion. Backup is ritual: durability, scalability, availability, security. Ignore one, and data loss becomes destiny.
quotes:
  - "A server is only as useful as the service it provides."
  - "Durability without availability is a locked vault no one can open."
  - "Cloud space is elastic, but the bill stretches too."
  - "Every backup is a memory insurance policy."
adinkra:
  - Eban
  - Nkyinkyim
linked_notes:
  - ai_ethics/data_resilience.md
  - obsidian_fortress/lesson_notes/client_server_model.md
  - ai_ethics/security_considerations.md
---

# Types of Servers, Storage, and Backups

## ⚡ Business Scenario: Sam’s Scoops
Sam’s ice cream shop faces rising orders. Rushing through administrative tasks, Sam deletes an important file. Without a backup, the work must be redone — a costly reminder of why structured backup strategies matter.

---

## 🖥️ Servers Revisited
**Client-Server model**: a server delivers a service when a client requests it.

![Client-Server](media/client_server.png)

Types of servers:
- **File server** → stores common files.
- **Print server** → manages print jobs.
- **Mail server** → routes communications.
- **Compute server** → performs CPU-heavy tasks.
- **Application server** → hosts embedded apps.

![Server Network](media/print_file_server.png)


---

## 💾 Storage
- **Database servers** handle large data loads.

### Types of Backups
- **Full Backup** – Copies all data to the backup location; most secure, but time and storage heavy.  
- **Incremental Backup** – Only copies data changed since the last backup; fast and storage-efficient, but restores require chaining backups.  
- **Differential Backup** – Copies data changed since the last full backup; middle ground between full and incremental in speed and restore complexity.  
- **Mirror Backup** – Maintains an exact real-time copy of the source data; fast to restore but vulnerable if files are deleted or corrupted.  

