import sys, pygame

class Enemy(object):
	def __init__(self, x, y, w, h, vx, vy, image):
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.vx = vx
			self.vy = vy
			self.image = image

	def render(self, screen):
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

	def update(self, px, py, d, a):
		if d:
			self.x -= 1 
		elif a:
			self.x += 1
		else:
			if px < self.x:
				self.vx = -.1
			if px > self.x:
				self.vx = .1
			if py < self.y:
				self.vy = -.1
			if py > self.y:
				self.vy = .1

		self.x += self.vx
		self.y += self.vy
		