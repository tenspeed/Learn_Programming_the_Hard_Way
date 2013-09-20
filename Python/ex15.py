# Import the argv module from sys so we can pass
# in arguments when we initially run the script.
from sys import argv

# Unpack the arguments in argv
script, filename = argv

# Create a variable 'txt' and use it to 'hold'
# our newly opened file.
txt = open(filename)

# Print a string telling the user what their
# file name is.
print "Here's your file %r:" % filename
# Use the read() method on 'txt' along with the
# print command to read the contents of the file
# and print them to the terminal.
print txt.read()

# Close the text file after we're done with it.
txt.close()

# Prompt the user to enter the file name again.
#print "Type the filename again:"
# Create a variable called 'file_again' and set
# it equal to the file name that the user enters.
#file_again = raw_input("> ")

# Create a variable called 'txt_again' and use it to
# 'hold'  the open file.
#txt_again = open(file_again)

# Use the read() method on 'txt_again' along with the
# print command to read the contents of the file
# and print them to the terminal.
#print txt_again.read()