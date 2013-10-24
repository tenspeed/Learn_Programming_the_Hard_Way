import os, sys
import pygame
from pygame.locals import *

pygame.init()

class GameObject(object):

	def __init__(self, a_surface, height, speed):
		self.speed = speed
		self.a_surface = a_surface
		self.height = height
		self.pos = a_surface.get_rect().move(0, self.height)
		
def load_image(new_image):
	new_surface = pygame.image.load(os.path.join('data', new_image)).convert_alpha()
	return new_surface

dirty_rects = []
screen_width = 1366
screen_height = 768
player_speed = 1
screen = pygame.display.set_mode((screen_width, screen_height))
player_surf = load_image('player.png')
background_surf = load_image('background.png')
screen.blit(background_surf, (0, 0))
player = GameObject(player_surf, 0, player_speed)
	
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	screen.blit(background_surf, player.pos, player.pos)
	keys = pygame.key.get_pressed()
	if keys[K_a]:
		player.pos = player.pos.move(-player.speed, 0)
	if keys[K_d]:
		player.pos = player.pos.move(player.speed, 0)
	if keys[K_w]:
		player.pos = player.pos.move(0, -player.speed)
	if keys[K_s]:
		player.pos = player.pos.move(0, player.speed)
	
	# erase last player sprite
	# blit new player to screen in different location
	screen.blit(player_surf, player.pos)
	# show it all on the screen
	pygame.display.update()