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
			print("updating item")
			item.update()

	def moveItem(self, vx, vy):
		print("moving")
		self.itemList[0].setVelX(vx)
		self.itemList[0].setVelY(vy)
