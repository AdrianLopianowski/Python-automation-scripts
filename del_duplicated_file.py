import os
import re

def delete_duplicate_files(dir_path):
  
    files = os.listdir(dir_path)
    deleted_count = 0
    
    for file in files:
            
        match = re.search(r'(.*)\s+\((\d+)\)\.(.*)', file)
        if match:
            # Get the base name and extension of the original file
            base_name = match.group(1)
            extension = match.group(3)
            original_file = base_name + '.' + extension

            # Check if the original file exists in the directory
            if original_file in files and os.path.isfile(os.path.join(dir_path, original_file)):
                os.remove(os.path.join(dir_path, file))
                deleted_count += 1
                
    print(f"Deleted {deleted_count} duplicate files.")

# Example usage
delete_duplicate_files(r"your\path\dir")
