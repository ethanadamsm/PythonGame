import sys, pygame

class Inventory(object):
	def __init__(self):
		self.itemList = []

	def addItem(self, item):
		self.itemList.append(item)

	def render(self, screen):
		for item in self.itemList:
			item.render(screen)

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
