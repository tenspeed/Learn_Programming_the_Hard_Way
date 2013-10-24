import os, sys
import pygame
from pygame.locals import *

pygame.init()

class GameSprite(pygame.sprite.Sprite):

	def __init__(self, an_image, speed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join('data', an_image)).convert_alpha()
		self.speed = speed
		self.rect = self.image.get_rect()

# initialize the game window size
screen_width = 1366
screen_height = 768
# set the player movement speed
player_speed = 2
# create the game window
screen = pygame.display.set_mode((screen_width, screen_height))
# load the background image
background_surf = pygame.image.load(os.path.join('data', 'background.png')).convert_alpha()
# blit the background image to the game window
screen.blit(background_surf, (0, 0))


# create a group for the player sprite
player_sprites = pygame.sprite.Group()
# create the player sprite
player = GameSprite('player.png', player_speed)
# add the player sprite to the player group
player_sprites.add(player)

# main program loop
while True:

	# exit gracefully if game window is closed
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	# handle keyboard input
	keys = pygame.key.get_pressed()
	if keys[K_w]:
		player.rect = player.rect.move(0, -player.speed)
	if keys[K_s]:
		player.rect = player.rect.move(0, player.speed)
	if keys[K_a]:
		player.rect = player.rect.move(-player.speed, 0)
	if keys[K_d]:
		player.rect = player.rect.move(player.speed, 0)
	
	player_sprites.clear(screen, background_surf)
	player_sprites.draw(screen)
	pygame.display.update()