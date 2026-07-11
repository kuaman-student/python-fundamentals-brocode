name = input("Enter your full name:\t")
print(f'\nLength: {len(name)}')
print(f'\nFind: {name.find("a")}') #return first index
print(f'\nrFind: {name.rfind("a")}')  # return last index
# return -1 if not find
print(f'\nFind: {name.find("b")}') #return first index

print(f'Capitalize: {name.capitalize()}')
print(f'lower: {name.lower()}')
print(f'upper: {name.upper()}')

print(f'is a number? : {name.isnumeric()}')
print(f'is alpha? : {name.isalpha()}')
# Contains only letters and numbers
# text1 = "Python314"
# print(text1.isalnum())  # Output: True

# # Contains only letters
# text2 = "HelloWorld"
# print(text2.isalnum())  # Output: True

# # Contains only numbers
# text3 = "2026"
# print(text3.isalnum())  # Output: True

# # Returns False due to the space
# text4 = "Python 3"
# print(text4.isalnum())  # Output: False

# # Returns False due to special characters
# text5 = "user@domain.com"
# print(text5.isalnum())  # Output: False

# # Returns False for empty strings
# text6 = ""
# print(text6.isalnum())  # Output: False


print(f'Number of a = {name.count("a")}')
print(f'Replaced name = {name.replace(" ", "-")}')

print(f'All functions of string\n {help(str)}')