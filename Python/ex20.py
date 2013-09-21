# Import the argv module from the sys package.
from sys import argv
# Unpack the variables given to argv.
script, input_file = argv
# Define a function called print_all which will print
# all the contents of a text file given to it.
def print_all(f):
	print f.read()
# Define a function called rewind which set's the file's
# current position to 0.
def rewind(f):
	f.seek(0)
# Define a function called print_a_line which will
# print a single line in the file.
def print_a_line(line_count, f):
	print line_count, f.readline(),
# Open the file.
current_file = open(input_file)

print "First let's print the whole file:\n"
# Call print_all and pass the file to it.
print_all(current_file)

print "Now let's rewind, kind of like a tape."
# Call rewind and pass the file to it.
rewind(current_file)

print "Let's print three lines:"

# Create a line counter.
current_line = 1
# Call print_a_line and pass it the line counter
# and the file.
print_a_line(current_line, current_file)
# Increment the line counter.
current_line += 1
# Call print_a_line and pass it the line counter
# and the file.
print_a_line(current_line, current_file)
# Increment the line counter.
current_line += 1
# Call print_a_line and pass it the line counter
# and the file.
print_a_line(current_line, current_file)