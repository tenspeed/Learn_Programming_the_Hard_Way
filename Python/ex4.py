# Create a variable called 'cars' and set it equal to 100.
cars = 100
# Create a variable called 'space_in_a_car' and set it equal to 4.0.
space_in_a_car = 4.0
# Create a variable called 'drivers' and set it equal to 30.
drivers = 30
# Create a variable called 'passengers' and set it equal to 90.
passengers = 90
# Create a variable called 'cars_not_driven' and set it equal to
# the difference between the variables 'cars' and 'drivers'.
cars_not_driven = cars - drivers
# Create a variable called 'cars_driven' and set it equal to
# the variable 'drivers'.
cars_driven = drivers
# Create a variable called 'carpool_capacity' and set it equal to
# the product of the variables 'cars_driven' and 'space_in_a_car'.
carpool_capacity = cars_driven * space_in_a_car
# Create a variable called 'average_passengers_per_car' and set it
# equal to the quotient of the variables 'passengers' and 'cars_driven'.
average_passengers_per_car = passengers / cars_driven

# Print a statement that tells how many cars are available.
print "There are", cars, "cars available."
# Print a statement that tells how many drivers are available.
print "There are only", drivers, "drivers available."
# Print a statement that tells how many empty cars there are today.
print "There will be", cars_not_driven, "empty cars today."
# Print a statement that tells how many people can be transported today.
print "We can transport", carpool_capacity, "people today."
# Print a statement that tells how many passengers have to carpool today.
print "We have", passengers, "to carpool today."
# Print a statement that tells how many passengers each car should carry.
print "We need to put about", average_passengers_per_car, "in each car."