import sys, pygame, player
pygame.init()
pygame.display.set_caption('Basic Pygame program')

size = width, height, = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

character = pygame.image.load("character.png")
background = pygame.image.load("background.png")

player = player.Player(195, 190, 50, 100, 0, 0, character)

playerx = 295
playery = 190
backgroundx = 0
backgroundy = 0
velx = 0
vely = 0
bvelx = 0
bvely = 0

def render():
	screen.fill(black)
	screen.blit(background, (backgroundx, backgroundy))
	screen.blit(character, (playerx, playery))
	pygame.display.flip()

def update():
	global playery
	global playerx
	global backgroundx
	global backgroundy
	playery += vely
	playerx += velx
	backgroundx += bvelx
	backgroundy += bvely
	if backgroundx >= 0:
		backgroundx = 0
	if playerx >= 295:
		playerx = 295
	if playerx <= 0:
		playerx = 0
	if playery <= 50:
		playery = 50
	if playery >= 380:
		playery = 380

while 1:
	global backgroundx
	render()
	update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				vely = -1
			elif event.key == pygame.K_s:
				vely = 1
			elif event.key == pygame.K_d:
				if playerx < 295:
					velx = 1
				else:
					bvelx = -1
			elif event.key == pygame.K_a:
				if(backgroundx >= 0):
					velx = -1
				else:
					bvelx = 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w or event.key == pygame.K_s:
				vely = 0
			elif event.key == pygame.K_d or event.key == pygame.K_a:
				velx = 0
				bvelx = 0

	

