import pygame
pygame.init()

screen = pygame.display.set_mode((1061,596))
background = pygame.image.load('jungleresized1.jpeg')


pygame.display.set_caption("Jungle Hunt!!!")
icon = pygame.image.load('man.png')
pygame.display.set_icon(icon)

playerImage = pygame.image.load('enemy.png')
playerX = 570
playerY = 220
playerX_change = 0

def player(playerX,playerY):
	screen.blit(playerImage,(playerX,playerY))

run = True

while run:
	screen.fill((255,0,0))
	screen.blit(background,(0,0))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False


	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_LEFT:
			playerX_change = -5
		if event.key == pygame.K_RIGHT:
			playerX_change = 5


	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LEFT or pygame.K_RIGHT:
			playerX_change = 0

	player(playerX,playerY)
	pygame.display.update()