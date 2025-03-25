**🚀 Module 5: Error Handling & Debugging**  
*Resolve issues systematically and write resilient scripts in 15 minutes.*  

---

### **Key Concepts**  
1. **Error Types**: Terminating vs. non-terminating errors  
2. **Try/Catch/Finally**: Gracefully handle exceptions  
3. **Debugging Tools**: `Write-Debug`, `Set-PSBreakpoint`, `-Verbose`  
4. **Logging**: Track script execution and errors  

---

### **Drill 5: Robust Process Monitor**  
*Task*: Enhance the `ProcessWatcher.ps1` script with error handling and logging.  

```powershell  
param([string]$TargetProcess = "notepad")  

Try {  
    $process = Get-Process -Name $TargetProcess -ErrorAction Stop  
    Write-Host "$TargetProcess is running (PID: $($process.Id))"  
    Write-Debug "Process details: $($process | Out-String)"  
} Catch {  
    Write-Warning "$TargetProcess not found. Attempting to start..."  
    Try {  
        Start-Process $TargetProcess -ErrorAction Stop  
        Add-Content -Path "ProcessLog.txt" -Value "$(Get-Date): Restarted $TargetProcess"  
    } Catch {  
        Write-Error "Failed to start $TargetProcess. Details: $_"  
    }  
} Finally {  
    Write-Verbose "Script completed at $(Get-Date)"  
}  
```  

**Run with debugging**:  
```powershell  
.\ProcessWatcher.ps1 -TargetProcess "notepad" -Verbose -Debug  
```  

---

### **Pro Techniques**  
1. **Breakpoints**:  
   ```powershell  
   Set-PSBreakpoint -Script .\ProcessWatcher.ps1 -Line 5  
   ```  
   - Pauses execution at line 5 to inspect variables.  

2. **Error Variable**:  
   ```powershell  
   $Error[0]  # View the latest error  
   $Error.Clear()  # Clear error history  
   ```  

3. **Transcripts**:  
   ```powershell  
   Start-Transcript -Path "ScriptLog.txt"  
   .\ProcessWatcher.ps1  
   Stop-Transcript  
   ```  

---

### **Common Errors & Fixes**  
| **Error**                          | **Solution**                          |  
|------------------------------------|---------------------------------------|  
| `CommandNotFoundException`         | Check module installation (`Install-Module`) |  
| `Access Denied`                    | Run as Admin or adjust permissions    |  
| `WinRM Connection Issues`          | Verify `TrustedHosts`/firewall rules  |  
| `Null-valued Expression`           | Check if objects exist before use     |  

---

### **Final Challenge**  
**Add to your script**:  
- Email notification on failure (use `Send-MailMessage` if configured)  
- Retry logic for transient errors (e.g., 3 retries)  

---

### **Next Steps**  
- ✅ **Completed**: Error handling, debugging, and logging.  
- 🏁 **Mastery Achieved**: You’ve covered all core PowerShell concepts!  

**What’s next?**  
- Automate real-world tasks (disk cleanup, log analysis, etc.)  
- Explore advanced modules (e.g., `PSReadLine`, `Pester` for testing)  

Reply with:  
- **"Real-world project ideas"**  
- **"Troubleshoot my script"**  
- **"Review a concept"**  

Your PowerShell journey is now self-sustaining! 🎉🔥
[[powershell-master-foundational-powershell-concepts]] | [[ai-ml-overview]] | [[00-index]] | [[Python Learning Roadmap]]