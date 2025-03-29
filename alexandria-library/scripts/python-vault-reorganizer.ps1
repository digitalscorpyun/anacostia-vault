# python-vault-reorganizer.ps1 v1.1
# Purpose: Reorganize the Anacostia Vault for Python learning and libraries in Obsidian.
# Version: 1.1 (2025-03-28) - Add library structure from python-libraries.md
# Author: DigitalScorpyun (with assistance from Grok)

# Define the vault root path
$vaultPath = "C:\Users\digitalscorpyun\Anacostia\OneDrive\Documents\Anacostia"

# Log file for debugging
$logFile = Join-Path $vaultPath "python-reorganization-log.txt"

function Write-Log {
  param($Message)
  $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
  "$timestamp - $Message" | Out-File -FilePath $logFile -Append -ErrorAction Stop
}

try {
  Write-Log "Starting Python vault reorganization..."

  # Create top-level folder for python-programming
  $topFolders = @(
    "python-programming"
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

  # Create subfolders for Python learning stages
  $pythonStages = @(
    "stage-1-python-basics",
    "stage-2-intermediate-python",
    "stage-3-object-oriented-programming",
    "stage-4-python-libraries-frameworks",
    "stage-5-advanced-python",
    "stage-6-python-for-ai-ml"
  )
  foreach ($stage in $pythonStages) {
    $path = Join-Path $vaultPath "python-programming\$stage"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created python stage folder: $path"
    } else {
      Write-Log "python stage folder already exists, skipping: $path"
    }
  }

  # Create subfolders for Stage 1: Python Basics
  $stage1Subfolders = @(
    "data-types",
    "variables-constants",
    "control-flow",
    "functions-recursion",
    "list-tuple-dictionary"
  )
  foreach ($subfolder in $stage1Subfolders) {
    $path = Join-Path $vaultPath "python-programming\stage-1-python-basics\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created stage-1 subfolder: $path"
    } else {
      Write-Log "stage-1 subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for Stage 2: Intermediate Python
  $stage2Subfolders = @(
    "list-comprehensions",
    "lambda-functions",
    "error-handling",
    "file-handling",
    "modules-packages"
  )
  foreach ($subfolder in $stage2Subfolders) {
    $path = Join-Path $vaultPath "python-programming\stage-2-intermediate-python\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created stage-2 subfolder: $path"
    } else {
      Write-Log "stage-2 subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for Stage 3: Object-Oriented Programming
  $stage3Subfolders = @(
    "classes-objects",
    "methods-attributes",
    "inheritance-polymorphism",
    "encapsulation-abstraction"
  )
  foreach ($subfolder in $stage3Subfolders) {
    $path = Join-Path $vaultPath "python-programming\stage-3-object-oriented-programming\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created stage-3 subfolder: $path"
    } else {
      Write-Log "stage-3 subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for Stage 4: Python Libraries & Frameworks
  $stage4Subfolders = @(
    "numpy",
    "pandas",
    "matplotlib-seaborn",
    "requests",
    "flask"
  )
  foreach ($subfolder in $stage4Subfolders) {
    $path = Join-Path $vaultPath "python-programming\stage-4-python-libraries-frameworks\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created stage-4 subfolder: $path"
    } else {
      Write-Log "stage-4 subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for Stage 5: Advanced Python Concepts
  $stage5Subfolders = @(
    "generators-iterators",
    "decorators",
    "multithreading-multiprocessing",
    "regular-expressions",
    "unit-testing-mocking"
  )
  foreach ($subfolder in $stage5Subfolders) {
    $path = Join-Path $vaultPath "python-programming\stage-5-advanced-python\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created stage-5 subfolder: $path"
    } else {
      Write-Log "stage-5 subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for Stage 6: Python for AI & Machine Learning
  $stage6Subfolders = @(
    "machine-learning",
    "tensorflow",
    "pytorch",
    "ai-ethics"
  )
  foreach ($subfolder in $stage6Subfolders) {
    $path = Join-Path $vaultPath "python-programming\stage-6-python-for-ai-ml\$subfolder"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created stage-6 subfolder: $path"
    } else {
      Write-Log "stage-6 subfolder already exists, skipping: $path"
    }
  }

  # Create subfolders for Python Libraries
  $libraryCategories = @(
    "core-libraries",
    "data-science-ml",
    "web-development-apis",
    "automation-scripting",
    "cybersecurity-ethical-hacking"
  )
  foreach ($category in $libraryCategories) {
    $path = Join-Path $vaultPath "python-programming\libraries\$category"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created library category folder: $path"
    } else {
      Write-Log "library category folder already exists, skipping: $path"
    }
  }

  # Create subfolders for Core Libraries
  $coreLibraries = @(
    "os",
    "sys",
    "re",
    "json",
    "logging"
  )
  foreach ($library in $coreLibraries) {
    $path = Join-Path $vaultPath "python-programming\libraries\core-libraries\$library"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created core library folder: $path"
    } else {
      Write-Log "core library folder already exists, skipping: $path"
    }
  }

  # Create subfolders for Data Science & ML Libraries
  $dataScienceLibraries = @(
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn",
    "tensorflow",
    "pytorch"
  )
  foreach ($library in $dataScienceLibraries) {
    $path = Join-Path $vaultPath "python-programming\libraries\data-science-ml\$library"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created data science library folder: $path"
    } else {
      Write-Log "data science library folder already exists, skipping: $path"
    }
  }

  # Create subfolders for Web Development & APIs
  $webDevLibraries = @(
    "flask",
    "django",
    "requests",
    "beautifulsoup",
    "fastapi"
  )
  foreach ($library in $webDevLibraries) {
    $path = Join-Path $vaultPath "python-programming\libraries\web-development-apis\$library"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created web development library folder: $path"
    } else {
      Write-Log "web development library folder already exists, skipping: $path"
    }
  }

  # Create subfolders for Automation & Scripting
  $automationLibraries = @(
    "shutil",
    "subprocess",
    "selenium",
    "pyautogui"
  )
  foreach ($library in $automationLibraries) {
    $path = Join-Path $vaultPath "python-programming\libraries\automation-scripting\$library"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created automation library folder: $path"
    } else {
      Write-Log "automation library folder already exists, skipping: $path"
    }
  }

  # Create subfolders for Cybersecurity & Ethical Hacking
  $cybersecurityLibraries = @(
    "scapy",
    "cryptography",
    "requests",
    "socket"
  )
  foreach ($library in $cybersecurityLibraries) {
    $path = Join-Path $vaultPath "python-programming\libraries\cybersecurity-ethical-hacking\$library"
    if (-not (Test-Path $path)) {
      New-Item -Path $path -ItemType Directory | Out-Null
      Write-Log "Created cybersecurity library folder: $path"
    } else {
      Write-Log "cybersecurity library folder already exists, skipping: $path"
    }
  }

  Write-Log "Python vault reorganization completed successfully."
} catch {
  Write-Log "Error: $($_.Exception.Message)"
  Write-Error "An error occurred: $($_.Exception.Message)"
} finally {
  Write-Log "Script execution finished."
}