import sys, pygame, inventory, healthbar

class Player(object):
	def __init__(self, x, y, w, h, vx, vy, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = vx
		self.vy = vy
		self.image = image
		self.inven = inventory.Inventory()
		self.healthbar = healthbar.Healthbar(self.x - 10, self.y - 30, 100)
		self.down = False

	def render(self, screen):
		screen.blit(self.image, (self.x, self.y))
		self.healthbar.render(screen)
		self.inven.render(screen)

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

	def bindHealth(self):
		self.healthbar.setX(self.x - 10)
		self.healthbar.setY(self.y - 30)

	def bindItem(self):
		if self.down == False:
			self.inven.setItem(self.x + 20, self.y - 70)
		else:
			self.inven.setItem(self.x + 20, self.y + 40)

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
		self.inven.update()
		self.bindItem()
		self.bindHealth()

	def addItem(self, item):
		self.inven.addItem(item)

	def moveItem(self, vx, vy):
		self.inven.moveItem(vx, vy)

	def setItem(self, x, y):
		self.inven.setItem(x, y)

	def rotateItem(self, angle):
		self.down = not self.down
		print(self.down)
		self.inven.rotateItem(angle)


