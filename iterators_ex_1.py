# In python comprehensions can use multiple input sequences and multiple if-clauses
print([(x,y) for x in range(5) for y in range(3)])
values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]
print(values)

# The comprehension example can be visualized as given below
print([(x, y) for x in range(10) for y in range(x)])
result = []
for x in range(10):
    for y in range(x):
        result.append((x, y))

print(result)