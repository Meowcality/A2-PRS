import pygame

from Map import mapp
pygame.init()

from Robot import Robot
pygame.init()

from AI import Com
pygame.init()

from random import randint


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
tick = 0
move = 0

while Running:
    
    #FSP
    clock.tick(60)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False            
        elif event.type==pygame.KEYDOWN:
            #Pressing x button (upper right) will quit
            if event.key==pygame.K_x: 
                Running = False

    #limit AI moves per second
    tick += 1

    #Moves 1 block before changing direction
    if tick == 1:
        move = randint(0,3)
    #Moves moves 2 pixels at a time
    #smoother movement
    if tick %3 == 0:
        if move == 0:
            AIR.goRight(2)
        if move == 1:
            AIR.goLeft(2)
        if move == 2:
            AIR.goForward(2)
        if move == 3:
            AIR.goBackward(2)      
    elif tick == 61:
        tick = 0

        
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
