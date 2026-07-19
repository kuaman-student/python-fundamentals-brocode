import os
import json
import csv
text = "Hello world"
file = open("test.txt")

print(file.read())
file.seek(0)   # Resets the cursor to the beginning
print()
print(file.read(26)) # to read first 20 chars
print()
# It is a good practice to always close the file when you are done with it.
file.close()

# You can also use the with statement when opening a file:

with open("test.txt") as f:
  print(f.read())
  f.seek(0)
  print("\n")
  print(f.readline())
  print(f.readline())

print("\n")
print("\n")

# Loop through the file line by line:
with open("test.txt") as f:
  for x in f:
    print(x)


# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content
# Note: the "w" method will overwrite the entire file.

with open("test.txt", "w") as file:
    file.write("Hello! Welcome to test.txt\nThis file is for testing purposes.")

with open("test.txt", "a") as f:
  f.write("\nNow the file has more content!")




# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exists

# "a" - Append - will create a file if the specified file does not exists

# "w" - Write - will create a file if the specified file does not exists

open("demo1.txt", "x")
open("demo2.txt", "a")
open("demo2.txt", "a")
open("demo3.txt", "w")
open("demo3.txt", "w")


os.remove("demo1.txt")
print("demo1 deleted")
os.remove("demo2.txt")
print("demo2 deleted")
os.remove("demo3.txt")
print("demo3 deleted")



open("demo3.txt", "w")
if os.path.exists("demo3.txt"):
  os.remove("demo3.txt")
  print("The file demo3 again deleted")
else:
  print("The file demo3 does not exist")

os.mkdir("test")
print("test folder created")
os.rmdir("test")
print("test folder deleted")




employee = {
  "Name" : "AK",
  "Language" : "Python",
  "College" : "IIT Mandi"
}

with open("MyData.json", "w") as f:
  json.dump(employee, f, indent=4)


colors = [
    ["White", "#FFFFFF", "rgb(100,100,100)"],
    ["Silver", "#C0C0C0", "rgb(75,75,75)"],
    ["Gray", "#808080", "rgb(50,50,50)"],
    ["Black", "#000000", "rgb(0,0,0)"],
    ["Red", "#FF0000", "rgb(100,0,0)"],
    ["Maroon", "#800000", "rgb(50,0,0)"],
    ["Yellow", "#FFFF00", "rgb(100,100,0)"],
    ["Olive", "#808000", "rgb(50,50,0)"],
    ["Lime", "#00FF00", "rgb(0,100,0)"],
    ["Green", "#008000", "rgb(0,50,0)"],
    ["Aqua", "#00FFFF", "rgb(0,100,100)"],
    ["Teal", "#008080", "rgb(0,50,50)"],
    ["Blue", "#0000FF", "rgb(0,0,100)"],
    ["Navy", "#000080", "rgb(0,0,50)"],
    ["Fuchsia", "#FF00FF", "rgb(100,0,100)"],
    ["Purple", "#800080", "rgb(50,0,50)"],
]

with open("MyCSV.csv", "w") as f:
  writer = csv.writer(f)
  for row in colors:
    writer.writerow(row)
with open("MyCSV.csv", "w", newline="") as f:
  writer = csv.writer(f)
  for row in colors:
    writer.writerow(row)