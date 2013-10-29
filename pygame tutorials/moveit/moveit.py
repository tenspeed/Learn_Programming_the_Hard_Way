import os, sys
import pygame
from pygame.locals import *

pygame.init()
class GameSprite(pygame.sprite.Sprite):

	def __init__(self, an_image):
		pygame.sprite.Sprite.__init__(self)
		if an_image == None:
			self.image = pygame.Surface([1366, 100])
			self.image.fill((0, 100, 0))
			self.rect = self.image.get_rect()
		else:
			self.image = pygame.image.load(os.path.join('data', an_image)).convert_alpha()
			self.rect = self.image.get_rect()
			self.vx, self.vy = 0, 0

		
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
# create a block sprite and add it to the all_sprites and block_sprites groups
platform = GameSprite('platform.png')
all_sprites.add(platform)
block_sprites.add(platform)
platform.rect.x = 750
platform.rect.y = 600

#player_sprites.draw(screen)
block_sprites.draw(screen)
ground_sprites.draw(screen)
#all_sprites.draw(screen)

brake = False
jump = False
counter = 0
v_max = 30
braking_force = 0
# main program loop
while True:
	# exit gracefully if game window is closed
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	# gravity
	if player.vy > v_max:
		player.vy = v_max
	else:
		player.vy += 2

	# handle keyboard input
	keys = pygame.key.get_pressed()
	# if 'a' is pressed move left
	if keys[K_a] and not jump:
		if player.vx < -v_max:
			player.vx = -v_max
		else:
			player.vx += -2
		brake = False
	# if 'd' is pressed move right
	if keys[K_d] and not jump:
		if player.vx > v_max:
			player.vx = v_max
		else:
			player.vx += 2
		brake = False
	# if SPACEBAR is pressed, jump
	if keys[K_SPACE]:
		# check if already jumping to prevent double-jump
		if jump:
			pass
		else:
			jump = True
			player.vy = 0

	# small non-blocking loop to calculate jump time
	if jump:
		counter += 1
		player.vy += -7
		if counter >= 5:
			player.vy += 7

	# check to see if the player has stopped pressing 'a' or 'd'
	# if so, initiate braking, unless the key pressed was the spacebar
	if event.type == pygame.KEYUP:
		if (event.key == pygame.K_a or pygame.K_d) and not jump:
			braking_force = 3
			brake = True

	if brake:
		if player.vx > 0:
			player.vx += -braking_force
			if player.vx < 0:
				player.vx = 0
				brake = False
		elif player.vx < 0:
			player.vx += braking_force
			if player.vx > 0:
				player.vx = 0
				brake = False

	# move sprite in x direction
	player.rect = player.rect.move(player.vx, 0)
	# check for a collision with the blocks, if so undo the previous move
	if pygame.sprite.spritecollide(player, block_sprites, False):
		player.rect = player.rect.move(-player.vx, 0)
		brake = True
	# check if sprite has gone off left side of screen, if so, put it back
	if player.rect.x <= 0:
		player.rect = player.rect.move(-player.vx, 0)
		player.vx = 0
	# check if sprite has gone off right side of screen, if so, put it back
	if player.rect.x >= (screen_width - 60):
		player.rect = player.rect.move(-player.vx, 0)
		player.vx = 0

	# move sprite in y directon
	player.rect = player.rect.move(0, player.vy)
	# check for a collision with the ground, if so, undo the previous move
	if pygame.sprite.spritecollide(player, ground_sprites, False):
		player.rect = player.rect.move(0, -player.vy)
		player.vy = 0
		jump = False
		counter = 0
		brake = True
		braking_force = 200
	# check for a collision with the blocks, if so, undo the previous move
	if pygame.sprite.spritecollide(player, block_sprites, False):
		player.rect = player.rect.move(0, -player.vy)
		player.vy = 0
		jump = False
		counter = 0
		brake = True
		braking_force = 200

	player_sprites.clear(screen, background_surf)
	player_sprites.draw(screen)
	pygame.display.update()
	pygame.time.delay(30)