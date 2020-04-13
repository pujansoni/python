# For formatting the strings in the python we can use the format method as shown below
print("The age of {0} is {1}".format("Pujan", 22))

# In the range() function the enumerate method is used to construct an
# iterable of (index, value) tuples around another iterable object
t = [6, 1234, 14324, 4124636234]
for i in enumerate(t):
    print(i)

# We can also use the tuple unpacking to avoid dealing with the tuple
for i, v in enumerate(t):
    print(f"i = {i}, v = {v}")