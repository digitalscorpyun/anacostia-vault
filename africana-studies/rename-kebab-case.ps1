# Set the directory to africana-studies
$directory = "C:\Users\miker\OneDrive\Documents\Anacostia\africana-studies"

# Get all markdown files in africana-studies, including subfolders
$files = Get-ChildItem -Path $directory -Recurse -Filter "*.md"

foreach ($file in $files) {
    # Convert filename to lowercase
    $newName = $file.Name.ToLower()

    # Replace spaces and underscores with hyphens
    $newName = $newName -replace "[_ ]", "-"

    # Remove redundant prefix "africana-studies-" if it appears at the start
    $newName = $newName -replace "^africana-studies-", ""

    # Ensure the new name is different before renaming
    if ($newName -ne $file.Name) {
        $newPath = Join-Path -Path $file.DirectoryName -ChildPath $newName
        Rename-Item -Path $file.FullName -NewName $newPath
        Write-Output "Renamed: $($file.Name) → $newName"
    }
}
