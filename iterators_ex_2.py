# Comprehensions can be nested inside other comprehensions
# map() - apply a function to every element in a sequence, producing a new sequence
# map() is lazy - it only produces values as they're needed
print(list(map(ord, 'The quick brown fox')))

# map() can accept any number of input sequences
# The number of input sequences must match the number of function arguments