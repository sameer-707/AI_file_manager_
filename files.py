from pathlib import Path
import shutil
import os
import json
import file_picker
def list_files(directory_path):
    """
    Lists all files in the specified source_dir.

    Args:
        directory_path (str): The path to the source_dir.

    Returns:
        list: A list of file names in the source_dir.
    """
    source_dir = Path(directory_path)
    files=[]
    count=0
    for f in source_dir.iterdir():
        if count>100:
            break
        if f.is_file():
            files.append(f.name)
            count+=1
    return files

def list_folders(directory_path):
    folders = []
    source_dir = Path(directory_path)
    for f in source_dir.iterdir():
        if f.is_dir():  # Changed from is_file() to is_dir()
            folders.append(f.name)
        
    
    return folders

# Function to move files to their respective folders
def organize_files(json_data, source_dir, destination_dir):
    # Create destination folders if they don't exist
    for item in json_data:
        folder_path = os.path.join(destination_dir, item["destination_folder"])
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        source_file = os.path.join(source_dir, item["file_name"])
        destination_file = os.path.join(destination_dir, item["destination_folder"], item["file_name"])

        if os.path.exists(source_file):
            shutil.move(source_file, destination_file)
            print(f"Moved: {item['file_name']} -> {item['destination_folder']}")
        else:
            print(f"File not found: {item['file_name']}")
def organize_revert(json_data, source_dir, destination_dir):
    for item in json_data:
        file=os.path.join(destination_dir, item["destination_folder"], item["file_name"])
        revert_dir=os.path.join(source_dir, item["file_name"])
        if os.path.exists(revert_dir):
            print('file'+file+'already exists, therefore skipping')
        else:
            shutil.move(file, revert_dir)
    delete_empty_folders(destination_dir)
def delete_empty_folders(source_dir):
    # Traverse the source_dir tree
    for root, dirs, files in os.walk(source_dir, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                # Check if the source_dir is empty
                if not os.listdir(dir_path):
                    os.rmdir(dir_path)  # Delete the empty source_dir
                    print(f"Deleted empty source_dir: {dir_path}")
            except Exception as e:
                print(f"Error deleting {dir_path}: {e}")

# Main program
if __name__ == "__main__":
    # Load JSON data (from a file or string)
    json_data = '''
    [
        {"file_name": "1.zip", "destination_folder": "Archives"},
        {"file_name": "all users - remove Edit in Notepad.reg", "destination_folder": "Configuration"},
        {"file_name": "brave_debullshitinator-policies.reg", "destination_folder": "Configuration"},
        {"file_name": "buffalo_trail__the_impending_storm_2014.79.3.jpg", "destination_folder": "Images"},
        {"file_name": "bundle.msixbundle", "destination_folder": "Installers"},
        {"file_name": "copyq-9.1.0-setup.exe", "destination_folder": "Installers"},
        {"file_name": "copyq-9.1.0.zip", "destination_folder": "Archives"},
        {"file_name": "current user - remove Edit in Notepad.reg", "destination_folder": "Configuration"},
        {"file_name": "download.jpg", "destination_folder": "Images"},
        {"file_name": "ec_menu.zip", "destination_folder": "Archives"},
        {"file_name": "elements_v2_cursor_by_skyeo84_dhe234j.zip", "destination_folder": "Archives"},
        {"file_name": "get-pip.py", "destination_folder": "Scripts"},
        {"file_name": "gorgeous-hyper-realistic-painting-of-a-peaceful-nature-landscape-8k-best-most-popular-free-download-wallpapers-for-macbook-pro-and-macbook-air-and-microsoft-windows-desktop-pcs-4k-07-12-2024-1733638449-hd-wallpaper.png", "destination_folder": "Images"}
    ]
    '''
    try:
        data = json.loads(json_data)  # Use json.loads() to parse JSON string
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        exit(1)

    # User-defined paths
    source_directory = os.getcwd()+"\\testing folder"
    destination_directory = os.getcwd()+"\\testing folder"
    # Organize files
    json_file_path=os.path.join(os.getcwd(),"last_output.json")
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    organize_revert(data, source_directory, destination_directory)
    