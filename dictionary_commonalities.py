# You have two dictionaries and want to find out what they might have in common (same
# keys, same values, etc.).
a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# To find out what the two dictionaries have in common, simply perform common set
# operations using the keys() or items() methods. For example:
# Find keys in common
print(a.keys() & b.keys())

# Find keys in a that are not in b
print(a.keys() - b.keys())

# Find (key, value) pairs in common
print(a.items() & b.items())

# To make a  new dictionary with selected keys removed. Here
# is some sample code using a dictionary comprehension:
# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)