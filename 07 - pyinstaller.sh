#!/bin/sh

# !If a command fails then the deploy stops
set -e

printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

userinput=""

# !Prompt for the filename
echo "Please enter the Python file name to compile (without .py extension):"
read userinput

# !Check if the input is empty
if [ -z "$userinput" ]; then
    echo "No filename provided. Exiting."
    exit 1
fi

# Append .py to the user input
userinput="$userinput.py"

# !Check if the file exists
if [ ! -f "$userinput" ]; then
    echo "File '$userinput' not found. Exiting."
    exit 1
fi

printf "\033[0;32mStarting PyInstaller for '$userinput'... $(date):\033[0m\n"

# !Run the pyinstaller command with the input file
pyinstaller --onefile "$userinput"

# !Display a message when PyInstaller is done
printf "\033[0;32mPyInstaller has finished creating the executable.\033[0m\n"
