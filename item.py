import sys, pygame

class Item():
	def __init__(self, x, y, w, h, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = 0
		self.vy = 0
		self.a = False
		self.d = False
		self.visible = True
		self.image = image

	def render(self, screen):
		if self.visible:
			screen.blit(self.image, (int(self.x), int(self.y)))

	def getImage(self):
		return self.image

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getImage(self):
		return self.image

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

	def getW(self):
		return self.w

	def getH(self):
		return self.h

	def setVisible(self, visible):
		self.visible = visible

	def getVisible(self):
		return self.visible