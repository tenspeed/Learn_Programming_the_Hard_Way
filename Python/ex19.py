# Define a function called cheese_and_crackers which
# requires two parameters when called.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"

print "We can just give the functions numbers directly:"
# Call cheese_and_crackers and pass it two integers directly.
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# Create two variables and set them equal to integer values.
amount_of_cheese = 10
amount_of_crackers = 50
# Call cheese_and_crackers and pass the variables to it
# instead of plain integers.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# Call cheese_and_crackers and pass math equations into
# it instead of plain integers.
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
# Call cheese_and_crackers and pass variables AND math
# equations into it instead of plain integers.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)	