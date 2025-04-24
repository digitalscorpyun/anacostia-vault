<#

.SYNOPSIS

Weekly task automation for the Anacostia Vault.

Adds recurring weekly tasks to to-do-list.md and logs task completion count.

  

.AUTHOR

digitalscorpyun

  

.NOTES

Version: 1.3

Date: 2025-04-08

Vault Path: C:\Users\digitalscorpyun\KUSH\Anacostia

#>

  

# === CONFIGURATION ===

$vaultPath = "C:\Users\digitalscorpyun\KUSH\Anacostia"

$todoFile = Join-Path $vaultPath "to-do-list.md"

$logFile = Join-Path $vaultPath "weekly-log.txt"

  

# === FUNCTION: Completed Task Summary ===

function Get-CompletedTaskSummary {

    if (-not (Test-Path $todoFile)) {

        Write-Host "⚠️  Warning: Could not find to-do-list.md at $todoFile"

        return

    }

  

    $completed = Select-String -Path $todoFile -Pattern "^\s*-\s*\[x\]" -SimpleMatch

    $count = $completed.Count

    $date = Get-Date -Format "yyyy-MM-dd"

  

    Write-Host "`n--- Weekly Summary for $date ---"

    Write-Host "✅ Completed Tasks: $count"

    "$date - Completed Tasks: $count" | Out-File -Append $logFile -Encoding UTF8

}

  

# === FUNCTION: Add Weekly Task Block ===

function Add-WeeklyTasks {

    if (-not (Test-Path $todoFile)) {

        Write-Host "⚠️  Warning: Could not find to-do-list.md at $todoFile"

        return

    }

  

    $existing = Get-Content $todoFile -Raw

    if ($existing -match "## Weekly Review Actions") {

        Write-Host "⏭ Weekly tasks already exist. Skipping injection."

        return

    }

  

    $weeklyTasks = @"

## 🔁 Weekly Review Actions

  

- [ ] Audit backlink health via validate_backlinks.py

- [ ] Add all new research outputs to [[scorpyunsummaries]]

- [ ] Sync vault with Git for version control

- [ ] Re-run graph_view_optimizer.py weekly

  

"@

  

    Add-Content -Path $todoFile -Value $weeklyTasks

    Write-Host "📝 Weekly task block added to to-do-list.md"

}

  

# === EXECUTION ===

Write-Host "`n🚀 Running Weekly To-Do Populator..."

Get-CompletedTaskSummary

Add-WeeklyTasks

Write-Host "`n🎯 Weekly task routine complete! Check to-do-list.md and logs for updates."
