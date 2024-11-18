# this is a python script to update my note git repo at 11:00pm
# since i usually update my obsidian vault then 
# this was created since i usually forget todo that exact thing!

import os
import subprocess
from datetime import datetime
import schedule
import time

#* Configuration
REPO_PATH = "path/to/git/repo"  # Replace with the local path to your GitHub repository
COMMIT_MESSAGE = "Add daily update file"
FILE_EXTENSION = ".txt"  # File extension for the new file

#! Function to update repo
def update_repo():
    #* Change directory to the repository
    os.chdir(REPO_PATH)
    
    #* Create a new file with the current date as the name
    file_name = f"{datetime.now().strftime('%Y-%m-%d')}{FILE_EXTENSION}"
    with open(file_name, "w") as file:
        file.write("Daily update file.\n")

    #* Stage, commit, and push changes
    try:
        subprocess.run(["git", "add", file_name], check=True)
        subprocess.run(["git", "commit", "-m", COMMIT_MESSAGE], check=True)
        subprocess.run(["git", "push"], check=True)
        print(f"Successfully updated repository with {file_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error during Git operation: {e}")

#* Schedule the job for 11:00 PM daily
schedule.every().day.at("23:00").do(update_repo)

print("Scheduled task to update repository at 11:00 PM.")

#! Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
