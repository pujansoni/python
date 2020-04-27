# You want to search for and replace a text pattern in a string
# For simple patterns, use the str.replace() method
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))
# For more complicated patterns, use the sub() functions/methods in the re module. To
# illustrate, suppose you want to rewrite dates of the form “11/27/2012” as “2012-11-27.”
# Here is a sample of how to do it:
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))
# The first argument to sub() is the pattern to match and the second argument is the
# replacement pattern. Backslashed digits such as \3 refer to capture group numbers in
# the pattern.
# If you’re going to perform repeated substitutions of the same pattern, consider compil‐
# ing it first for better performance. For example:
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)

# For more complicated substitutions, it’s possible to specify a substitution callback func‐
# tion instead. For example:
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))
print(datepat.sub(change_date, text))

# As input, the argument to the substitution callback is a match object, as returned by
# match() or find(). Use the .group() method to extract specific parts of the match. The
# function should return the replacement text.
# If you want to know how many substitutions were made in addition to getting the
# replacement text, use re.subn() instead. For example:
newtext, n = datepat.subn(r'\3-\1-\2', text)
print(newtext)