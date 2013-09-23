# Define a function called break_words that will take a string
# and break up all the words into a list of words.
# The function then returns the list of words.
def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words
# Define a function called sort_words which, when passed a list
# of words, will sort them in alphabetical order. The function
# returns the list with the sorted words. (the original list is
# overwritten).
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
# Define a function called print_first_word which takes a list
# of words, removes the first word from the list, and stores it
# in a variable which gets printed to the terminal. This modifies
# the original list by removing the first word from it.
def print_first_word(words):
	"""Prints the first word after popping it off."""
	word = words.pop(0)
	print word
# Define a function called print_last_word which takes a list
# of words, removes the last word from the list, and stores it
# in a variable which gets printed to the terminal. This modifies
# the original list by removing the last word from it.
def print_last_word(words):
	"""Prints the last word after popping it off."""
	word = words.pop(-1)
	print word
# Define a function called sort_sentence which takes a string
# and returns a list of sorted words. This function calls the
# previous two functions, break_words and sort_words, to accomplish
# this. sort_sentence returns the list of sorted words.
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
# Define a function called print_first_and_last which takes a string
# and prints the first and last words in the string to the terminal.
# This function calls the previous three functions, break_words,
# print_first_word, and print_last_word, to accomplish this.
def print_first_and_last(sentence):
	"""Prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
# Define a function called print_first_and_last_sorted which takes
# a string, sorts the words in the string in alphabetical order,
# and then prints the first and last sorted words to the terminal.
# This function calls the previous three functions, sort_sentence,
# print_first_word, and print_last_word, to accomplish this.
def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)