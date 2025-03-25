**🚀 Module 1: Cmdlets & Pipelines**  
*Master PowerShell's core syntax in 15 minutes.*  

---

### **Key Concepts**  
1. **Cmdlets**: PowerShell commands (`Verb-Noun` format, e.g., `Get-Process`)  
2. **Pipelines (`|`)**: Chain cmdlets to pass output as input to the next command  
3. **Help System**: Self-documentation via `Get-Help`  

---

### **Core Commands**  
```powershell
# 1. Discover commands
Get-Command -Verb Get  # Lists all "Get-" cmdlets

# 2. Learn about a cmdlet
Get-Help Get-Process -Examples  # Shows usage examples

# 3. Inspect object properties
Get-Process | Get-Member  # Reveals properties like CPU, Name, etc.
```

---

### **Drill 1: Process Monitor**  
*Task*: List all processes using >50MB memory and export to CSV.  
```powershell
Get-Process | 
  Where-Object { $_.WS -gt 50MB } | 
  Select-Object Name, WS, CPU | 
  Export-CSV -Path "HighMemoryProcesses.csv" -NoTypeInformation
```

**Breakdown**:  
1. `Get-Process`: Fetches all running processes  
2. `Where-Object`: Filters by Working Set (memory) >50MB  
3. `Select-Object`: Keeps only key columns  
4. `Export-CSV`: Saves results to a file  

**Verify Success**:  
```powershell
Import-CSV HighMemoryProcesses.csv | Format-Table -AutoSize
```
![[Pasted image 20250315162959.png]]
---

### **Pro Tips**  
- Use `Tab` to autocomplete cmdlet names (e.g., type `Get-Pro` + `Tab` → `Get-Process`)  
- Pipe to `Get-Member` to explore any object:  
  ```powershell
  Get-Service | Get-Member  # Shows properties like Status, DisplayName
  ```

---

### **Next Step**  
- ✅ **Completed**: Basic cmdlets, pipelines, and data export  
- ➡️ **Next**: Module 2 (Objects & Properties) – Learn to manipulate and format output [[powershell-module-2-objects-and-properties]] 

Reply with:  
- "Next module"  
- "Repeat drill with services instead of processes"  
- "Clarify [concept]"  

Let’s cement these fundamentals! 💻
[[powershell-master-foundational-powershell-concepts]] | [[Computer Science - PowerShell - Cheat Sheet.md]]