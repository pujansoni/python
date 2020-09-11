import numpy as np
x = [1, 2, 3, 4, 5]
y = np.pad(x, (3, 2), 'constant', constant_values=(6, 4))
print(y)
z = np.pad(x, (3, 2), 'edge')
print(z)
a = np.pad(x, (3, 2), 'linear_ramp', end_values=(-4, 5))
print(a)
b = np.pad(x, (3,), 'maximum')
print(b)
c = np.pad(x, (3,), 'mean')
print(c)
d = np.pad(x, (3,), 'median')
print(d)
print("-"*20)
a1 = [[1, 2], [3, 4]]
e = np.pad(a1, (3,), 'minimum')
print(e)
