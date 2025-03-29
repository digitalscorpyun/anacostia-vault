# anacostia-vault-reorganizer.ps1 v1.8
# Purpose: Reorganize the Anacostia Vault structure in Obsidian.
# Version: 1.8 (2025-03-28) - Update vault path and align with 00-index.md structure
# Author: DigitalScorpyun (with assistance from Grok)

# Define the vault root path
$vaultPath = "C:\Users\digitalscorpyun\Anacostia\OneDrive\Documents\Anacostia"

# Log file for debugging
$logFile = Join-Path $vaultPath "reorganization-log.txt"

function Write-Log {
  param($Message)
  $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  "$timestamp - $Message" | Out-File -FilePath $logFile -Append -ErrorAction Stop
}

try {
  Write-Log "Starting vault reorganization..."

  # Create top-level folders based on 00-index.md categories
  $topFolders = @(
    "algebra",
    "python-programming",
    "ai-ml",
    "africana-studies",
    "personal-development",
    "career-development",
    "history-political-thought",
    "the-lion-of-anacostia"
  )
  foreach ($folder in $topFolders) {
    $path = Join-Path $vaultPath $folder
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created top-level folder: $path"
    } else {
      Write-Log "Top-level folder already exists, skipping: $path"
    }
  }

  # Create subfolders for algebra
  $algebraSubfolders = @(
    "graphing-linear-equations-unit-22",
    "systems-of-linear-equations-unit-23",
    "inequalities-unit-24",
    "functions-unit-25",
    "quadratic-equations-unit-26",
    "exponential-functions-unit-27",
    "polynomials-unit-28",
    "rational-expressions-unit-29",
    "radical-expressions-unit-30"
  )
  foreach ($subfolder in $algebraSubfolders) {
    $path = Join-Path $vaultPath "algebra\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created algebra subfolder: $path"
    } else {
      Write-Log "algebra subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for python-programming
  $pythonSubfolders = @(
    "python-basics",
    "python-libraries",
    "oop-in-python"
  )
  foreach ($subfolder in $pythonSubfolders) {
    $path = Join-Path $vaultPath "python-programming\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created python-programming subfolder: $path"
    } else {
      Write-Log "python-programming subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for ai-ml
  $aiMlSubfolders = @(
    "neural-networks",
    "ai-ethics",
    "real-world-applications"
  )
  foreach ($subfolder in $aiMlSubfolders) {
    $path = Join-Path $vaultPath "ai-ml\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created ai-ml subfolder: $path"
    } else {
      Write-Log "ai-ml subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for africana-studies
  $africanaSubfolders = @(
    "harlem-renaissance",
    "african-diaspora-themes",
    "black-technology-innovators",
    "african-american",
    "lion-of-anacostia"
  )
  foreach ($subfolder in $africanaSubfolders) {
    $path = Join-Path $vaultPath "africana-studies\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created africana-studies subfolder: $path"
    } else {
      Write-Log "africana-studies subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for personal-development
  $personalSubfolders = @(
    "goal-setting",
    "productivity-strategies",
    "mindfulness-practice"
  )
  foreach ($subfolder in $personalSubfolders) {
    $path = Join-Path $vaultPath "personal-development\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created personal-development subfolder: $path"
    } else {
      Write-Log "personal-development subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for career-development
  $careerSubfolders = @(
    "reskilling-for-tech",
    "soft-skills-for-it",
    "networking-strategies"
  )
  foreach ($subfolder in $careerSubfolders) {
    $path = Join-Path $vaultPath "career-development\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created career-development subfolder: $path"
    } else {
      Write-Log "career-development subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for history-political-thought
  $historySubfolders = @(
    "on-tyranny",
    "anticipatory-obedience",
    "mass-media-and-political-influence",
    "the-rise-of-totalitarianism"
  )
  foreach ($subfolder in $historySubfolders) {
    $path = Join-Path $vaultPath "history-political-thought\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created history-political-thought subfolder: $path"
    } else {
      Write-Log "history-political-thought subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for the-lion-of-anacostia
  $lionSubfolders = @(
    "bias-detection",
    "real-world-applications"
  )
  foreach ($subfolder in $lionSubfolders) {
    $path = Join-Path $vaultPath "the-lion-of-anacostia\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created the-lion-of-anacostia subfolder: $path"
    } else {
      Write-Log "the-lion-of-anacostia subfolder already exists, skipping: $path"
    }
  }

  # Move africana-studies-* folders
  $africanaFolders = Get-ChildItem -Path $vaultPath -Filter "africana-studies-*" -Directory -ErrorAction Stop
  foreach ($folder in $africanaFolders) {
    $target = switch ($folder.Name) {
      "africana-studies-sankofa" { "africana-studies\harlem-renaissance" }
      "africana-studies-w-e-b-du-bois" { "africana-studies\lion-of-anacostia" }
      default { "africana-studies\african-diaspora-themes" }
    }
    $targetPath = Join-Path $vaultPath $target
    Get-ChildItem -Path $folder.FullName | Move-Item -Destination $targetPath -Force -ErrorAction Stop
    if (-not (Get-ChildItem -Path $folder.FullName)) {
      Remove-Item -Path $folder.FullName -ErrorAction Stop
      Write-Log "Moved and removed: $($folder.FullName) to $targetPath"
    }
  }

  # Move other folders
  $moves = @(
    @{ Source = "ai-overview"; Dest = "ai-ml\overview" },
    @{ Source = "advanced-powershell"; Dest = "python-programming\powershell" }
  )
  foreach ($move in $moves) {
    $sourcePath = Join-Path $vaultPath $move.Source
    $destPath = Join-Path $vaultPath $move.Dest
    if (Test-Path $sourcePath) {
      Move-Item -Path $sourcePath -Destination $destPath -Force -ErrorAction Stop
      Write-Log "Moved: $sourcePath to $destPath"
    }
  }

  # Rename the index file
  $indexFile = Get-ChildItem -Path $vaultPath -Filter "*lexandria Library - Central Knowledge Hub*" -ErrorAction Stop
  if ($indexFile) {
    Rename-Item -Path $indexFile.FullName -NewName "00-index.md" -ErrorAction Stop
    Write-Log "Renamed index file to 00-index.md"
  }

  Write-Log "Vault reorganization completed successfully."
} catch {
  Write-Log "Error: $($_.Exception.Message)"
  Write-Error "An error occurred: $($_.Exception.Message)"
} finally {
  Write-Log "Script execution finished."
}