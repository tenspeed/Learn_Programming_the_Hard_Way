# Define a function called add which will add two
# integers and return the result.
def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a + b
# Define a function called subtract which will
# subtract two integers and return the result.
def subtract(a,b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b
# Define a function called multiply which will
# multiply two integers and return the result.
def multiply(a,b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b
# Define a function called divide which will
# divide two integers and return the result.
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b

print "Let's do some math with just functions!"

# Call the function add and put the result in 'age'.
age = add(30, 5)
# Call the function subtract and put the result in 'height'.
height = subtract(78, 4)
# Call the function multiply and put the result in 'weight'.
weight = multiply(90, 2)
# Call the function divide and put the result in 'iq'.
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"