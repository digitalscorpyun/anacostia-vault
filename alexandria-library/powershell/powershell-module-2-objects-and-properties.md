**🚀 Module 2: Objects & Properties**  
*Master PowerShell’s object-oriented nature in 15 minutes.*  

---

### **Key Concepts**  
1. **Everything is an object**: Outputs have properties (data) and methods (actions).  
2. **Property Access**: Use `Select-Object`, dot notation (`$process.Name`), or `Format-*` cmdlets.  
3. **Methods**: Actions you can perform on objects (e.g., `$service.Stop()`).  

---

### **Core Commands**  
```powershell  
# 1. Explore object properties  
Get-Service | Get-Member  # Shows all properties/methods of service objects  

# 2. Select specific properties  
Get-Process | Select-Object Name, CPU, WS  # WS = Working Set (memory)  

# 3. Format output  
Get-Service | Format-Table -Property Name, Status, DisplayName -AutoSize  
```

---

### **Drill 2: Service Monitor**  
*Task*: List all **stopped** services and save their names + descriptions to a file.  
```powershell  
Get-Service |  
  Where-Object { $_.Status -eq "Stopped" } |  
  Select-Object Name, DisplayName |  
  Export-CSV "StoppedServices.csv" -NoTypeInformation  
```  

**Breakdown**:  
1. `Get-Service`: Retrieves all services  
2. `Where-Object`: Filters for `Status = Stopped`  
3. `Select-Object`: Keeps only `Name` and `DisplayName`  
4. `Export-CSV`: Saves the results  

**Verify**:  
```powershell  
Import-CSV StoppedServices.csv | Format-Table -AutoSize  
```  

---

### **Pro Tips**  
- Use `Format-List *` to show **all properties** of an object:  
  ```powershell  
  Get-Process -Name "explorer" | Format-List *  
  ```  
![[Pasted image 20250315172416.png]]
- Avoid piping `Format-*` to `Export-CSV` (it corrupts data structure).  

---

### **Next Step**  
- ✅ **Completed**: Object inspection, property selection, and advanced filtering.  Elapsed time: 30 minutes.
- ➡️ **Next**: Module 3 (Scripting Basics) – Build reusable scripts with parameters and logic.  

Reply with:  
- "Next module"  
- "Repeat drill with processes instead of services"  
- "Explain methods vs. properties"  

Let’s turn data into actionable insights! 💡
[[powershell-master-foundational-powershell-concepts]] | [[Computer Science - PowerShell - Cheat Sheet.md]]
[[powershell-module-3-scripting-basics]]
