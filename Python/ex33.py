def number_list(increment):
	i = 0
	last_num = increment * 10
	numbers = []

	while i < last_num:
		print "At the top i is %d" % i
 		numbers.append(i)

 		i += increment
 		print "Numbers now: ", numbers
 		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

def second_number_list():
	numbers = []

	for i in range(0, 11):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

number_list(5)
second_number_list()