# You want to eliminate the duplicate values in a sequence, but preserve the order of the remaining items
# If the value in the sequence are hashable, the problem can easily be solved using a set and a generator
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))