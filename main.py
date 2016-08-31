import sys, pygame, player
pygame.init()
pygame.display.set_caption('Basic Pygame program')

size = width, height, = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

character = pygame.image.load("character.png")
background = pygame.image.load("background.png")

player = player.Player(295, 190, 50, 100, 0, 0, character)

backgroundx = 0
backgroundy = 0
bvelx = 0
bvely = 0

def render():
	screen.fill(black)
	screen.blit(background, (backgroundx, backgroundy))
	player.render(screen)
	pygame.display.flip()

def update():
	global backgroundx
	global backgroundy
	player.update()
	backgroundx += bvelx
	backgroundy += bvely
	if backgroundx >= 0:
		backgroundx = 0

while 1:
	global backgroundx
	render()
	update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player.setVelY(-1)
			elif event.key == pygame.K_s:
				player.setVelY(1)
			elif event.key == pygame.K_d:
				if player.getX() < 295:
					player.setVelX(1)
				else:
					bvelx = -1
			elif event.key == pygame.K_a:
				if(backgroundx >= 0):
					player.setVelX(-1)
				else:
					bvelx = 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_s:
				player.setVelY(0)
			elif event.key == pygame.K_d or event.key == pygame.K_a:
				player.setVelX(0)
				bvelx = 0

	

