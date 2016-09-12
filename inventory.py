import sys, pygame

class Inventory(object):
	def __init__(self):
		self.itemList = []
		self.image = pygame.image.load("inventory.png")
		self.font = pygame.font.SysFont("comicsansms", 30)

	def addItem(self, item):
		self.itemList.append(item)

	def render(self, screen):
		for item in self.itemList:
			item.render(screen)
		screen.blit(self.image, (10, 420))
		x = 20
		y = 430
		num = 1
		for item in self.itemList:
			scalex = 50 / item.getW()
			scaley = 50 / item.getH()
			screen.blit
			cur = pygame.transform.scale(item.getImage(), (scalex, scaley))
			screen.blit(item.getImage(), (x, y))
			text = self.font.render(str(num), True, (0, 0, 0))
			screen.blit(text, (x, 380))
			x += 50
			num += 1

	def update(self):
		for item in self.itemList:
			item.update()

	def moveItem(self, vx, vy):
		self.itemList[0].setVelX(vx)
		self.itemList[0].setVelY(vy)

	def setItem(self, x, y):
		self.itemList[0].setX(x)
		self.itemList[0].setY(y)

	def rotateItem(self, angle):
		self.itemList[0].rotateItem(angle)

	def getX(self):
		return self.itemList[0].getX()

	def getY(self):
		return self.itemList[0].getY()

	def getW(self):
		return self.itemList[0].getW()

	def getH(self):
		return self.itemList[0].getH()

	def getItem(self, index):
		return self.itemList[index]