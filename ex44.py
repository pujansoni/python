from collections import deque

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, (year, mon, day) = data
print(name)
print(mon)
# If there is a mismatch in the number of elements, you’ll get an error.

# Unpacking actually works with any object that happens to be iterable, not just tuples or
# lists. This includes strings, files, iterators, and generators.
s = 'Hello'
a, b, c, d, e = s
print(a)

# When unpacking, you may sometimes want to discard certain values. Python has no
# special syntax for this, but you can often just pick a throwaway variable name for it. For example:
_, shares1, price1, _ = data
print(shares1)

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name1, email, *phone_numbers = record
print(name1)
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

# The star operation can also be useful when combined with certain kinds of processing
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(sh)

# Sometimes you might want to unpack values and throw them away.
# You can't specify a bare *, but could use common throwaway like _ or ign
record1 = ('ACME', 50, 123.45, (12, 18, 2012))
name2, *_, (*_, year2) = record1
print(name2)
print(year2)

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

# Moreover, a deque can be used whenever you need a simple queue structure.
# If you do not give it a maximum size, you get an unbounded queue that lets you append and pop items on either end.
q1 = deque()
q1.append(1)
q1.append(2)
q1.append(3)
print(q1)
q1.appendleft(4)
print(q1)
print(q1.pop())
print(q1)
print(q1.popleft())
print(q1)