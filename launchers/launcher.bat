@echo off

:: Check for administrator privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo This script must be run as Administrator.
    echo Please right-click the file and select "Run as administrator".
    pause
    exit /b
)

:: Go to project directory
cd /d "G:\myDocuments\Programming\Python\myApps\PTK6"

:: Run Python GUI app without console window
start "" pythonw.exe main.py

exit