import os

file_path = "test.txt"


if os.path.exists(file_path):
    print(f"File exists")
else:
    print(f"File not exists")

if os.path.isfile(file_path):
    print("Its a file")
elif os.path.isdir(file_path):
    print("Its a directory")



tester = "test/tester.txt"
if os.path.exists(tester):
    print(f"File exists")
else:
    print(f"File not exists")