# Task 9: Number of files in a folder.

import os

def numFiles(path):
    num_files = 0
    list_content = os.listdir(path)
    for content in list_content:
        if os.path.isfile(os.path.join(path, content)):
            num_files += 1
    return num_files

print(numFiles(r"C:\\Users\\Sandra\\Documents\\GitHub\\Python_code"))