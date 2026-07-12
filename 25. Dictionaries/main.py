# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020,
#   Duplicate values will overwrite existing values
  "colors": ["red", "white", "blue"]
}
print(thisdict)
print(thisdict["brand"])

for this in thisdict:
    print(this)

print(len(thisdict))


# print(dir(thisdict))
#  'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

newdict = thisdict.copy()
print(newdict)

values = ["a", "b", "c"]
newdict = dict.fromkeys(values, "hello")
print(newdict)

print(thisdict.get("brand"))

if thisdict.get("brand"):
    print("yes brand exist")

print(thisdict.items())

print(thisdict.keys())

thisdict.pop("brand")
print(thisdict)

thisdict.popitem()
print(thisdict)

thisdict.setdefault("car", "ooh")
print(thisdict)

profile = {"name": "Bob", "role": "Developer"}
new_data = {"role": "Lead", "status": "Active"}

profile.update(new_data)
print(profile)
# Output: {'name': 'Bob', 'role': 'Lead', 'status': 'Active'}

thisdict["hello"] = "hello"
print(thisdict)

print(thisdict.values())

thisdict.clear()
print(thisdict)