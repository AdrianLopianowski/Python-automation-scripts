import os
import shutil

def sort_files(download_path):
    file_types = {
        "Documents": ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.ppt', '.odt'],
        "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.heic', 'webp'],
        "Videos": ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv'],
        "Audio": ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
        "Archives": ['.zip', '.rar', '.tar.gz', '.7z', '.bz2', '.gz'],
        "Code": ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.ts', '.json'],
        "Executables": ['.exe', '.msi', '.bat', '.sh', '.bin'],
        "Spreadsheets": ['.xls', '.xlsx', '.ods'],
        "Presentations": ['.ppt', '.pptx', '.odp'],
        "Ebooks": ['.epub', '.mobi', '.azw3', '.pdf'],
        "System Files": ['.iso', '.dmg', '.img'],
        "Scripts": ['.sh', '.bat', '.cmd'],
        "Databases": ['.sql']
    }
    for file in os.listdir(download_path):
        file_path=os.path.join(download_path, file)

        if os.path.isfile(file_path):
            file_ext=os.path.splitext(file)[1].lower()

            for folder, extension in file_types.items():
                if file_ext in extension:
                
                    folder_path = os.path.join(download_path, folder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    print(f"Moved: {file} to {folder}")
                    break

if __name__=="__main__":
   download_directory=os.path.expanduser("~/Downloads")
   sort_files(download_directory)
