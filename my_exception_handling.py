from pathlib import Path

cwd = Path.cwd()

demo_file_path = cwd / 'demo_files' / 'my_data.txt'

# file = open(demo_file_path)
# file error because doesn't exist

try:
    file = open(demo_file_path, encoding='utf-8')
except TypeError as te:
    print(f'TypeError: {te}')
except FileNotFoundError as fnf:
    print(f'FileNotFoundError: {fnf}')
except Exception as e:
    print(f'Exception: {e}')
finally:
    print("end of try block")
