# Import the argv module from the sys package.
from sys import argv

# Unpack the variables in argv.
script, filename = argv

# Print a couple statements telling the user we're
# going to erase the file. Give them the chance
# to cancel or confirm.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# Print the prompt "?" to the terminal
raw_input("?")

print "Opening the file..."
# Open the file and store the file object in 'target'.
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# Truncate (erase) the file.
target.truncate()

print "Now I'm going to ask you for three lines."

# Get 3 lines of input from the user.
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."

# Write each line of input to the file, placing
# a newline after each one.
contents = "%s\n%s\n%s\n" % (line1, line2, line3)
target.write(contents)

target.close()
target = open(filename)
# Print the contents of the file to the terminal.
print target.read()
print "And finally, we close it."
# Close the file before exiting the program.
target.close()