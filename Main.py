import pygame, random

from Map import mapp
pygame.init()

from Robot import Robot
pygame.init()

from AI import Com
pygame.init()


imageMap = pygame.image.load("imageMap.png")

ORANGE = (255, 165, 0)
RED = (250, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode()
pygame.display.set_caption("VRS")

all_sprites_list = pygame.sprite.Group()

playerRobot = Robot(RED, 20, 20)
playerRobot.rect.x = 1530
playerRobot.rect.y = 650

AIR = Com(ORANGE, 20, 20)
AIR.rect.x = 130
AIR.rect.y = 130

all_sprites_list.add(playerRobot)
all_sprites_list.add(AIR)

Running = True

mapp()

clock = pygame.time.Clock()

while Running:

    clock.tick(60) #FPS
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing x button (upper right) will quit
                Running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        playerRobot.moveLeft(3)
    if keys[pygame.K_RIGHT]:
        playerRobot.moveRight(3)
    if keys[pygame.K_UP]:
        playerRobot.moveForward(3)
    if keys[pygame.K_DOWN]:
        playerRobot.moveBackward(3)

        
    #Game Logic
    all_sprites_list.update()
    
    #New copy of the image of the map to remove sprite trails    
    screen.blit(imageMap, (0, 0))
        
    #Draw all sprites
    all_sprites_list.draw(screen)

    #Refresh screen
    pygame.display.update()


pygame.quit()
