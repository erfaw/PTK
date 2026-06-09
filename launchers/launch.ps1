# Check for Administrator privileges
$isAdmin = ([Security.Principal.WindowsPrincipal] `
    [Security.Principal.WindowsIdentity]::GetCurrent()
).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "This script must be run as Administrator."
    Write-Host "Please right-click the file and select 'Run with PowerShell (Admin)'."
    pause
    exit
}

# Change directory to project path
Set-Location "G:\myDocuments\Programming\Python\myApps\PTK6"

# Run Python GUI app without opening console window
Start-Process "pythonw.exe" "main.py"

exit