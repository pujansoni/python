# If you are trying to eliminate duplicates in a sequence of unhashable types, you can make a slight change to this recipe
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
# If you want to eliminate duplicates based on the value of a single field then use the solution given below
print(list(dedupe(a, key=lambda d: (d['x'],d['y']))))
# The duplicates can also be eliminated by using the set operator but it does not preserve any kind of ordering