# Create a variable 'x' containing a string.
x = "There are %d types of people." % 10
# Create a variable 'binary' containing a string.
binary = "binary"
# Create a variable 'do_not' containing a string.
do_not = "don't"
# Create a variable 'y' containing a string.
# This is the first string within a string.
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the string contained in 'x'.
print x
# Print the string contained in 'y'.
print y

# Print the string using the %r formatter to substitute in 'x'
# into the string.
# This is the second string within a string.
# This is also a string within a string within a string O_O
print "I said: %r." % x
# Print the string using the %r formatter to substitute in 'x'
# into the string.
# This is the third string within a string.
# This is also a string within a string within a string O_O
print "I also said: '%s'." % y

# Create a variable 'hilarious' and set it equal to False.
hilarious = False
# Create a variable 'joke_evaluation' containing a string and a formatting character.
joke_evaluation = "Isn't that joke so funny?! %r"

# Print the variable 'joke_evaluation' while substituting the variable 'hilarious'
# into the string.
print joke_evaluation % hilarious

# Create a variable called 'w' containing a string.
w = "This is the left side of..."
# Create a variable called 'e' containing a string.
e = "a string with a right side."

# Print out the variables 'w' and 'e' one after the other,
# creating one longer string from the two shorter strings.
# I suppose this is technically a string within a string.
print w + e