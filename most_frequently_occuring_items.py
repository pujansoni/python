# You have a sequence of items, and you’d like to determine the most frequently occurring
# items in the sequence.
# The collections.Counter class is designed for just such a problem. It even comes with
# a handy most_common() method that will give you the answer.
from collections import Counter

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)
# To count a specific words use the syntax given below
print(word_counts['not'])
print(word_counts['eyes'])