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
	words = a_string.lower().split()
	result = []
	for word in words:
		match = False
		i = 0
		while not match:
			if word in the_lexicon[i]:
				result.append(the_lexicon[i])
				match = True
			elif i >= (len(the_lexicon) - 1):
				try:
					num = int(word)
					result.append(('number', num))
				except ValueError:
					result.append(('error', word))
				match = True
			else:
				i += 1
	return result