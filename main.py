import sys, pygame, player, enemy, sword
pygame.init()
pygame.display.set_caption('Basic Pygame program')

size = width, height, = 640, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

character = pygame.image.load("character.png")
zombie = pygame.image.load("enemy.png")
background = pygame.image.load("background.png")

player = player.Player(295, 190, 50, 100, 0, 0, character)
player.addItem(sword.Sword(300, 230, 40, 10, "sword.png"))
player.addItem(sword.Sword(300, 230, 70, 20, "sword2.png"))
player.getItem(1).setVisible(False)

zombie = enemy.Enemy(400, 190, 50, 100, 0, 0, zombie)

backgroundx = 0
backgroundy = 0
bvelx = 0
bvely = 0
d = False
a = False
items = []

def render():
	screen.fill(black)
	screen.blit(background, (backgroundx, backgroundy))
	player.render(screen)
	if zombie != "":
		zombie.render(screen)
	pygame.display.flip()
	if zombie == "":
		screen.blit(items[0].getImage(), (items[0].getX(), items[0].getY()))
		for item in items:
			item.render(screen)

def update():
	global backgroundx
	global backgroundy
	global zombie
	player.update()
	backgroundx += bvelx
	backgroundy += bvely
	if backgroundx >= 0:
		backgroundx = 0
	if zombie != "" and checkCollision(player.getItemX(), player.getItemY(), player.getItemW(), player.getItemH(), zombie.getX(), zombie.getY(), zombie.getW(), zombie.getH()):
		zombie.setHealth(zombie.getHealth() - .3)
	if zombie != "" and checkCollision(player.getX(), player.getY(), 50, 100, zombie.getX(), zombie.getY(), zombie.getX(), zombie.getY()):
		player.setHealth(player.getHealth() - .5)
	if zombie != "":
		zombie.update(player.getX(), player.getY(), d, a)
		if zombie.getAlive() == False:
			items.append(zombie.getDroppedItem())
			zombie = ""
			print items[0].getX()
			print items[0].getY()
			print items[0].getImage()

def checkCollision(x, y, w, h, x2, y2, w2, h2):
	return ((x < x2 + w2) and (x + w > x2) and (y < y2 + h2) and (y + h > y2))

while 1:
	#global backgroundx
	#global player
	render()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN: #keydown
			if event.key == pygame.K_w:
				player.setVelY(-1)
				#player.moveItem(0, -1)
			elif event.key == pygame.K_s:
				player.setVelY(1)
				#player.moveItem(0, 1)
			elif event.key == pygame.K_d:
				player.setLeft(True)
				if player.getX() < 295:
					player.setVelX(1)
					#player.moveItem(1, 0)
				else:
					bvelx = -1
					#zombie.setVelX(zombie.getVelX() - 1) 
					d = True
			elif event.key == pygame.K_a:
				player.setRight(True)
				if(backgroundx >= 0):
					player.setVelX(-1)
					#player.moveItem(-1, 0)
				else:
					bvelx = 1
					if player.getVelX != 0:
						a = True
			elif event.key == pygame.K_g:
				player.addItem()
			elif event.key == pygame.K_SPACE and event.key != pygame.K_1 and event.key != pygame.K_2:
				player.rotateItem(270)
				player.setAttackLeft(True)
			elif event.key == pygame.K_1:
				player.setCurrent(0)
			#if(len(player.getInventory()) > 1):
			if event.key == pygame.K_2:
				player.setCurrent(1)
		if event.type == pygame.KEYUP: #keyup
			if event.key == pygame.K_w or event.key == pygame.K_s:
				player.setVelY(0)
				#player.moveItem(0, 0)
			elif event.key == pygame.K_d or event.key == pygame.K_a:
				player.setLeft(False)
				player.setRight(False)
				player.setVelX(0)
				#player.moveItem(0, 0)
				bvelx = 0
				#zombie.setVelX(zombie.getVelX() + 1)
				d = False
				a = False
			elif event.key == pygame.K_SPACE:
				player.setAttackLeft(False)
				player.rotateItem(90)
	update()

	

