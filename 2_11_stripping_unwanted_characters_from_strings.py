# The strip() method can be used to strip characters from the beginning or end of a
# string. lstrip() and rstrip() perform stripping from the left or right side, respectively.
# By default, these methods strip whitespace, but other characters can be given. For
# example:
# Whitespace stripping
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# Character stripping
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('-='))