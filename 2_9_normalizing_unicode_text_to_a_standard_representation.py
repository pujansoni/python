s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'
print(s1)
print(s2)
print(s1 == s2)
print('length of s1 is:', len(s1))
print('length of s2 is:', len(s2))
# Here the text “Spicy Jalapeño” has been presented in two forms. The first uses the fully
# composed “ñ” character (U+00F1). The second uses the Latin letter “n” followed by a
# “~” combining character (U+0303).
# Having multiple representations is a problem for programs that compare strings. In
# order to fix this, you should first normalize the text into a standard representation using
# the unicodedata module:
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print(t1 == t2)
print(t1)
print(ascii(t1))
t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(t3 == t4)
print(t3)
print(ascii(t3))
# Normalization can also be an important part of sanitizing and filtering text. For example,
# suppose you want to remove all diacritical marks from some text (possibly for the pur‐
# poses of searching or matching):
t1 = unicodedata.normalize('NFD', s1)
print(''.join(c for c in t1 if not unicodedata.combining(c)))