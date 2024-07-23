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
        '''
        Match files with a pattern:- 
            {base name + (number) + extension} & {base name + " (Copy number)" + extension}
        Eg: If Original = Screenshot, and Dublicates: Screenshot (2).png, Screenshot (3).png,
          Screenshot (Copy 2).png, Screenshot (Copy 3).png
        Then the program will delete Screenshot (2).png, Screenshot (3).png, Screenshot (Copy 2).png, 
        and Screenshot (Copy 3).png
        '''
        match_number = re.match(r'(.*)\s+\((\d+)\)\.(.*)', file)
        match_copy = re.match(r'(.*)\s+\(Copy (\d+)\)\.(.*)', file)

        if match_number:
            base_name, _, extension = match_number.groups()
            original_file = f"{base_name.strip()}.{extension}"

        elif match_copy:
            base_name, _, extension = match_copy.groups()
            original_file = f"{base_name.strip()}.{extension}"

        else:
            continue

        # Check if the original file exists
        if original_file in files:
            # Delete the duplicate file
            os.remove(os.path.join(dir_path, file))
            print(f"Deleted duplicate file: {file}")

if __name__ == "__main__":
    # Specify the directory to clean up
    directory_to_clean = '/home/prajwal/Downloads/Test'#Give your path here
    
    # Run the function to delete duplicate files
    delete_duplicate_files(directory_to_clean)

