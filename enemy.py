import sys, pygame, healthbar

class Enemy(object):
	def __init__(self, x, y, w, h, vx, vy, image):
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.vx = vx
			self.vy = vy
			self.image = image
			self.healthbar = healthbar.Healthbar(self.x - 10, self.y - 30, 100)
			self.visible = True

	def render(self, screen):
		if self.visible:
			screen.blit(self.image, (self.x, self.y))
			self.healthbar.render(screen)

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

	def getW(self):
		return self.w

	def getH(self):
		return self.h

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def bindHealth(self):
		self.healthbar.setX(self.x - 10)
		self.healthbar.setY(self.y - 30)

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

		if self.healthbar.getHealth() <= 0:
			self.visible = False

		self.x += self.vx
		self.y += self.vy

		self.bindHealth()
		
	def getBox(self):
		return [self.x, self.y, self.w, self.h]

	def setHealth(self, health):
		self.healthbar.setHealth(health)

	def getHealth(self):
		return self.healthbar.getHealth()