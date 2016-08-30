import sys, pygame

class Player(object):
	def __init__(self, x, y, w, h, vx, vy, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = vx
		self.vy = vy
		self.image = image

	def render(self, screen):
		screen.blit(image, x, y)
