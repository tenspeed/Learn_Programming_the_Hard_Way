import os, sys
import pygame
from pygame.locals import *

pygame.init()
class GameSprite(pygame.sprite.Sprite):

	def __init__(self, an_image):
		pygame.sprite.Sprite.__init__(self)
		if an_image == None:
			self.image = pygame.Surface([1366, 100])
			self.image.fill((255, 0, 0))
			self.rect = self.image.get_rect()
		else:
			self.image = pygame.image.load(os.path.join('data', an_image)).convert_alpha()
			self.rect = self.image.get_rect()
			self.vx, self.vx_old, self.vy, self.vy_old = 0, 0, 1, 1

# initialize the game window size
screen_width = 1366
screen_height = 768

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
player = GameSprite('player.png')
# add the player sprite to the all_sprites group
all_sprites.add(player)
# add the player sprite to the player_sprites group
player_sprites.add(player)
# create a group for the ground sprite
ground_sprites = pygame.sprite.Group()
# create a sprite for the ground
ground = GameSprite(None)
# set it's location to the bottom of the screen
ground.rect.y = 668
all_sprites.add(ground)
ground_sprites.add(ground)

# create a group for the blocks
block_sprites = pygame.sprite.Group()
# create two block sprites and add them to the all_sprites and block_sprites groups
for i in range(1):
	block = GameSprite('block.png')
	# set the block's location on the screen
	block.rect.x = (screen_width - 300)
	block.rect.y = (screen_height - 200)

	all_sprites.add(block)
	block_sprites.add(block)

collison = []
v_max = 25
player_sprites.draw(screen)


a_x = 0
brake = True
# main program loop
while True:

	# exit gracefully if game window is closed
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	# physics time
	player.vy += 1
	if player.vy >= v_max:
		player.vy = v_max
	player.rect = player.rect.move(0, player.vy)
	if pygame.sprite.spritecollide(player, ground_sprites, False):
		player.rect = player.rect.move(0, -player.vy)
		player.vy = 1
	if pygame.sprite.spritecollide(player, block_sprites, False):
		player.rect = player.rect.move(0, -player.vy)
		player.vy = 1

	
	# handle keyboard input
	keys = pygame.key.get_pressed()
	# if 'a' is pressed move left
	if keys[K_a]:
		a_x = -2
		brake = False
	# if 'd' is pressed move right
	if keys[K_d]:
		a_x = 2
		brake = False

	# calculate player movement
	player.vx = player.vx_old + a_x
	if player.vx > 0:
		if player.vx > v_max:
			player.vx = v_max
	elif player.vx < 0:
		if player.vx < -v_max:
			player.vx = -v_max
	# update player rectange with new coordinates
	player.rect = player.rect.move(player.vx, 0)
	# check for a collision, if so undo the previous move
	if pygame.sprite.spritecollide(player, block_sprites, False):
		player.rect = player.rect.move(-player.vx, 0)
		player.vx, player.vx_old = 0, 0
	# check if player has gone off left side of screen, if so, put him back
	elif player.rect.x <= 0:
			player.rect.x = 0
			player.rect.y = (screen_height - 160)
			player.vx, player.vx_old = 0, 0
	# check if player has gone off right side of screen, if so, put him back
	elif player.rect.x >= (screen_width - 60):
			player.rect.x = (screen_width - 60)
			player.rect.y = (screen_height - 160)
			player.vx, player.vx_old = 0, 0
	# if no collisions, carry on
	else:
		player.vx_old = player.vx

	if event.type == pygame.KEYUP:
		brake = True

	# we want our natural state to be at rest
	if brake:
		if player.vx > 0:
			a_x = -3
			player.vx = player.vx_old + a_x
			player.rect = player.rect.move(player.vx, 0)
			# check for a collision, if so undo the previous move
			if pygame.sprite.spritecollide(player, block_sprites, False):
				player.rect = player.rect.move(-player.vx, 0)
				player.vx, player.vx_old = 0, 0
			# check if player has gone off left side of screen, if so, put him back
			elif player.rect.x <= 0:
				player.rect.x = 0
				player.rect.y = (screen_height - 160)
				player.vx, player.vx_old = 0, 0
			# check if player has gone off right side of screen, if so, put him back
			elif player.rect.x >= (screen_width - 60):
				player.rect.x = (screen_width - 60)
				player.rect.y = (screen_height - 160)
				player.vx, player.vx_old = 0, 0
			# if no collisions, carry on
			else:
				player.vx_old = player.vx
			if player.vx <= 0:
				player.vx, player.vx_old = 0, 0
				brake = False

		if player.vx < 0:
			a_x = 3
			player.vx = player.vx_old + a_x
			player.rect = player.rect.move(player.vx, 0)
			# check for a collision, if so undo the previous move
			if pygame.sprite.spritecollide(player, block_sprites, False):
				player.rect = player.rect.move(-player.vx, 0)
				player.vx, player.vx_old = 0, 0
			# check if player has gone off left side of screen, if so, put him back
			elif player.rect.x <= 0:
				player.rect.x = 0
				player.rect.y = (screen_height - 160)
				player.vx, player.vx_old = 0, 0
			# check if player has gone off right side of screen, if so, put him back
			elif player.rect.x >= (screen_width - 60):
				player.rect.x = (screen_width - 60)
				player.rect.y = (screen_height - 160)
				player.vx, player.vx_old = 0, 0
			# if no collisions, carry on
			else:
				player.vx_old = player.vx
			if player.vx >= 0:
				player.vx, player.vx_old = 0, 0
				brake = False

	a_x = 0

	print "x = %d" % player.rect.x
	player_sprites.clear(screen, background_surf)
	all_sprites.draw(screen)
	player_sprites.draw(screen)
	pygame.display.update()
	pygame.time.delay(30)