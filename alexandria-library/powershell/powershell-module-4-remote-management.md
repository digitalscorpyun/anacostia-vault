**🚀 Module 4: Remote Management**  
*Control multiple machines via PowerShell in 15 minutes.*  

---

### **Key Concepts**  
1. **WinRM**: Windows Remote Management (required for remote commands).  
2. **`Invoke-Command`**: Run scripts or commands on remote machines.  
3. **`Enter-PSSession`**: Interactive remote session.  

---

### **Prerequisite**  
Ensure WinRM is enabled (run as Admin):  
```powershell  
Enable-PSRemoting -Force  
```  

---

### **Drill 4: Remote Service Check**  
*Task*: Check the status of a service across multiple machines.  

1. **Script**:  
   ```powershell  
   $computers = "LocalHost", "Server01"  # Replace with actual machine names  
   $serviceName = "WinRM"  

   Invoke-Command -ComputerName $computers -ScriptBlock {  
       Get-Service -Name $using:serviceName |  
       Select-Object MachineName, Name, Status  
   }  
   ```  

2. **Run**:  
   ```powershell  
   .\RemoteServiceCheck.ps1  
   ```  

---

### **Expected Output**  
| MachineName | Name  | Status   |  
|-------------|-------|----------|  
| LocalHost   | WinRM | Running  |  
| Server01    | WinRM | Stopped  |  

---

### **Pro Tips**  
- Use `-Credential` for authenticated access:  
  ```powershell  
  $cred = Get-Credential  
  Invoke-Command -ComputerName Server01 -ScriptBlock { Get-Process } -Credential $cred  
  ```  
- Check connectivity first:  
  ```powershell  
  Test-Connection -ComputerName Server01 -Count 1  
  ```  

---

### **Next Step**  
- ✅ **Completed**: Remote command execution.  Troubles encountered:
  **Final Resolution for Server01 Connection:**

### 1. **Server01 Configuration Required**
The error indicates **WinRM isn't properly configured on Server01**. You must:

#### A. **On Server01 (the remote machine):**
```powershell
# Run in Windows PowerShell (5.1) as Administrator
Enable-PSRemoting -Force
Set-NetConnectionProfile -InterfaceAlias "Wi-Fi" -NetworkCategory Private
Restart-Service WinRM
```

#### B. **Verify WinRM Listener:**
```powershell
winrm enumerate winrm/config/listener  # Should show HTTP/HTTPS listeners
```

---

### 2. **Local Machine Fixes (Your Current PC)**
```powershell
# Add Server01 to TrustedHosts (if in a workgroup)
winrm set winrm/config/client '@{TrustedHosts="Server01"}'

# Test again with explicit credentials
$cred = Get-Credential
Test-WSMan -ComputerName Server01 -Credential $cred
```

---

### 3. **Firewall Check**
Ensure **port 5985** is open on Server01:
```powershell
# On Server01:
netsh advfirewall firewall add rule name="WinRM-HTTP" dir=in action=allow protocol=TCP localport=5985
```

---

### 4. **Final Test**
```powershell
Invoke-Command -ComputerName Server01 -Credential $cred -ScriptBlock {
    Get-Service -Name WinRM
}
```

---

**Key Takeaways**:
1. Server01 needs WinRM enabled **via Windows PowerShell 5.1** (not PowerShell 7).
2. Firewall rules must allow WinRM traffic (port 5985).
3. Use `Test-WSMan` to validate connectivity after fixes.

**If Server01 is your local machine**:  
- Run all Server01 steps in **Windows PowerShell 5.1** (search for "Windows PowerShell" in Start menu).  
- Your PowerShell 7 session won’t affect legacy WinRM configurations.  

Reply if you need help accessing Server01 directly! 🔧
- ➡️ **Final Module**: Module 5 ([[powershell-module-5-error-handling-and-debugging]]).  

Reply with:  
- **"Next module"**  
- **"Troubleshoot remote access"**  
- **"Clarify WinRM"**  

Your PowerShell journey is almost complete! 🏁
[[powershell-master-foundational-powershell-concepts]] | [[ai-ml-overview]] | [[00-index]]