from pathlib import Path

if Path('file_to_check.txt').is_file():
    print ("File exist")
else:
    print ("File not exist")