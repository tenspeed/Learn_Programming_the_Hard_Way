import os, sys
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
#pygame.key.set_repeat(10, 10)

#while 1:
#	for event in pygame.event.get():
#		if event.type == KEYDOWN:
#			if event.key == K_w:
#				print "up"
#			elif event.key == K_s:
#				print "down"
#			elif event.key == K_a:
#				print "left"
#			elif event.key == K_d:
#				print "right"
#			else:
#				pass
#		else:
#			pass

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

	pressed = pygame.key.get_pressed()

	if pressed[K_w]:
		print "up"
	if pressed[K_s]:
		print "down"
	if pressed[K_a]:
		print "left"
	if pressed[K_d]:
		print "right"