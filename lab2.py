import sys

my_items = ['gym mats', 'rigs', 'boxing gloves', 'ropes', 'treadmill', 'elliptical', 'dumbbell', 'yoga ball']
d1 = {}
search_str = ""
f = open("catalog.txt", "r")

# read file lines in a list and eliminating \n characters from each line
file_list = [z.rstrip() for z in f.readlines()]
# closing the file
f.close()
# remove empty strings
file_list_full = [i for i in file_list if i]

file_list_items = file_list_full[::3]


for element in file_list_items:
    if element in my_items:
        d1[element] = (file_list_full[file_list_full.index("element")+1], file_list_full[file_list_full.index("element")+2])
    else:
        print(element + " is not present in the my_items list")

print(d1)

while True:
    search_str = input("Enter an item to search: ")
    try:
        if search_str not in d1.keys():
            raise KeyError(search_str)
        print("The category for " + search_str + ": " + d1[search_str][0])
        print("The quantity for " + search_str + ": " + d1[search_str][1])
        while True:
            try:
                item_no = int(input("Enter how many " + search_str + " you want to order: "))
            except ValueError:
                print("Please enter a valid positive integer")
                sys.exit()
            else:
                if item_no < 0:
                    print("Negative values not accepted!")
                    continue
                else:
                    print("Your order is successful")
                    sys.exit()
    except KeyError as e:
        print("KeyError: " + str(e) + " not found")

