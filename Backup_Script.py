import shutil
import datetime
import os
import sys


def backup_directory(source_directory, backup_directory):
    current_time=datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder_name= f"backup_{current_time}"
    backup_path = os.path.join(backup_directory, backup_folder_name)

    try:
        os.makedirs(backup_path)

        shutil.copytree(source_directory, os.path.join(backup_path, os.path.basename(source_directory)))

        print(f"Backup successful! Backup created at: {backup_path}")

    except Exception as error:
        print(f"An error occurred while backing up: {error}")


if __name__=="__main__":
    source_dir=input("input a path of the directory you want to back up: ")
    backup_dir= input("Enter the path where you want to store the backup: ")

    backup_directory(source_dir, backup_dir)