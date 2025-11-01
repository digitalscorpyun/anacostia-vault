<#
Usage: Run from vault root (PowerShell)
  powershell -ExecutionPolicy Bypass -File .\scripts\update_wikilinks_from_master.ps1
What it does:
  - Finds the latest `master_move_log_*.csv` in the vault root
  - Builds a mapping from old basename (no .md) -> new relative path (no .md)
  - Scans all .md files (recursively), skipping the scripts folder and .git/.obsidian folders
  - For each file, backs it up to filename.linkbak_TIMESTAMP if any edits would be made
  - Rewrites wikilinks of the form [[target]] or [[path/target|alias]] where target's basename matches a moved file
  - Writes a CSV log of changes: scripts/link_update_log_YYYYMMDD_HHMMSS.csv
Notes:
  - This is conservative: it replaces only when the basename matches a moved file. It preserves aliases.
  - Always review the generated CSV and backups before committing changes.
#>

Set-StrictMode -Version Latest
$vaultRoot = (Get-Location).Path
# locate master log
$master = Get-ChildItem -Path $vaultRoot -Filter 'master_move_log_*.csv' | Sort-Object LastWriteTime | Select-Object -Last 1
if (-not $master) { Write-Error "No master_move_log_*.csv found in $vaultRoot. Aborting."; exit 1 }
Write-Host "Using master log: $($master.FullName)"
$rows = Import-Csv $master.FullName | Where-Object { $_.Action -eq 'MOVED' }
if (-not $rows) { Write-Host "No MOVED rows in master log; nothing to do."; exit 0 }

# Build mapping: oldBasename -> newRelativePathNoExt (unix-style slashes for Obsidian)
$map = @{}
foreach ($r in $rows) {
    $srcLeaf = Split-Path $r.Source -Leaf
    $oldBase = [IO.Path]::GetFileNameWithoutExtension($srcLeaf)
    $destPath = Resolve-Path $r.Destination -ErrorAction SilentlyContinue
    if (-not $destPath) { continue }
    $rel = $destPath.Path.Replace($vaultRoot + '\\', '') -replace '\\','/'
    $relNoExt = [System.IO.Path]::Combine((Split-Path $rel -Parent), [System.IO.Path]::GetFileNameWithoutExtension($rel)) -replace '\\','/'
    # Normalize when parent is '.' (root)
    if ($relNoExt -like '*/*') { $norm = $relNoExt } else { $norm = [System.IO.Path]::GetFileNameWithoutExtension($rel) }
    $map[$oldBase.ToLower()] = $norm
}

if ($map.Count -eq 0) { Write-Host "No valid mappings found. Aborting."; exit 0 }
Write-Host "Mapping count: $($map.Count)"

# Prepare log
$logDir = Join-Path $vaultRoot 'scripts'
if (-not (Test-Path $logDir)) { New-Item -Path $logDir -ItemType Directory -Force | Out-Null }
$logFile = Join-Path $logDir ("link_update_log_{0}.csv" -f (Get-Date -Format "yyyyMMdd_HHmmss"))
'File,ChangesCount,ChangedLinks' | Out-File $logFile -Encoding utf8

# File search: exclude scripts, .git, .obsidian
$excludeFolders = @('\.git','\.obsidian','scripts')
$mdFiles = Get-ChildItem -Path $vaultRoot -Recurse -Filter '*.md' -File | Where-Object {
    $p = $_.FullName.Replace($vaultRoot + '\\','')
    -not ($excludeFolders | ForEach-Object { $p -match [regex]::Escape($_) })
}

$updateCount = 0
foreach ($f in $mdFiles) {
    $text = Get-Content -Path $f.FullName -Raw -ErrorAction SilentlyContinue
    if ($null -eq $text) { continue }
    $orig = $text
    $changed = $false
    # pattern to find wikilinks [[...]]
    $pattern = '\[\[([^\]]+)\]\]'
    $newText = [regex]::Replace($text, $pattern, {
        param($m)
        $inside = $m.Groups[1].Value.Trim()
        # split target and alias on '|'
        $parts = $inside -split '\|',2
        $target = $parts[0].Trim()
        $alias = if ($parts.Count -gt 1) { $parts[1] } else { $null }
        # strip trailing .md if present
        $targetNoExt = if ($target -match '\.md$') { $target.Substring(0, $target.Length - 3) } else { $target }
        # take last path segment as basename
        $seg = $targetNoExt -split '/' | Select-Object -Last 1
        $lower = $seg.ToLower()
        if ($map.ContainsKey($lower)) {
            $newTarget = $map[$lower]
            # if original target already contains the newTarget, skip
            if ($targetNoExt -eq $newTarget -or $targetNoExt -like "*/$newTarget") { return $m.Value }
            $changed = $true
            if ($alias) { return "[[${newTarget}|${alias}]]" } else { return "[[${newTarget}]]" }
        } else {
            return $m.Value
        }
    })

    if ($newText -ne $orig) {
        # backup original
        $bak = $f.FullName + ".linkbak_" + (Get-Date -Format yyyyMMdd_HHmmss)
        Copy-Item -Path $f.FullName -Destination $bak -Force
        # write updated content
        Set-Content -Path $f.FullName -Value $newText -Encoding utf8
        # log
        $changedLinks = ([regex]::Matches($newText, $pattern) | ForEach-Object { $_.Groups[1].Value }) -join ';'
        $line = '"{0}",{1},"{2}"' -f $f.FullName, ([regex]::Matches($orig,$pattern).Count - ([regex]::Matches($newText,$pattern).Count)), ($changedLinks -replace '"','""')
        Add-Content -Path $logFile -Value $line
        $updateCount++
    }
}

Write-Host "Link update complete. Files updated: $updateCount. Log: $logFile"
Write-Host "Backups created for modified files with suffix .linkbak_TIMESTAMP"

exit 0
