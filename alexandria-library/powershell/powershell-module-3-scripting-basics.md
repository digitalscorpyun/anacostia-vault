**🚀 Module 3: Scripting Basics**  
*Automate tasks with parameters, logic, and error handling in 15 minutes.*  

---

### **Key Concepts**  
1. **Parameters**: Inputs for scripts (`param(...)`)  
2. **Conditionals**: `if/else` logic  
3. **Loops**: `foreach` iteration  
4. **Error Handling**: `Try/Catch` blocks  

---

### **Core Script Template**  
```powershell  
param(
    [string]$ProcessName
)

Try {
    $process = Get-Process -Name $ProcessName -ErrorAction Stop
    Write-Host "$ProcessName is running (PID: $($process.Id))"
} Catch {
    Write-Host "$ProcessName not found. Starting it..."
    Start-Process $ProcessName
}
```

---

### **Drill 3: Process Monitor & Auto-Restart**  
*Task*: Create a script that restarts a process if it’s not running.  
1. Save as `ProcessWatcher.ps1`:  
   ```powershell  
   param(
       [string]$TargetProcess = "notepad"
   )

   if (Get-Process -Name $TargetProcess -ErrorAction SilentlyContinue) {
       Write-Host "$TargetProcess is already running."
   } else {
       Start-Process $TargetProcess
       Write-Host "Restarted $TargetProcess."
   }
   ```  

2. **Run it**:  
   ```powershell  
   .\ProcessWatcher.ps1 -TargetProcess "notepad"
   ```  

---

### **Pro Tips**  
- Use `-ErrorAction SilentlyContinue` to suppress errors.  
- Add logging:  
  ```powershell  
  Add-Content -Path "ProcessLog.txt" -Value "$(Get-Date): Restarted $TargetProcess"
  ```  

---

### **Next Step**  
- ✅ **Completed**: Script parameters, conditional logic.  Elasped time: 17 minutes.
- ➡️ **Next**: [[powershell-module-4-remote-management]] – Control multiple machines via PowerShell.  

**Trouble encountered:**
**Let's fix this step-by-step:**

### 1. **Save the Script Properly**
The error occurs because you didn't save the script as a `.ps1` file. Here's how to do it:

#### **Option 1: Use Notepad**
```powershell
# Create the script file
notepad ProcessWatcher.ps1
```
- Paste the script into Notepad and save.

#### **Option 2: Use PowerShell**
```powershell
# Create and save the script
@'
param([string]$TargetProcess = "notepad")

if (Get-Process -Name $TargetProcess -ErrorAction SilentlyContinue) {
    Write-Host "$TargetProcess is already running."
} else {
    Start-Process $TargetProcess
    Write-Host "Restarted $TargetProcess."
}
'@ | Out-File -FilePath ProcessWatcher.ps1 -Encoding UTF8
```

---

### 2. **Enable Script Execution**
PowerShell blocks scripts by default. Fix this:
```powershell
# Run PowerShell as Administrator first
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```
- Choose `Y` when prompted.

---

### 3. **Run the Script**
```powershell
# Navigate to your script's directory if needed
cd C:\Users\digitalscorpyun\Anacostia

# Execute the script
.\ProcessWatcher.ps1 -TargetProcess "notepad"
```

---

### ✅ **Expected Output**
```
Restarted notepad.  # If Notepad wasn't running
# OR
notepad is already running.  # If it was
```

---

### 🔍 **Troubleshooting**
- **File Location**: Ensure `ProcessWatcher.ps1` is in your current directory (check with `Get-Item .\ProcessWatcher.ps1`).
- **Permissions**: If you still get errors, run PowerShell as Administrator.

---

### 📝 **Script Improvements**
Add logging for better tracking:
```powershell
param([string]$TargetProcess = "notepad")

$logPath = "ProcessWatcher.log"

if (Get-Process -Name $TargetProcess -ErrorAction SilentlyContinue) {
    Write-Host "$TargetProcess is already running."
    Add-Content -Path $logPath -Value "$(Get-Date): $TargetProcess was running"
} else {
    Start-Process $TargetProcess
    Write-Host "Restarted $TargetProcess."
    Add-Content -Path $logPath -Value "$(Get-Date): Restarted $TargetProcess"
}
```

---

**Reply "Fixed" once the script works!** 🚀 

Ready to automate? 💻⚡
[[powershell-master-foundational-powershell-concepts]] | [[ai-ml-overview]]