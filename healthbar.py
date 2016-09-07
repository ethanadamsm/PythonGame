import sys, pygame

class Healthbar():
	def __init__(self, x, y, health):
		self.x = x
		self.y = y
		self.health = health
		self.image = pygame.image.load("healthbar.png")

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y