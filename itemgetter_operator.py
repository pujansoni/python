# Problem: You have a list of dictionaries and you would like to sort the entries according to one
# or more of the dictionary values.
from operator import itemgetter
rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# The itemgetter() function can also accept multiple keys. For example, this code
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)

# The functionality of itemgetter() is sometimes replaced by lambda expressions. For
# example:
print(sorted(rows, key=lambda r: r['fname']))
print(sorted(rows, key=lambda r: (r['lname'],r['fname'])))
# This solution often works just fine. However, the solution involving itemgetter()
# typically runs a bit faster. Thus, you might prefer it if performance is a concern

# Last, but not least, don’t forget that the technique shown in this recipe can be applied
# to functions such as min() and max(). For example:
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))