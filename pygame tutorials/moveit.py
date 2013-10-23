import pygame
from pygame.locals import *

pygame.init()

class GameObject(object):

	def __init__(self, image, height, speed):
		self.speed = speed
		self.image = image
		self.height = height
		self.pos = image.get_rect().move(0, self.height)

	def move(self):
		self.pos = self.pos.move(self.speed, 0)
		if self.pos.right > 640:
			self.pos.left = 0
			self.pos.top += 60
		if self.pos.bottom > 480:
			self.pos.top = 0

screen = pygame.display.set_mode((640, 480))
player = pygame.image.load('player.bmp').convert()
background = pygame.image.load('background.bmp').convert()
screen.blit(background, (0, 0))
objects = []

o = GameObject(player, 0, 4)
	
while 1:
	for event in pygame.event.get():

		if event.type in (QUIT, KEYDOWN):
			sys.exit()

		# erase last player sprite
		screen.blit(background, o.pos, o.pos)
		# update the player position coordinates
		o.move()
		# blit new player to screen in different location
		screen.blit(player, o.pos)
		# show it all on the screen
		pygame.display.update()
		pygame.time.delay(2)