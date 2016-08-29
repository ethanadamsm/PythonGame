import sys, pygame
pygame.init()
pygame.display.set_caption('Basic Pygame program')

size = width, height, = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

person = pygame.image.load("random.jpg")
background = pygame.image.load("background.png")
personrect = person.get_rect()

def render():
	screen.fill(black)
	screen.blit(person, (50, 50))
	pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		render()

