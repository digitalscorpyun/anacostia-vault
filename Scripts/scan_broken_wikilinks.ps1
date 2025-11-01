# Scan broken wikilinks in vault
Set-StrictMode -Version Latest
$vaultRoot = (Get-Location).Path
$logDir = Join-Path $vaultRoot 'scripts'
if (-not (Test-Path $logDir)) { New-Item -Path $logDir -ItemType Directory -Force | Out-Null }
$outCsv = Join-Path $logDir ("broken_wikilinks_{0}.csv" -f (Get-Date -Format 'yyyyMMdd_HHmmss'))
'SourceFile,LineNumber,LinkText,Target,CandidateMatchesCount,CandidateMatches,Context' | Out-File $outCsv -Encoding utf8

# gather all md files (exclude .git, .obsidian, scripts)
$exclude = @('.git','.obsidian','\scripts\')
$allMd = Get-ChildItem -Path $vaultRoot -Recurse -Filter '*.md' -File | Where-Object {
    $p = $_.FullName.Substring($vaultRoot.Length) -replace "^\\" , ''
    $fn = $_.FullName -replace '/','\\'
    ($fn -notmatch '\\[.]git\\') -and ($fn -notmatch '\\[.]obsidian\\') -and ($fn -notmatch '\\scripts\\')
}
Write-Host "Found $($allMd.Count) markdown files to scan."
# build index by basename (lowercase)
$index = @{}
foreach ($f in $allMd) {
    $b = [IO.Path]::GetFileNameWithoutExtension($f.Name).ToLower()
    if (-not $index.ContainsKey($b)) { $index[$b] = @() }
    $index[$b] += $f.FullName
}

# scan for wikilinks
$pattern = '\[\[([^\]]+)\]\]'
$brokenCount = 0
$totalLinks = 0
foreach ($f in $allMd) {
    $lines = Get-Content -LiteralPath $f.FullName -ErrorAction SilentlyContinue
    for ($i=0; $i -lt $lines.Count; $i++) {
        $line = $lines[$i]
        $matches = [regex]::Matches($line, $pattern)
        foreach ($m in $matches) {
            $totalLinks++
            $inside = $m.Groups[1].Value.Trim()
            $parts = $inside -split '\|',2
            $target = $parts[0].Trim()
            # strip anchor after #
            if ($target -match '#') { $target = $target.Split('#')[0] }
            # strip .md extension
            if ($target -match '\.md$') { $targetNoExt = $target.Substring(0, $target.Length - 3) } else { $targetNoExt = $target }
            # if target looks like a path (contains / or \), check literal path
            $found = $false
            $candidates = @()
            if ($targetNoExt -match '[\\/]') {
                $candidatePath = Join-Path $vaultRoot ($targetNoExt -replace '/','\\') + '.md'
                if (Test-Path -LiteralPath $candidatePath) {
                    $found = $true
                } else {
                    # also try relative to the source file's dir
                    $rel = Join-Path (Split-Path $f.FullName -Parent) ($targetNoExt -replace '/','\\') + '.md'
                    if (Test-Path -LiteralPath $rel) { $found = $true }
                }
            } else {
                $b = $targetNoExt.ToLower()
                if ($index.ContainsKey($b)) {
                    $candidates = $index[$b]
                    if ($candidates.Count -gt 0) { $found = $true }
                }
            }
            if (-not $found) {
                $brokenCount++
                $candidateStr = if ($candidates) { ($candidates -join ';') } else { '' }
                $context = ($line -replace '"','""')
                $row = '"{0}",{1},"{2}","{3}",{4},"{5}","{6}"' -f $f.FullName, ($i+1), ($m.Value -replace '"','""'), $targetNoExt -replace '"','""', ($candidates.Count -as [int]), ($candidateStr -replace '"','""'), $context
                Add-Content -Path $outCsv -Value $row
            }
        }
    }
}
Write-Host "Scan complete. Total links scanned: $totalLinks; broken links found: $brokenCount"
Write-Host "Broken links CSV: $outCsv"
exit 0
