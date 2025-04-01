# Version: 2.5
# Base Directories
$BaseDir = "C:\Users\digitalscorpyun\scripts"
$CSVFile = "$BaseDir\reading-log.csv"
$NotesDir = "C:\Users\digitalscorpyun\KUSH\Anacostia\notes"

# Ensure Notes Directory Exists
if (!(Test-Path -Path $NotesDir)) {
    New-Item -Path $NotesDir -ItemType Directory | Out-Null
}

# Step 1: Log Entry into reading-log.csv
$entry = [PSCustomObject]@{
    chapter = "Chapter 2: Variables and Simple Data Types"
    pages = "19-36"
    date_read = (Get-Date).ToString("yyyy-MM-dd")
    key_takeaway = "This chapter emphasizes the importance of precision in programming..."
    reflection_action = "Incorporate robust variable naming practices..."
    excerpt = @"
In Python, strings are a series of characters enclosed in quotes. Python offers powerful tools for handling strings, such as the 'title()' method to capitalize each word, and 'upper()' or 'lower()' for formatting text uniformly. Concatenation with the '+' operator allows developers to dynamically combine strings, enabling personalized user interactions like 'Hello, Ada Lovelace!'. Python also supports whitespace manipulation with '\t' for tabs and '\n' for newlines, making outputs well-structured and easier to read. These features form the foundation for creating professional and clear programs, especially when handling user input or displaying data.
"@
    summary = "This chapter introduces variables as containers for data..."
    historical_context = "Python’s design philosophy emphasizes readability and simplicity..."
    contemporary_connection = "The string manipulation techniques covered in this chapter remain central..."
    scholarly_source = "Matthes, E. (2019). Python Crash Course..."
}

# Escape backticks in excerpt
$entry.excerpt = $entry.excerpt -replace '`', '``'

# Define CSV headers
$headers = @(
    "chapter", 
    "pages", 
    "date_read", 
    "key_takeaway", 
    "reflection_action", 
    "excerpt", 
    "summary", 
    "historical_context", 
    "contemporary_connection", 
    "scholarly_source"
)

# Create CSV if missing
if (!(Test-Path -Path $CSVFile)) {
    $headers | ConvertTo-Csv -NoTypeInformation | Select-Object -Skip 1 | Out-File -FilePath $CSVFile -Encoding UTF8
}

# Append entry to CSV
$entry | Select-Object $headers | Export-Csv -Path $CSVFile -Append -NoTypeInformation -Encoding UTF8
Write-Output "Entry logged into $CSVFile"

# Step 2: Generate Markdown Note
$file_name_timestamp = (Get-Date).ToString("yyyyMMddHHmmss")
$file_name_title = $entry.chapter -replace '\s+', '-' -replace ':', '' -replace '[^a-zA-Z0-9-]', ''
$file_name = "$NotesDir\$file_name_timestamp-$file_name_title.md"

# Build Markdown content
$markdown_content = @"
---
id: $file_name_timestamp
title: $($entry.chapter)
tags: [reading-log, python, programming]
created: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
updated: $(Get-Date -Format "yyyy-MM-dd HH:mm:ss")
---

# $($entry.chapter)

## ✊🏿 Overview
$($entry.summary)

## 🔥 Key Takeaway
$($entry.key_takeaway)

## 🌍 Reflection/Action
- **Reflection:** $($entry.reflection_action)
- **Action:** Use insights to sharpen Python programming skills.

## 📖 Excerpt
$($entry.excerpt)

## 📚 Historical Context
$($entry.historical_context)

## 🛠 Contemporary Connection
$($entry.contemporary_connection)

## 📚 Scholarly Source
$($entry.scholarly_source)
"@

# Save Markdown file
$markdown_content | Out-File -FilePath $file_name -Encoding UTF8
Write-Output "Markdown note created: $file_name"