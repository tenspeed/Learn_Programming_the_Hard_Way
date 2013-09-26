## Animal is-a object (yes, sort of confusing) look at the extra credit.
class Animal(object):
	
	def __init__(self):
		pass

## Dog is-a Animal object
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a Animal object
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object.
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person object
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	## water should be 'fresh water' or 'salt water'
	def __init__(self, name, water):
		self.name = name
		self.water = water

class Salmon(Fish):
	def __init__(self, name, water):
		super(Salmon, self).__init__(name, water)
		self.size = None

class Halibut(Fish):
	def __init__(self, name, water):
		super(Halibut, self).__init__(name, water)
		self.size = None

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet that is-a Cat
mary.pet = satan

## frank is-a Employee, has-a salary, and also is-a Person
frank = Employee("Frank", 120000)

## frank has-a pet which is-a Dog
frank.pet = rover

## flipper is-a Fish
flipper = Fish("Flipper", "salt water")

## crouse is-a Salmon
crouse =  Salmon("Crouse", "fresh water")

crouse.size = 12

## harry is-a Halibut
harry = Halibut("Harry", "salt water")

harry.size = 24

print rover.name, satan.name, mary.name, mary.pet.name
print frank.name, frank.salary, frank.pet.name, flipper.name
print flipper.water, crouse.name, crouse.water, crouse.size
print harry.name, harry.water, harry.size