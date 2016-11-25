import pygame, random

from Map import mapp
pygame.init()

from Robot import Player
from Robot import Wall
pygame.init()

from AI import Com
from AI import Wall
pygame.init()

from random import randint

imageMap = pygame.image.load("imageMap.png")

#GREEN = (20, 255, 140)
#GREY = (210, 210, 210)
#WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode()
pygame.display.set_caption("VRS")

all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()


##Pierwsze 0 = Lewo Prawo
##Drugie 0 = Góra , Dół

##Pierwsze 40 = Width/Długość
##Drugie 40 = Height/Wysokość

wall = Wall(0, 0, 1600,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall(0,760,1600,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall(0,40,40,720)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall(0,40,40,720)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall(80,40,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall(1560,40,40,720)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (280,40,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (720,40,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (40,160,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (120,200,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (40,440,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (40,600,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (160,80,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (200,120,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (360,80,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (240,160,40,160)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (200,200,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (320,160,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (40,240,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (40,280,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (280,240,160,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (400,200,160,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (440,80,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (480,80,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (640,120,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (520,160,240,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (520,160,240,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (720,200,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (760,240,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (800,80,40,160)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (840,80,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (960,80,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (880,160,160,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1040,80,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1080,120,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1120,160,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1160,80,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1320,80,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1000,200,40,160)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1040,240,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1200,120,40,240)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1320,120,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1280,160,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1400,160,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1480,160,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1360,200,160,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1360,240,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1480,240,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1440,280,40,120)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1240,240,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (600,240,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (480,280,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (320,320,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (80,360,280,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (640,320,360,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (840,360,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1120,240,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1080,320,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1280,280,40,200)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1240,400,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1320,320,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1520,360,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (160,400,40,280)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (200,440,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (320,400,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (400,400,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (560,360,40,160)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (640,400,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (680,440,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (800,440,160,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (920,400,280,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1080,360,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1360,400,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1080,440,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1400,440,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1400,440,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (280,440,160,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (360,480,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (360,520,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (480,480,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (600,480,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1000,480,40,160)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (80,520,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (280,520,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (680,520,320,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1160,480,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1400,480,40,160)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1440,520,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1080,520,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (240,560,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (440,560,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (680,560,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1160,560,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1280,560,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (320,600,160,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (600,600,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (760,600,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (760,600,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1040,600,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1200,600,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1320,600,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1480,600,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1480,640,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (80,680,280,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (320,640,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (520,640,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (400,680,400,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (760,640,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (840,680,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (920,640,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (960,680,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1000,720,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1080,640,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1160,640,200,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1080,680,120,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1200,720,40,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1280,680,80,40)
wall_list.add(wall)
all_sprites_list.add(wall)

wall= Wall (1400,680,40,80)
wall_list.add(wall)
all_sprites_list.add(wall)


# Create the player paddle object
player = Player(1530, 650)
AIrobot = Com(880, 310)

player.walls = wall_list
AIrobot.walls = wall_list
 
all_sprites_list.add(player)
all_sprites_list.add(AIrobot)

done = False

mapp()



clock = pygame.time.Clock()
tick = 0
move = 0

while not done:

    clock.tick(60)

    #limit AI moves per second
    tick += 1
    
    #Moves 1 block before changing direction
    if tick == 1:
        move = randint(0,3)
        
    if tick %3 == 0:

        #Left
        if move == 0:
            AIrobot.change_x = -3 

        #Right       
        if move == 1:
            AIrobot.change_x = 3

        #Up        
        if move == 2:
            AIrobot.change_y = -3

        #Down        
        if move == 3:
            AIrobot.change_y = 3
                
    elif tick == 31:
        if move == 0:
            AIrobot.change_x = 0
        if move == 1:
            AIrobot.change_x = 0
        if move == 2:
            AIrobot.change_y = 0
        if move == 3:
            AIrobot.change_y = 0
        tick = 0


        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
     
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)



        
    #Game Logic
    all_sprites_list.update()
        
    screen.blit(imageMap, (0, 0))
    #mapp()
        
    #Draw all sprites
    all_sprites_list.draw(screen)

    #Refresh screen
    pygame.display.update()


pygame.quit()
