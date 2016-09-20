import sys, pygame, box

class Gui:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.visible = True
		self.boxes = []
		self.image = pygame.image.load("gui.png")

	def render(self, screen):
		if self.visible:
			screen.blit(self.image, (self.x, self.y))
			self.image = pygame.transform.scale(self.image, (self.w, self.h))
			for box in self.boxes:
				box.render(screen)

	def setVisible(self, visible):
		self.visible = visible

	def addBox(self, x, y, w, h):
		self.boxes.append(box.Box(x, y, w, h))

	def addImage(self, index, image):
		self.boxes[index].addImage(image)