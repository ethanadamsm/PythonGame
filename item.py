import sys, pygame

class Item():
	def __init__(self, x, y, image):
		self.x = x
		self.y = y
		self.vx = 0
		self.vy = 0
		self.a = False
		self.d = False
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

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def getVelX(self):
		return self.vx

	def getVelY(self):
		return self.vy

	def setVelX(self, vx):
		self.vx = vx

	def setVelY(self, vy):
		self.vy = vy

	def update(self, d, a):
		if d:
			self.x -= 1
		elif a:
			self.x += 1