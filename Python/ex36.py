from sys import exit

print "Oh my glob! You're LSP!"

def hunky_guy_room():
	print """
	You have just entered the hunky guy room <3_<3!
	This room contains all the HAWT dudes in Ooo!
	In the left corner, you see Finn.
	In the right corner, you see Flame Prince.
	Are you feeling steamy? or adventurous?
	"""

	action = raw_input("> ")

	if "steamy" in action:
		print """
		You see Flame Prince and think to yourself,
		\"I'm lumping steamy! I'm gonna get a piece
		of that HAWT bod!\" You float over, thinking about how jealous
		Mellissa will be after you make out with
		Flame Prince. You think to yourself,
		\"is it getting hot in he..\" OH MY GLOB
		YOU'RE ON FIRE!!!

		You're dead.
		"""
		exit(0)
	elif "adventurous" in action:
		print """
		You see Finn and think he looks worried.
		Because you're SUCH a good friend, you go
		talk to him and see what's wrong.

		You: Hey Finn, what's wrong with your face today?

		Finn: Hey LSP, I'm just worried about BMO. I can't
		find him anywhere.

		You: I'll help you look for him Finn, because I'm
		such a good friend like that!
		"""
		exit(0)
	else:
		print "WHAT THE LUMP, YOU CAN'T DO THAT!"
		exit(0)
def dead(why):
	print why
	exit(0)

def start():
	while True:
		hunky_guy_room()

start()