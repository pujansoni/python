# You’re trying to match a block of text using a regular expression, but you need the match
# to span multiple lines.
# This problem typically arises in patterns that use the dot (.) to match any character but
# forget to account for the fact that it doesn’t match newlines. For example, suppose you
# are trying to match C-style comments:
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
... multiline comment */
... '''
print(comment.findall(text1))
print(comment.findall(text2))
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))
# In this pattern, (?:.|\n) specifies a noncapture group (i.e., it defines a group for the
# purposes of matching, but that group is not captured separately or numbered).
