from collections import Counter
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]
morewords = ['why','are','you','not','looking','in','my','eyes']

a = Counter(words)
b = Counter(morewords)
print(a + b)
print(a - b)

# Needless to say, Counter objects are a tremendously useful tool for almost any kind of
# problem where you need to tabulate and count data. You should prefer this over man‐
# ually written solutions involving dictionaries.