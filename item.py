import sys, pygame

class Item():
	def __init__(self, x, y, image):
		self.x = x
		self.y = y
		self.image = image

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))