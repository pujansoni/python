from sys import argv
script, filename = argv
# Take the filename from the command line and opens it
txt = open(filename)
print(f"Here's your file {filename}")
# Print the content of the file
print(txt.read())
print("Type the filename again: ")
# Take the filename form the user through input
file_again = input("> ")
txt_again = open(file_again)
# Print the content of the file
print(txt_again.read())