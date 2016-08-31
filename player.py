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
		print(self.x)
		screen.blit(self.image, (self.x, self.y))

	def setVelX(self, vx):
		self.vx = vx

	def setVelY(self, vy):
		self.vy = vy

	def getVelX(self):
		return self.vx

	def getVelY(self):
		return self.yv

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def update(self):
		self.x += self.vx
		self.y += self.vy
		if self.x >= 295:
			self.x = 295
		if self.x <= 0:
			self.x = 0
		if self.y <= 50:
			self.y = 50
		if self.y >= 380:
			self.y = 380
