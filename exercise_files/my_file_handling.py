from pathlib import Path

# q1 Objective: Read the content of a file and handle the case when
# the file doesn’t exist.
correct_dir = Path(__file__).parents[1]  # file path for python-basics
TEXT_FILE_NAME = 'demo_files/data.txt'
text_file_path = correct_dir / TEXT_FILE_NAME

# try:
#     with open(text_file_path, 'r', encoding='utf-8') as txt:
#         print(txt.read())
# except FileNotFoundError as fnf:
#     print(f'Error: {fnf}')
# except Exception as e:
#     print(f'Error: {e}')
# finally:
#     print('End of try block.')


# q2 Write data to a new file using a context manager
lines = ["Line 1: Hello, world!",
         "Line 2: Python file handling.",
         "Line 3: Goodbye!"]

NEW_TXT_NAME = 'demo_files/output.txt'
new_text_file_path = correct_dir / NEW_TXT_NAME
# with new_text_file_path.open(mode='w', encoding='utf-8') as new_txt:
#     new_txt.write(str(lines))
# print(new_text_file_path.exists())

# example answer:
# with open('output.txt', 'w') as file:
#     for line in lines:
#         file.write(line + "\n")

# q3
# Handle permission errors when trying to write to a file.
