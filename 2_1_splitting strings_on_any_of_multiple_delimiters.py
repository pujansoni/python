# The split() method of string objects is really meant for very simple cases, and does
# not allow for multiple delimiters or account for possible whitespace around the delim‐
# iters. In cases when you need a bit more flexibility, use the re.split() method:
import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

# When using re.split(), you need to be a bit careful should the regular expression
# pattern involve a capture group enclosed in parentheses. If capture groups are used,
# then the matched text is also included in the result. For example, watch what happens
# here:
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# Getting the split characters might be useful in certain contexts. For example, maybe you
# need the split characters later on to reform an output string:
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# Reform the line using the same delimiters
print(''.join(v+d for v,d in zip(values, delimiters)))