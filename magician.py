import sys, pygame, healthbar, item, inventory

class Magician():
	def __init__(self, x, y, w, h, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = 0
		self.vy = 0
		self.image = image
		self.healthbar = healthbar.Healthbar(self.x - 10, self.y - 30, 100)
		self.visible = True
		self.alive = True
		self.frame = 0
		self.droppedItem = ""
		self.typpe = "magician"
		self.inventory = inventory.Inventory()
		self.inventory.addItem(bow.Bow(300, 230, 20, 50, "bow.png"))

	def render(self, screen):
		if self.visible:
			screen.blit(self.image, (self.x, self.y))
			self.healthbar.render(screen)
			self.inventory.render(screen)

	def setVelX(self, vx):
		self.vx = vx

	def setVelY(self, vy):
		self.vy = vy

	def getVelX(self):
		return self.vx

	def getVelY(self):
		return self.vy

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
			self.x -= 2
		elif a:
			self.x += 2
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
			self.alive = False
			self.droppedItem = item.Item(self.x + 25, self.y + 75, 20, 20, pygame.image.load("coin.png"))

		self.x += self.vx
		self.y += self.vy

		self.bindHealth()
		self.healthbar.update()

	def getBox(self):
		return [self.x, self.y, self.w, self.h]

	def setHealth(self, health):
		self.healthbar.setHealth(health)

	def getHealth(self):
		return self.healthbar.getHealth()

	def getAlive(self):
		return self.alive

	def getDroppedItem(self):
		return self.droppedItem

	def setDroppedItem(self, droppedItem):
		self.droppedItem = droppedItem

	def getFrame(self):
		return self.frame

	def getTypeE(self):
		return self.typpe
