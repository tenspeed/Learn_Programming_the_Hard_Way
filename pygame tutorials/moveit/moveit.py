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

# create a group for all the sprites in the game
all_sprites = pygame.sprite.Group()
# create a group for the player sprite
player_sprites = pygame.sprite.Group()
# create the player sprite
player = GameSprite('player.png', player_speed)
# add the player sprite to the all_sprites group
all_sprites.add(player)
# add the player sprite to the player_sprites group
player_sprites.add(player)

# create a group for the blocks
block_sprites = pygame.sprite.Group()
# create two block sprites and add them to the all_sprites and block_sprites groups
for i in range(2):
	block = GameSprite('block.png', 0)
	# set the block's location on the screen
	block.rect.x = (i + 1) * 200
	block.rect.y = (i + 1) * 200

	all_sprites.add(block)
	block_sprites.add(block)

collison = []
# main program loop
while True:

	# exit gracefully if game window is closed
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	# handle keyboard input
	keys = pygame.key.get_pressed()
	# if 'w' is pressed and we're not colliding above, move up
	if keys[K_w]:
		# update player rectange with new coordinates
		player.rect = player.rect.move(0, -player.speed)
		# check for a collision, if so undo the previous move
		if pygame.sprite.spritecollide(player, block_sprites, False):
			player.rect = player.rect.move(0, player.speed)
	# if 's' is pressed and we're not colliding below, move down
	if keys[K_s]:
		player.rect = player.rect.move(0, player.speed)
		if pygame.sprite.spritecollide(player, block_sprites, False):
			player.rect = player.rect.move(0, -player.speed)
	# if 'a' is pressed and we're not colliding to the left, move left
	if keys[K_a]:
		player.rect = player.rect.move(-player.speed, 0)
		if pygame.sprite.spritecollide(player, block_sprites, False):
			player.rect = player.rect.move(player.speed, 0)
	# if 'd' is pressed and we're not colliding to the right, move right
	if keys[K_d]:
		player.rect = player.rect.move(player.speed, 0)
		if pygame.sprite.spritecollide(player, block_sprites, False):
			player.rect = player.rect.move(-player.speed, 0)
		
	# check if player is off screen, if so, loop around
	if player.rect.x > screen_width:
		player.rect.x = 0
	if player.rect.x < 0:
		player.rect.x = screen_width
	if player.rect.y > screen_height:
		player.rect.y = 0
	if player.rect.y < 0:
		player.rect.y = screen_height
	
	player_sprites.clear(screen, background_surf)
	block_sprites.draw(screen)
	player_sprites.draw(screen)
	pygame.display.update()