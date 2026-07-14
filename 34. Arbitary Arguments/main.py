#  arbitrary arguments allow a function to accept an unpredictable, variable number of inputs

# *args : pass multiple non-key arguments , its tuple, Collects unnamed, ordered inputs.
# **kwargs : pass multiple key arguments, its dict, Collects named, key-value inputs.

def calculate_sum(*numbers):
    # 'numbers' is treated as a tuple
    return sum(numbers)

# Call the function with any number of inputs
print(calculate_sum(10, 20))        # Output: 30
print(calculate_sum(5, 15, 2, 8))   # Output: 30

def build_profile(**user_info):
    # 'user_info' is treated as a dictionary
    for key, value in user_info.items():
        print(f"{key}: {value}")

# Call the function with diverse key-value pairs
build_profile(username="dev_jay", role="Admin", status="Active")

def complex_function(required_id, *args, **kwargs):
    print(f"ID: {required_id}")
    print(f"Extra Positional: {args}")
    print(f"Extra Keywords: {kwargs}")

complex_function(101, "apple", "banana", theme="dark", mode="silent")
