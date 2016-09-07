import sys, pygame

class Healthbar():
	def __init__(self, x, y, health):
		self.x = x
		self.y = y
		self.w = 75
		self.h = 25
		self.totalhealth = health
		self.health = health
		self.image = pygame.image.load("healthbar.png")

	def render(self, screen):
		if self.health < 0:
			self.health = 0
		self.image = pygame.transform.scale(self.image, (75 * (self.health / self.totalhealth), 25))
		screen.blit(self.image, (self.x, self.y))

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def setHealth(self, health):
		self.health = health

	def getHealth(self):
		return self.health