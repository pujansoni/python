# functools.reduce() - repeatedly apply a function to the elements of a sequence reducing them to a single value
from functools import reduce
import operator
print(reduce(operator.add, [1, 2, 3, 4, 5]))