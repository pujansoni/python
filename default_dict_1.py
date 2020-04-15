# You want to make a dictionary that maps keys to more than one value (a so-called “multidict”).
# A dictionary is a mapping where each key is mapped to a single value. If you want to
# map keys to multiple values, you need to store the multiple values in another container
# such as a list or set
# The choice of whether or not to use lists or sets depends on intended use. Use a list if
# you want to preserve the insertion order of the items. Use a set if you want to eliminate
# duplicates (and don’t care about the order).
# To easily construct such dictionaries, you can use defaultdict in the collections
# module. A feature of defaultdict is that it automatically initializes the first value so
# you can simply focus on adding items. For example:
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(5)
d['a'].append(3)
print(d)

d1 = defaultdict(set)
d1['a'].add(1)
d1['a'].add(2)
d1['b'].add(4)
d1['b'].add(5)
d1['a'].add(3)
print(d1)