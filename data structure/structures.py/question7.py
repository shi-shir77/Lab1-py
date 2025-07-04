# Write a Python program to merge two dictionaries and sum the values of
# common keys.
dict1 = {'a':10, 'b': 40, 'c':50}
dict2 = {'a': 40, 'b': 50, 'd':45}

print(f"Original dictionary 1: {dict1}")
print(f"Original dictionary 2: {dict2}")

for key, value in (dict1.items()):
    if key in dict2:
        dict2[key] = value + dict2[key]
    else:
        dict2[key] = dict1[key]

print(f"Updated dictionary 2: {dict2}")