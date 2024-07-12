import os
import re

def delete_duplicate_files(dir_path):
    """
    Delete duplicate files in the specified directory.
    Duplicate files are identified by a number in parentheses in their filenames.
    
    Args:
    dir_path (str): Path to the directory to clean up.
    """
    
    # List all files in the directory
    files = os.listdir(dir_path)
    
    # Iterate through the files
    for file in files:
        # Match files with a pattern: base name + (number) + extension
        match = re.match(r'(.*)\s+\((\d+)\)\.(.*)', file)
        if match:
            base_name, _, extension = match.groups()
            original_file = f"{base_name}.{extension}"
            
            # Check if the original file exists
            if original_file in files:
                # Delete the duplicate file
                os.remove(os.path.join(dir_path, file))
                print(f"Deleted duplicate file: {file}")

if __name__ == "__main__":
    # Specify the directory to clean up
    directory_to_clean = '/home/prajwal/Pictures/automation-main/File Managment/Files/Backup'
    
    # Run the function to delete duplicate files
    delete_duplicate_files(directory_to_clean)

