import json
import csv

text_file = "../60. Writing Files/test.txt"
json_file = "../60. Writing Files/MyData.json"
csv_file = "../60. Writing Files/MyCSV.csv"

with open(text_file, "r") as f:
    print(f.read())



with open(json_file, "r") as f:
    content = json.load(f)
    print(content)
    print(content["Name"])
    print(content["Language"])
    print(content["College"])


with open(csv_file) as f:
    content = csv.reader(f)
    print("Data")
    for line in content:
        print(line[0] + " : " + line[1])