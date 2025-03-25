Focus 100% on core PowerShell from the book.
2-hour intensive study plan for *Learn Windows PowerShell in a Month of Lunches*:

---

### **🚀 Book-Centric Learning Plan**  
**Goal**: Master foundational PowerShell concepts in 2 hours.  

---

### **1. Critical Chapters (60 mins)**  
**Module 1 (15 mins)**: Cmdlets & Pipelines  
- **Key Commands**: `Get-Command`, `Get-Help`, `Get-Member`  
- **Drill**:  
  ```powershell
  Get-Process | Where-Object {$_.CPU -gt 50} | Select-Object Name, CPU | Export-CSV "HighCPU.csv"
  ```

**Module 2 (15 mins)**: Objects & Properties  
- **Key Concept**: Everything is an object (`.GetType()`, `| Get-Member`)  
- **Drill**:  
  ```powershell
  Get-Service | Where-Object Status -eq "Running" | Format-Table Name, DisplayName -AutoSize
  ```

**Module 3 (15 mins)**: Scripting Basics  
- **Key Syntax**: `if/else`, `foreach`, `param()`  
- **Drill**:  
  ```powershell
  param($ProcessName)
  if (Get-Process $ProcessName -ErrorAction SilentlyContinue) {
      Write-Host "$ProcessName is running!"
  } else {
      Write-Host "$ProcessName not found."
  }
  ```

**Module 4 (15 mins)**: Remote Management  
- **Key Commands**: `Enter-PSSession`, `Invoke-Command`  
- **Drill**:  
  ```powershell
  Invoke-Command -ComputerName Server01 -ScriptBlock {Get-Service WinRM}
  ```

---

### **2. Practical Scenarios (60 mins)**  
**Lab 1 (20 mins)**: File System Automation  
- List all `.log` files >30 days old:  
  ```powershell
  Get-ChildItem C:\Logs\*.log | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-30)}
  ```

**Lab 2 (20 mins)**: Service Monitoring  
- Restart crashed services automatically:  
  ```powershell
  Get-Service | Where-Object {$_.Status -eq "Stopped"} | Restart-Service -Confirm:$false
  ```

**Lab 3 (20 mins)**: User Reporting  
- Generate HTML user report:  
  ```powershell
  Get-LocalUser | ConvertTo-Html | Out-File "Users.html"
  ```

---

### **3. Book-Aligned Cheat Sheet**  
```markdown
# Core PowerShell Cheat Sheet

| Task                  | Command                          | Example                            |
|-----------------------|----------------------------------|------------------------------------|
| List commands         | `Get-Command`                    | `Get-Command *service*`            |
| Get help              | `Get-Help`                       | `Get-Help Get-Process -Examples`   |
| Filter objects        | `Where-Object`                   | `Get-Process | Where CPU -gt 50`     |
| Format output         | `Format-Table`, `Format-List`    | `Get-Service | Format-Table -AutoSize` |
| Export data           | `Export-CSV`, `Out-File`         | `Get-Process > processes.txt`      |
```

---

### **⚠️ FAQ**  
**Q**: *Why do I get "Access Denied" errors?*  
**A**: Run PowerShell as Administrator (right-click → "Run as Administrator").  

**Q**: *How to handle errors in scripts?*  
**A**: Use `Try/Catch`:  
```powershell
Try {
    Stop-Service NonExistentService -ErrorAction Stop
} Catch {
    Write-Host "Error: $_"
}
```

---

**Ready to start?** Reply with:  
- "Begin Module 1"  
- "Need simpler examples"  
- "Clarify [topic]"  

No Azure, no distractions – pure PowerShell mastery! 💻🔧
[[00-index]] | [[ai-ml-overview]] | [[ai-ml-central-hub]] | [[powershell-module-1-cmdlets-and-piplines]] | [[Computer Science - PowerShell - Cheat Sheet.md]]
