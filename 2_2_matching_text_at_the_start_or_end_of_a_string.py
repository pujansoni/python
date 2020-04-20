# You need to check the start or end of a string for specific text patterns, such as filename
# extensions, URL schemes, and so on.
# A simple way to check the beginning or end of a string is to use the str.starts
# with() or str.endswith() methods. For example:
import os
filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

# If you need to check against multiple choices, simply provide a tuple of possibilities to
# startswith() or endswith():
filenames = os.listdir('.')
print(filenames)
print([name for name in filenames if name.endswith(('.c', '.h'))])
print(any(name.endswith('.py') for name in filenames))

# Here is another example:
from urllib.request import urlopen
def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

# Oddly, this is one part of python where a tuple is actually required as input. If you happen
# to have the choices specified in a list or set, just make sure you convert them using tuple() first
choices1 = ['http:', 'ftp:']
url = 'http://www.python.org'

# This line will give the error
# print(url.startswith(choices1))

print(url.startswith(tuple(choices1)))