# computer-science-vault-reorganizer.ps1 v1.0
# Purpose: Reorganize the Anacostia Vault for Computer Science structure in Obsidian.
# Version: 1.0 (2025-03-28) - Initial script based on computer-science-index.md
# Author: DigitalScorpyun (with assistance from Grok)

# Define the vault root path
$vaultPath = "C:\Users\digitalscorpyun\Anacostia\OneDrive\Documents\Anacostia"

# Log file for debugging
$logFile = Join-Path $vaultPath "computer-science-reorganization-log.txt"

function Write-Log {
  param($Message)
  $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  "$timestamp - $Message" | Out-File -FilePath $logFile -Append -ErrorAction Stop
}

try {
  Write-Log "Starting Computer Science vault reorganization..."

  # Create top-level folder for computer-science
  $topFolders = @(
    "computer-science"
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

  # Create subfolders for computer-science
  $computerScienceSubfolders = @(
    "fundamentals",
    "software-engineering",
    "ai-ml",
    "cybersecurity",
    "cloud-computing",
    "quantum-computing"
  )
  foreach ($subfolder in $computerScienceSubfolders) {
    $path = Join-Path $vaultPath "computer-science\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created computer-science subfolder: $path"
    } else {
      Write-Log "computer-science subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for fundamentals
  $fundamentalsSubfolders = @(
    "data-structures",
    "algorithms",
    "computational-complexity",
    "programming-paradigms",
    "theory-of-computation"
  )
  foreach ($subfolder in $fundamentalsSubfolders) {
    $path = Join-Path $vaultPath "computer-science\fundamentals\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created fundamentals subfolder: $path"
    } else {
      Write-Log "fundamentals subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for software-engineering
  $softwareEngineeringSubfolders = @(
    "software-engineering-principles",
    "object-oriented-programming",
    "functional-programming",
    "version-control",
    "devops-cicd"
  )
  foreach ($subfolder in $softwareEngineeringSubfolders) {
    $path = Join-Path $vaultPath "computer-science\software-engineering\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created software-engineering subfolder: $path"
    } else {
      Write-Log "software-engineering subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for ai-ml
  $aiMlSubfolders = @(
    "neural-networks",
    "natural-language-processing",
    "ai-ethics",
    "reinforcement-learning"
  )
  foreach ($subfolder in $aiMlSubfolders) {
    $path = Join-Path $vaultPath "computer-science\ai-ml\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created ai-ml subfolder: $path"
    } else {
      Write-Log "ai-ml subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for cybersecurity
  $cybersecuritySubfolders = @(
    "information-security",
    "ethical-hacking",
    "cryptography",
    "malware-analysis"
  )
  foreach ($subfolder in $cybersecuritySubfolders) {
    $path = Join-Path $vaultPath "computer-science\cybersecurity\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created cybersecurity subfolder: $path"
    } else {
      Write-Log "cybersecurity subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for cloud-computing
  $cloudComputingSubfolders = @(
    "cloud-computing-virtualization",
    "distributed-systems",
    "edge-computing",
    "blockchain"
  )
  foreach ($subfolder in $cloudComputingSubfolders) {
    $path = Join-Path $vaultPath "computer-science\cloud-computing\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created cloud-computing subfolder: $path"
    } else {
      Write-Log "cloud-computing subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for quantum-computing
  $quantumComputingSubfolders = @(
    "quantum-computing-fundamentals",
    "computational-biology",
    "high-performance-computing",
    "emerging-technologies"
  )
  foreach ($subfolder in $quantumComputingSubfolders) {
    $path = Join-Path $vaultPath "computer-science\quantum-computing\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created quantum-computing subfolder: $path"
    } else {
      Write-Log "quantum-computing subfolder already exists, skipping: $path"
    }
  }

  Write-Log "Computer Science vault reorganization completed successfully."
} catch {
  Write-Log "Error: $($_.Exception.Message)"
  Write-Error "An error occurred: $($_.Exception.Message)"
} finally {
  Write-Log "Script execution finished."
}