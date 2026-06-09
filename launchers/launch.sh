#!/bin/bash

# Check if running as root (Linux/macOS equivalent of admin)
if [ "$EUID" -ne 0 ]; then
  echo "This script must be run as root (sudo)."
  echo "Please run: sudo bash $0"
  exit 1
fi

# Go to project directory
cd "/g/myDocuments/Programming/Python/myApps/PTK6" || exit 1

# Run Python GUI app in background (no terminal blocking)
nohup pythonw main.py >/dev/null 2>&1 &

exit 0