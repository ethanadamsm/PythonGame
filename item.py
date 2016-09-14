import sys, pygame

class Item():
	def __init__(self, x, y, image):
		self.x = x
		self.y = y
		self.image = image

	def render(self, screen):
		screen.blit(self.image, (int(self.x), int(self.y)))

	def getImage(self):
		return self.image

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getImage(self):
		return self.image