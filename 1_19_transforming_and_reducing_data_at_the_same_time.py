# A very elegant way to combine a data reduction and a transformation is to use a
# generator-expression argument. For example, if you want to calculate the sum of
# squares, do the following:
import os

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

# Determine if any .py files exist in a dictionary
files = os.listdir('.')

if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
 {'name':'GOOG', 'shares': 50},
 {'name':'YHOO', 'shares': 75},
 {'name':'AOL', 'shares': 20},
 {'name':'SCOX', 'shares': 65}
]
# Certain reduction functions such as min() and max() accept a key argument that might
# be useful in situations where you might be inclined to use a generator. For example, in
# the portfolio example, you might consider this alternative:
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
# To return the whole key we can use
min_shares1 = min(portfolio, key=lambda s: s['shares'])
print(min_shares1)