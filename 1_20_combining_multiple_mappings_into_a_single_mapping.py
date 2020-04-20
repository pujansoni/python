# You have multiple dictionaries or mappings that you want to logically combine into a
# single mapping to perform certain operations, such as looking up values or checking
# for the existence of keys
from collections import ChainMap

a = {'x':1, 'z':3}
b = {'y':2, 'z':4}
# Now suppose you want to perform lookups where you have to check both dictionaries
# (e.g., first checking in a and then in b if not found). An easy way to do this is to use the
# ChainMap class from the collections module. For example:
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

# A ChainMap takes multiple mappings and makes them logically appear as one. However,
# the mappings are not literally merged together. Instead, a ChainMap simply keeps a list
# of the underlying mappings and redefines common dictionary operations to scan the
# list. Most operations will work. For example:
print(len(c))
print(list(c.keys()))
print(list(c.values()))

# If there are duplicate keys, the values from the first mapping get used. Thus, the entry
# c['z'] in the example would always refer to the value in dictionary a, not the value in
# dictionary b

# Operations that mutate the mapping always affect the first mapping listed. For example:

# A ChainMap is particularly useful when working with scoped values such as variables in
# a programming language (i.e., globals, locals, etc.). In fact, there are methods that make
# this easy:
values = ChainMap()
values['x'] = 1
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
print(values)
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
# Discard last mapping
values = values.parents
print(values['x'])
print(values)

# As an alternative to ChainMap, you might consider merging dictionaries together using
# the update() method. For example:
a1 = {'x': 1, 'z': 3 }
b1 = {'y': 2, 'z': 4 }
merged = dict(b1)
merged.update(a1)
print(merged['x'])
print(merged['y'])
print(merged['z'])

# This works, but it requires you to make a completely separate dictionary object (or
# destructively alter one of the existing dictionaries). Also, if any of the original diction‐
# aries mutate, the changes don’t get reflected in the merged dictionary. For example:
a['x'] = 13
print(merged['x'])

# A ChainMap uses the original dictionaries, so it doesn’t have this behavior. For example:
a2 = {'x': 1, 'z': 3 }
b2 = {'y': 2, 'z': 4 }
merged1 = ChainMap(a2, b2)
print(merged1['x'])
a2['x'] = 42
print(merged1['x'])