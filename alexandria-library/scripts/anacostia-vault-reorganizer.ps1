# anacostia-vault-reorganizer.ps1 
# Purpose: Reorganize the Anacostia Vault structure in Obsidian.
# Version: 1.0 (2025-03-28)
# Author: DigitalScorpyun (with assistance from Grok)


# Define the vault root path
$vaultPath = "c:\users\digitalscorpyun\spencer-tullis"

# Log file for debugging
$logFile = Join-Path $vaultPath "reorganization-log.txt"
function Write-Log {
  param($Message)
  $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  "$timestamp - $Message" | Out-File -FilePath $logFile -Append
}

try {
  Write-Log "Starting vault reorganization..."

  # Create top-level folders
  $topFolders = @(
    "africana-studies",
    "alexandria-library",
    "projects",
    "personal-development",
    "zettelkasten"
  )
  foreach ($folder in $topFolders) {
    $path = Join-Path $vaultPath $folder
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory -Force | Out-Null
      Write-Log "Created top-level folder: $path"
    }
  }

  # Create subfolders for africana-studies
  $africanaSubfolders = @(
    "cultural-movements",
    "intellectual-legacies",
    "economics",
    "concepts-and-themes"
  )
  foreach ($subfolder in $africanaSubfolders) {
    $path = Join-Path $vaultPath "africana-studies\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory -Force | Out-Null
      Write-Log "Created africana-studies subfolder: $path"
    }
  }

  # Create subfolders for alexandria-library
  $alexandriaSubfolders = @(
    "science\ai-ml",
    "science\economics",
    "science\astronomy",
    "science\mathematics",
    "science\data-science",
    "templates\note-taking",
    "templates\project-planning",
    "miscellaneous\cooking\cajun-creole",
    "miscellaneous\cooking\southern-comfort",
    "miscellaneous\history-political-thought\ancient",
    "miscellaneous\history-political-thought\modern",
    "miscellaneous\holy-bible\old-testament",
    "miscellaneous\holy-bible\new-testament",
    "miscellaneous\notion"
  )
  foreach ($subfolder in $alexandriaSubfolders) {
    $path = Join-Path $vaultPath "alexandria-library\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory -Force | Out-Null
      Write-Log "Created alexandria-library subfolder: $path"
    }
  }

  # Create subfolders for projects
  $projectsSubfolders = @(
    "scripts",
    "news-scrapers",
    "ai-training",
    "bias-detection"
  )
  foreach ($subfolder in $projectsSubfolders) {
    $path = Join-Path $vaultPath "projects\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory -Force | Out-Null
      Write-Log "Created projects subfolder: $path"
    }
  }

  # Create subfolders for personal-development
  $personalSubfolders = @(
    "reskilling",
    "journaling",
    "to-do-list"
  )
  foreach ($subfolder in $personalSubfolders) {
    $path = Join-Path $vaultPath "personal-development\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory -Force | Out-Null
      Write-Log "Created personal-development subfolder: $path"
    }
  }

  # Create subfolders for zettelkasten
  $zettelSubfolders = @(
    "ideas",
    "connections"
  )
  foreach ($subfolder in $zettelSubfolders) {
    $path = Join-Path $vaultPath "zettelkasten\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory -Force | Out-Null
      Write-Log "Created zettelkasten subfolder: $path"
    }
  }

  # Move africana-studies-* folders
  $africanaFolders = Get-ChildItem -Path $vaultPath -Filter "africana-studies-*" -Directory -ErrorAction Stop
  foreach ($folder in $africanaFolders) {
    $target = switch ($folder.Name) {
      "africana-studies-sankofa" { "africana-studies\concepts-and-themes" }
      "africana-studies-w-e-b-du-bois" { "africana-studies\intellectual-legacies" }
      default { "africana-studies\movements-and-events" }
    }
    $targetPath = Join-Path $vaultPath $target
    Get-ChildItem -Path $folder.FullName | Move-Item -Destination $targetPath -ErrorAction Stop
    if (-not (Get-ChildItem -Path $folder.FullName)) {
      Remove-Item -Path $folder.FullName -ErrorAction Stop
      Write-Log "Moved and removed: $($folder.FullName) to $targetPath"
    }
  }

  # Move other folders
  $moves = @(
    @{ Source = "ai-overview"; Dest = "alexandria-library\science\ai-ml" },
    @{ Source = "notion"; Dest = "alexandria-library\miscellaneous\notion" },
    @{ Source = "advanced-powershell"; Dest = "projects\scripts" }
  )
  foreach ($move in $moves) {
    $sourcePath = Join-Path $vaultPath $move.Source
    $destPath = Join-Path $vaultPath $move.Dest
    if (Test-Path $sourcePath) {
      Move-Item -Path $sourcePath -Destination $destPath -ErrorAction Stop
      Write-Log "Moved: $sourcePath to $destPath"
    }
  }

  # Rename the index file
  $indexFile = Get-ChildItem -Path $vaultPath -Filter "*Alexandria Library - Central Knowledge Hub*" -ErrorAction Stop
  if ($indexFile) {
    Rename-Item -Path $indexFile.FullName -NewName "00-index.md" -ErrorAction Stop
    Write-Log "Renamed index file to 00-index.md"
  }

  Write-Log "Vault reorganization completed successfully."
}
catch {
  Write-Log "Error: $($_.Exception.Message)"
  Write-Error "An error occurred: $($_.Exception.Message)"
}