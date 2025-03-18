# import the os modules to work with files
import os
from pathlib import Path

# pwd - print current working directory
print("Current working directory: ", os.getcwd())


# File paths
TEXT_FILE_NAME = "data.txt"  # caps variable name means constant value, DO NOT CHANGE

file_path_not_as_good = os.getcwd() + '/' + TEXT_FILE_NAME

# this may not work across OSs
# using os.path.join is better


file_path = os.path.join(os.getcwd() + '/' + TEXT_FILE_NAME)

# print(file_path_not_as_good, file_path)


# check if a file exists
# if (os.path.exists(file_path)):
#     print('file exists')

current_dir = Path.cwd()

# Define the text file name
TEXT_FILE_NAME = "demo_files/data.txt"

# Create the full file path
file_path = current_dir / TEXT_FILE_NAME

print(file_path)


if (Path.exists(file_path)):
    print('File Exists')
else:
    print('File Does Not Exist')
