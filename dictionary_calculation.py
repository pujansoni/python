# You want to perform various calculations on a dictionary of data.
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# In order to perform useful calculations on the dictionary contents, it is often useful to
# invert the keys and values of the dictionary using zip(). For example, here is how to
# find the minimum and maximum price and stock name:
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# Similarly, to rank the data, use zip() with sorted(), as in the following:
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# When doing these calculations, be aware that zip() creates an iterator that can only be
# consumed once. For example, the following code is an error:
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names)) # OK
# print(max(prices_and_names)) # ValueError: max() arg is an empty sequence

# If you try to perform common data reductions on a dictionary, you’ll find that they only
# process the keys, not the values. For example:
print("--------------")
print(min(prices.values()))
print(max(prices.values()))

# This is probably not what you want because you’re actually trying to perform a calcu‐
# lation involving the dictionary values. You might try to fix this using the values()
# method of a dictionary:
print("--------------")
print(min(prices.values()))
print(max(prices.values()))

# Unfortunately, this is often not exactly what you want either. For example, you may want
# to know information about the corresponding keys (e.g., which stock has the lowest
# price?).
# You can get the key corresponding to the min or max value if you supply a key function
# to min() and max(). For example:
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

# However, to get the minimum value, you’ll need to perform an extra lookup step. For example:
print("--------------")
print(prices[min(prices, key=lambda k: prices[k])])

# In calculations such as min() and max(), the entry with the smallest
# or largest key will be returned if there happen to be duplicate values. For example:
prices1 = { 'AAA' : 45.23, 'ZZZ': 45.23 }
print(min(zip(prices1.values(), prices1.keys())))
print(max(zip(prices1.values(), prices1.keys())))