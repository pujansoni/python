from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# If the distinction matters, use fnmatchcase() instead. It matches exactly based
# on the lower and upper case conventions that apply:
print(fnmatchcase('foo.txt', '*.TXT'))

# An often overlooked feature of these functions is their potential use with data processing
# of nonfilename strings. For example, suppose you have a list of street addresses like this:
addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# The matching performed by fnmatch sits somewhere between the functionality of sim‐
# ple string methods and the full power of regular expressions. If you’re just trying to
# provide a simple mechanism for allowing wildcards in data processing operations, it’s
# often a reasonable solution. If you’re actually trying to write code that matches filenames, use the glob module
# instead