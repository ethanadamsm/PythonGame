import sys, pygame

class Sword:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = 0
		self.vy = 0
		self.image = pygame.image.load("sword.png")
		self.image = pygame.transform.rotate(self.image, 90)

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def update(self):
		self.x += self.vx
		self.y += self.vy

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getW(self):
		return self.w

	def getH(self):
		return self.h

	def getVelX(self):
		return self.vx

	def getVelY(self):
		return self.vy

	def setVelX(self, vx):
		self.vx = vx

	def setVelY(self, vy):
		self.vy = vy

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def rotateItem(self, angle):
		self.image = pygame.transform.rotate(self.image, angle)


