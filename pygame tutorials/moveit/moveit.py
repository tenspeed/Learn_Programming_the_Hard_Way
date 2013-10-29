import os, sys
import pygame
from pygame.locals import *

pygame.init()
class GameSprite(pygame.sprite.Sprite):

	def __init__(self, an_image, v_max = None):
		pygame.sprite.Sprite.__init__(self)
		if an_image == None:
			self.image = pygame.Surface([1366, 100])
			self.image.fill((255, 0, 0))
			self.rect = self.image.get_rect()
		else:
			self.image = pygame.image.load(os.path.join('data', an_image)).convert_alpha()
			self.rect = self.image.get_rect()
			self.vx, self.vx_old, self.vy, self.vy_old = 0, 0, 0, 0
			self.v_max = v_max

	def move_x(self, a_x):
		# calculate sprite movement in the x-direction
		self.vx = self.vx_old + a_x
		# check if sprite is moving faster than v_max, if so, set speed equal to v_max
		# this requires checking which direction we're moving first by looking to
		# see if self.vx is positive (moving right) or negative (moving left).
		if self.vx > 0:
			if self.vx > self.v_max:
				self.vx = self.v_max
		elif self.vx < 0:
			if self.vx < -self.v_max:
				self.vx = -self.v_max
		# update sprite rectange with new x-coordinates
		self.rect = self.rect.move(self.vx, 0)
		self.vx_old = self.vx

	def move_y(self, a_y):
		# calculate sprite movement in the y-direction
		self.vy = self.vy_old + a_y
		# check if we're moving faster than v_max again.
		if self.vy > 0:
			if self.vy > self.v_max:
				self.vy = self.v_max
		elif self.vy < 0:
			if self.vy < -self.v_max:
				self.vy = -self.v_max
		# update the player rectange with the new y-coordinates
		self.rect = self.rect.move(0, self.vy)
		self.vy_old = self.vy
		

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
player = GameSprite('player.png', 25)
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
#player_sprites.draw(screen)
block_sprites.draw(screen)
ground_sprites.draw(screen)
#all_sprites.draw(screen)

a_x = 0
a_y = 1
brake = True
jump = False
counter = 0
# main program loop
while True:
	# exit gracefully if game window is closed
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	# handle keyboard input
	keys = pygame.key.get_pressed()
	# if 'a' is pressed move left
	if keys[K_a] and not jump:
		a_x = -2
		brake = False
	# if 'd' is pressed move right
	if keys[K_d] and not jump:
		a_x = 2
		brake = False
	# if SPACEBAR is pressed, jump
	if keys[K_SPACE]:
		# check if already jumping to prevent double-jump
		if jump:
			pass
		else:
			a_y = -3
			jump = True

	# small non-blocking loop to calculate jump time
	if jump:
		counter += 1
		if counter > 5:
			counter = 0
			a_y = 1

	# check to see if the player has stopped pressing 'a' or 'd'
	# if so, initiate braking, unless the key pressed was the spacebar
	if event.type == pygame.KEYUP:
		if (event.key == pygame.K_a or pygame.K_d) and not jump:
			brake = True

	# we want our natural state to be at rest
	
			#player.vx = player.vx_old + a_x
			#player.rect = player.rect.move(player.vx, 0)
			# check for a collision, if so undo the previous move
			#if pygame.sprite.spritecollide(player, block_sprites, False):
			#	player.rect = player.rect.move(-player.vx, 0)
			#	player.vx, player.vx_old = 0, 0
			# check if player has gone off left side of screen, if so, put him back
			#elif player.rect.x <= 0:
			#	player.rect.x = 0
			#	player.rect.y = (screen_height - 160)
			#	player.vx, player.vx_old = 0, 0
			# check if player has gone off right side of screen, if so, put him back
			#elif player.rect.x >= (screen_width - 60):
			#	player.rect.x = (screen_width - 60)
			#	player.rect.y = (screen_height - 160)
			#	player.vx, player.vx_old = 0, 0
			# if no collisions, carry on
			#else:
			#	player.vx_old = player.vx
	if brake:
		if player.vx > 0:
			a_x = -3
		if player.vx < 0:
			a_x = 3			
	player.move_x(a_x)
	# check for a collision with the blocks, if so undo the previous move
	if pygame.sprite.spritecollide(player, block_sprites, False):
		player.rect = player.rect.move(-player.vx, 0)
		player.vx, player.vx_old = 0, 0
	# check if sprite has gone off left side of screen, if so, put it back
	if player.rect.x <= 0:
		player.rect = player.rect.move(-player.vx, 0)
		player.vx, player.vx_old = 0, 0
	# check if sprite has gone off right side of screen, if so, put it back
	if player.rect.x >= (screen_width - 60):
		player.rect = player.rect.move(-player.vx, 0)
		player.vx, player.vx_old = (0, 0)
	if a_x == -3:
		if player.vx <= 0:
			player.vx, player.vx_old = 0, 0
			brake = False
			a_x = 0
	if a_x == 3:
		if player.vx >= 0:
			player.vx, player.vx_old = 0, 0
			brake = False
			a_x = 0

	player.move_y(a_y)
	# check for a collision with the ground, if so, undo the previous move
	if pygame.sprite.spritecollide(player, ground_sprites, False):
		player.rect = player.rect.move(0, -player.vy)
		player.vy, player.vy_old = 0, 0
		jump = False
		counter = 0
	# check for a collision with the blocks, if so, undo the previous move
	if pygame.sprite.spritecollide(player, block_sprites, False):
		player.rect = player.rect.move(0, -player.vy)
		player.vy, player.vy_old = 0, 0
		jump = False
		counter = 0

	player_sprites.clear(screen, background_surf)
	player_sprites.draw(screen)
	pygame.display.update()
	pygame.time.delay(30)