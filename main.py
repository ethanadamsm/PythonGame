import sys, pygame, player, enemy, sword, gui
pygame.init()
pygame.display.set_caption('Basic Pygame program')

size = width, height, = 640, 480
black = 0, 0, 0

start = False
menu = True

screen = pygame.display.set_mode(size)

character = pygame.image.load("character.png")
zombie = pygame.image.load("enemy.png")
background = pygame.image.load("background.png")
menubackground = pygame.image.load("menubackground.png")
enemies = []
enemies.append(enemy.Enemy(400, 190, 50, 100, 0, 0, zombie))
enemies.append(enemy.Enemy(700, 300, 50, 100, 0, 0, zombie))
enemies.append(enemy.Enemy(110, 200, 50, 100, 0, 0, zombie))

playerGui = gui.Gui(430, 10, 200, 460)
playerGui.setVisible(False)

playerGui.addBox(440, 30, 180, 180)
playerGui.addImage(0, pygame.image.load("playerpro.png"))

playerGui.addBox(450, 220, 40, 40)
playerGui.setBoxVisible(1, True)
playerGui.setBoxText(1, "Coins:")
playerGui.setBoxFontSize(1, 20)

playerGui.addBox(470, 220, 100, 40)
playerGui.setBoxVisible(2, True)
playerGui.setBoxText(2, "0")
playerGui.setBoxFontSize(2, 20)

playerGui.addBox(530, 232, 20, 20)
playerGui.setBoxVisible(3, True)
playerGui.addImage(3, pygame.image.load("coin.png"))

menuGui = gui.Gui(50, 50, 540, 380)

menuGui.addButton(220, 90, 200, 50)
menuGui.addImageButton(0, pygame.image.load("square.png"))
menuGui.setButtonText(0, "Play")

menuGui.addButton(220, 160, 200, 50)
menuGui.addImageButton(1, pygame.image.load("square.png"))
menuGui.setButtonText(1, "Load")

menuGui.addButton(220, 230, 200, 50)
menuGui.addImageButton(2, pygame.image.load("square.png"))
menuGui.setButtonText(2, "Settings")

player = player.Player(295, 190, 50, 100, 0, 0, character)
player.addItem(sword.Sword(300, 230, 40, 10, "sword.png"))
player.addItem(sword.Sword(300, 230, 70, 20, "sword2.png"))
player.getItem(1).setVisible(False)

backgroundx = 0
backgroundy = 0
bvelx = 0
bvely = 0
d = False
a = False
items = []

def render():
	screen.fill(black)
	if start:
		screen.blit(background, (backgroundx, backgroundy))
		player.render(screen, d, a)
		for enemy in enemies:
			if enemy != "":
				enemy.render(screen)
		for item in items: #item update loop
			item.render(screen)
		playerGui.render(screen)
	if menu:
		screen.blit(menubackground, (0, 0))
		menuGui.render(screen)
	pygame.display.flip()

def update():
	global menu
	global start
	if menu:
		print(menuGui.collideButton())
		if pygame.mouse.get_pressed()[0] and menuGui.collideButton() == 0:
			start = True
			menu = False
	if start:
		global backgroundx
		global backgroundy
		global enemies
		player.update()
		backgroundx += bvelx
		backgroundy += bvely
		if backgroundx >= 0: #background x bound
			backgroundx = 0
		for x in range(0, len(enemies)): #enemy append item list
			if enemies[x] != "":
				enemies[x].update(player.getX(), player.getY(), d, a)
				if enemies[x].getAlive() == False:
					items.append(enemies[x].getDroppedItem())
					enemies[x] = ""
		for enemy in enemies:
			#player sword collision with enemy
			if enemy != "" and checkCollision(player.getItemX(), player.getItemY(), player.getItemW(), player.getItemH(), enemy.getX(), enemy.getY(), enemy.getW(), enemy.getH()):
				enemy.setHealth(enemy.getHealth() - .3)
			#enemy collision with player
			if enemy != "" and checkCollision(player.getX(), player.getY(), 50, 100, enemy.getX(), enemy.getY(), enemy.getW(), enemy.getH()):
				player.setHealth(player.getHealth() - .5)
		for item in items: #collision with items (coins)
			if(item != ""):
				item.update(d, a)
				if checkCollision(player.getX(), player.getY(), 50, 100, item.getX(), item.getY(), item.getW(), item.getH()):
					if(item.getVisible()):
						num = int(playerGui.getBoxText(2)) + 1
						playerGui.setBoxText(2, str(num))
					item.setVisible(False)


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
			elif event.key == pygame.K_i:
				playerGui.setVisible(True)
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
			elif event.key == pygame.K_i:
				playerGui.setVisible(False)
	update()

	

