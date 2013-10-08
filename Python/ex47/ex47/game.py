class Room(object):

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}
		self.items = {}
		self.people = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def talk(self, person):
		return self.people.get(person, None)

	def take(self, item_key):
		return self.items.pop(item_key)

	def add_paths(self, paths):
		self.paths.update(paths)

	def add_items(self, items):
		self.items.update(items)

	def add_people(self, people):
		self.people.update(people)