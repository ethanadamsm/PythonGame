import sys, pygame

class Button:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.visible = False
		self.font = pygame.font.SysFont("comicsansms", 30)
		self.image = ""
		self.text = 0

	def render(self, screen):
		if self.visible and self.image != "":
			screen.blit(self.image, (self.x, self.y))
		if self.text != 0:
			text = self.font.render(self.text, True, (0, 0, 0))
			screen.blit(text, (((self.w / 2) + self.x) - (self.font.size(self.text)[0] / 2), ((self.h / 2) + self.y) - (self.font.size(self.text)[1] / 2)))

	def addImage(self, image):
		self.image = image
		self.image = pygame.transform.scale(self.image, (self.w, self.h))
		self.visible = True

	def setFontSize(self, size):
		self.font = pygame.font.SysFont("comicsansms", size)

	def setText(self, text):
		self.text = text

	def getText(self):
		return self.text

	def setVisible(self, visible):
		self.visible = visible

	def checkCollision(self):
		x = pygame.mouse.get_pos()[0]
		y = pygame.mouse.get_pos()[1]
		return (x > self.x and x < self.x + self.w and y > self.y and y < self.y + self.h)

	def getCollision(self):
		return self.checkCollision()