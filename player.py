import sys, pygame, inventory, healthbar

class Player(object):

	def getAnimationImages(self, prefix, suffix, n):
		images = []
		for x in range (1, n):
			current = str(x)
			images.append(pygame.image.load(prefix + current + suffix))
		return images

	def __init__(self, x, y, w, h, vx, vy, image):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = vx
		self.vy = vy
		self.current = 0
		self.frame = 0
		self.image = image
		self.attackleft = False
		self.left = False
		self.right = False
		self.inven = inventory.Inventory()
		self.healthbar = healthbar.Healthbar(self.x - 10, self.y - 30, 100)
		self.down = False
		self.leftAttackAnimation = self.getAnimationImages("playerrec/leftattack", ".png", 6)
		self.leftAnimation = self.getAnimationImages("playerrec/left", ".png", 5)
		self.rightAnimation = self.getAnimationImages("playerrec/right", ".png", 5)

	def render(self, screen):
		if(self.attackleft):
			screen.blit(self.leftAttackAnimation[self.current], (self.x, self.y))
		elif(self.left):
			screen.blit(self.leftAnimation[self.current], (self.x, self.y))
		elif(self.right):
			screen.blit(self.rightAnimation[self.current], (self.x, self.y))
		else:
			screen.blit(self.image, (self.x, self.y))
		self.healthbar.render(screen)
		self.inven.render(screen)
		self.frame += 1

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
			self.inven.setItem(self.x + 2, self.y + 19)
		else:
			self.inven.setItem(self.x + 35, self.y + 45)

	def setHealth(self, health):
		self.healthbar.setHealth(health)

	def getHealth(self):
		return self.healthbar.getHealth()

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
		if(self.attackleft):
			if(self.frame % 15 == 0.0):
				self.current += 1 
				if(self.current >= len(self.leftAttackAnimation)):
					self.current = 0
					self.attackleft = False
		elif(self.left):
			if(self.frame % 20 == 0.0):
				self.current += 1
				if(self.current >= len(self.leftAnimation)):
					self.current = 0
		elif(self.right):
			if(self.frame % 20 == 0.0):
				self.current += 1
				if(self.current >= len(self.leftAnimation)):
					self.current = 0

	def addItem(self, item):
		self.inven.addItem(item)

	def moveItem(self, vx, vy):
		self.inven.moveItem(vx, vy)

	def setItem(self, x, y):
		self.inven.setItem(x, y)

	def rotateItem(self, angle):
		self.down = not self.down
		self.inven.rotateItem(angle)

	def getItemBox(self):
		box = [self.inven.getX(), self.inven.getY(), self.inven.getW(), self.inven.getH()]
		return box

	def getItemX(self):
		return self.inven.getX()

	def getItemY(self):
		return self.inven.getY()

	def getItemW(self):
		return self.inven.getW()

	def getItemH(self):
		return self.inven.getH()

	def setAttackLeft(self, attackleft):
		self.attackleft = attackleft

	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right

	def getItem(self, index):
		return self.inven.getItem(index)