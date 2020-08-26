names = ['Corey', 'Chirs', 'Dave', 'Travis']

for index, name in enumerate(names):
    print(index, name)

print("=========================")

for index, name in enumerate(names, start=1):
    print(index, name)