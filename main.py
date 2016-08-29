import sys, pygame
pygame.init()
pygame.display.set_caption('Basic Pygame program')

size = width, height, = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

character = pygame.image.load("character.png")
background = pygame.image.load("background.png")

playerx = 295
playery = 190

def render():
	screen.fill(black)
	screen.blit(background, (0, 0))
	screen.blit(character, (playerx, playery))
	pygame.display.flip()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		render()
		if event.type == pygame.KEYDOWN:
			playery -= 1
			print("w")

