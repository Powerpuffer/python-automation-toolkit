import os
import shutil

def organize_folder(folder_path):
    """
    Organizes all files in the given folder into subfolders by file extension.
    Example: file.pdf -> /pdf/file.pdf
    """
    if not os.path.exists(folder_path):
        print(f"Error: Folder {folder_path} does not exist.")
        return

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1].lower()
            target_folder = os.path.join(folder_path, ext)
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))
    print("Files organized successfully!")

if __name__ == "__main__":
    folder = input("Enter the full path of the folder to organize: ")
    organize_folder(folder)