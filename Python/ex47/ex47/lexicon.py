the_lexicon = [('direction', 'north'),
			   ('direction', 'south'),
			   ('direction', 'east'),
			   ('direction', 'west'),
			   ('noun', 'bear'),
			   ('noun', 'princess'),
			   ('verb', 'go'),
			   ('verb', 'kill'),
			   ('verb', 'eat'),
			   ('stop', 'the'),
			   ('stop', 'in'),
			   ('stop', 'of')]

def scan(a_string):
	words = a_string.split()
	result = []
	for word in words:
		for i in range(len(the_lexicon)):
			if word in the_lexicon[i]:
				result.append(the_lexicon[i])
			else:
				pass
	return result