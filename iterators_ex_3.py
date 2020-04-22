# filter() - apply a function to each element in a sequence, constructing a
# new sequence with the elements for which the function returns True
print(list(filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])))

# Passing None as the first argument to filter() will remove elments which evaluate to False
print(list(filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'hello'])))