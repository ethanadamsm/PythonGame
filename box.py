import sys, pygame

class Box():
	def __init__(self, x, y, w, h):		
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.visible = False

	def render(self, screen):
		if self.visible:
			screen.blit(self.image, (self.x, self. y))

	def addImage(self, image):
		self.image = image
		self.image = pygame.transform.scale(self.image, (self.w, self.h))
		self.visible = True