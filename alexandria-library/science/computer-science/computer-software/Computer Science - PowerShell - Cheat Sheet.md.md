> _Cmdlets are built-in PowerShell commands for specific tasks._

- **Common Cmdlets:**
    
    - `Get-Help <cmdlet>` → Get documentation
    - `Get-Command` → List available cmdlets
    - `Import-Module <module_name>` → Load a module
- **Related Notes:** [[Cmdlet Reference]] | [[PowerShell Modules]]
    

- **File Operations:**
    
    ```powershell
    Get-ChildItem       # List files (alias: ls)
    Copy-Item -Path <source> -Destination <destination>  # Copy files
    Remove-Item <path>  # Delete files
    ```
    
- **System Info:**
    
    ```powershell
    Get-ComputerInfo    # System info
    Get-Service         # Check services
    ```
    
- **Related Notes:** [[File Management]] | [[System Administration]]
    

- **Create a variable:**
    
    ```powershell
    $var = "Hello, PowerShell!"
    ```
    
- **View variable content:**
    
    ```powershell
    Write-Output $var
    ```
    
- **Delete a variable:**
    
    ```powershell
    Remove-Variable <var_name>
    ```
    
- **Related Notes:** [[PowerShell Variables]] | [[Data Types]]
    

- **For Loop:**
    
    ```powershell
    for ($i = 1; $i -le 5; $i++) {
        Write-Output "Iteration $i"
    }
    ```
    
- **If Statement:**
    
    ```powershell
    if ($condition) {
        Write-Output "Condition met!"
    } else {
        Write-Output "Condition NOT met!"
    }
    ```
    
- **Related Notes:** [[Control Flow]] | [[Scripting Basics]]
    

- **Filter processes consuming high CPU:**
    
    ```powershell
    Get-Process | Where-Object {$_.CPU -gt 100}
    ```
    
- **Export output to CSV:**
    
    ```powershell
    Get-Process | Export-Csv -Path "processes.csv" -NoTypeInformation
    ```
    
- **Related Notes:** [[Pipelines]] | [[Data Export]]
    

---

## 🔗 Related Topics

- [[PowerShell Basics]]
- [[Scripting Techniques]]
- [[Automation with PowerShell]]

## 🏷 Tags

`#PowerShell` `#Automation` `#Scripting` `#Cmdlets`

## 💡 Notes & Reflections

- PowerShell is a **versatile** tool for automating repetitive tasks.
- It **integrates seamlessly** with Windows, making it valuable for IT professionals.