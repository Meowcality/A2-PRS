### Import files ###

import pygame, random

from Map import mapp
pygame.init()

from Robot import Player
from Robot import Wall
pygame.init()

from AI import Com
pygame.init()

from random import randint

### GUI ###

#Import Images
MainMenu = pygame.image.load("MainMenu.png")
Instructions = pygame.image.load("Instructions.png")
Controls = pygame.image.load("Controls.png")
Victory = pygame.image.load("Victory.png")
GameOver = pygame.image.load("GameOver.png")

#Current menu page
MenuScreen = MainMenu

### GUI end ###

#Images of states of the map
#Not collected key
imageMap = pygame.image.load("imageMap.png")
#Collected key
imageMap2 = pygame.image.load("imageMap2.png")


#Image of current state of map
backgroundImage = imageMap

#Colours
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
BLACK = (0, 0, 0)

#Initialise Display window
screen = pygame.display.set_mode()
pygame.display.set_caption("Virtual Robot Simulator")

#Sprite groups
all_sprites_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

### Wall sprites ###

##First 0 = Left, right
##Second 0 = Up, down

##First 40 = Width
##Second 40 = Height

#Creating wall sprites
#Adding wall sprites to sprite groups
wall = Wall(0, 0, 1600,40)
wall_list.add(wall)

wall= Wall(0,760,1600,40)
wall_list.add(wall)

wall= Wall(0,40,40,720)
wall_list.add(wall)

wall= Wall(0,40,40,720)
wall_list.add(wall)

wall= Wall(80,40,40,80)
wall_list.add(wall)

wall= Wall(1560,40,40,720)
wall_list.add(wall)

wall= Wall (280,40,40,40)
wall_list.add(wall)

wall= Wall (720,40,40,80)
wall_list.add(wall)

wall= Wall (40,160,120,40)
wall_list.add(wall)

wall= Wall (120,200,40,40)
wall_list.add(wall)

wall= Wall (40,440,40,40)
wall_list.add(wall)

wall= Wall (40,600,80,40)
wall_list.add(wall)

wall= Wall (160,80,80,40)
wall_list.add(wall)

wall= Wall (200,120,200,40)
wall_list.add(wall)

wall= Wall (360,80,40,40)
wall_list.add(wall)

wall= Wall (240,160,40,160)
wall_list.add(wall)

wall= Wall (200,200,40,40)
wall_list.add(wall)

wall= Wall (320,160,40,40)
wall_list.add(wall)

wall= Wall (40,240,40,40)
wall_list.add(wall)

wall= Wall (40,280,120,40)
wall_list.add(wall)

wall= Wall (200,280,40,40)
wall_list.add(wall)

wall= Wall (280,240,80,40)
wall_list.add(wall)

wall= Wall (400,240,40,40)
wall_list.add(wall)

wall= Wall (400,200,160,40)
wall_list.add(wall)

wall= Wall (440,80,40,80)
wall_list.add(wall)

wall= Wall (480,80,200,40)
wall_list.add(wall)

wall= Wall (520,160,240,40)
wall_list.add(wall)

wall= Wall (720,200,40,80)
wall_list.add(wall)

wall= Wall (760,240,200,40)
wall_list.add(wall)

wall= Wall (800,80,40,160)
wall_list.add(wall)

wall= Wall (840,80,80,40)
wall_list.add(wall)

wall= Wall (960,80,40,80)
wall_list.add(wall)

wall= Wall (880,160,160,40)
wall_list.add(wall)

wall= Wall (1040,80,80,40)
wall_list.add(wall)

wall= Wall (1080,120,40,80)
wall_list.add(wall)

wall= Wall (1120,160,40,40)
wall_list.add(wall)

wall= Wall (1160,80,120,40)
wall_list.add(wall)

wall= Wall (1320,80,200,40)
wall_list.add(wall)

wall= Wall (1000,200,40,160)
wall_list.add(wall)

wall= Wall (1040,240,40,40)
wall_list.add(wall)

wall= Wall (1200,120,40,240)
wall_list.add(wall)

wall= Wall (1320,120,40,40)
wall_list.add(wall)

wall= Wall (1280,160,40,40)
wall_list.add(wall)

wall= Wall (1400,160,40,40)
wall_list.add(wall)

wall= Wall (1480,160,40,40)
wall_list.add(wall)

wall= Wall (1360,200,160,40)
wall_list.add(wall)

wall= Wall (1480,240,40,80)
wall_list.add(wall)

wall= Wall (1440,280,40,120)
wall_list.add(wall)

wall= Wall (1240,240,80,40)
wall_list.add(wall)

wall= Wall (600,240,80,40)
wall_list.add(wall)

wall= Wall (480,280,200,40)
wall_list.add(wall)

wall= Wall (320,320,200,40)
wall_list.add(wall)

wall= Wall (80,360,280,40)
wall_list.add(wall)

wall= Wall (640,320,120,40)
wall_list.add(wall)

wall= Wall (880,320,120,40)
wall_list.add(wall)

wall= Wall (1120,240,40,80)
wall_list.add(wall)

wall= Wall (1080,320,120,40)
wall_list.add(wall)

wall= Wall (1280,280,40,200)
wall_list.add(wall)

wall= Wall (1240,400,40,40)
wall_list.add(wall)

wall= Wall (1320,320,120,40)
wall_list.add(wall)

wall= Wall (1520,360,40,40)
wall_list.add(wall)

wall= Wall (160,400,40,200)
wall_list.add(wall)

wall= Wall (160,640,40,40)
wall_list.add(wall)

wall= Wall (200,440,40,80)
wall_list.add(wall)

wall= Wall (320,400,40,40)
wall_list.add(wall)

wall= Wall (400,400,120,40)
wall_list.add(wall)

wall= Wall (560,360,40,160)
wall_list.add(wall)

wall= Wall (640,400,200,40)
wall_list.add(wall)

wall= Wall (680,440,80,40)
wall_list.add(wall)

wall= Wall (800,440,160,40)
wall_list.add(wall)

wall= Wall (920,400,280,40)
wall_list.add(wall)

wall= Wall (1080,360,40,40)
wall_list.add(wall)

wall= Wall (1360,400,40,40)
wall_list.add(wall)

wall= Wall (1080,440,40,40)
wall_list.add(wall)

wall= Wall (1400,440,120,40)
wall_list.add(wall)

wall= Wall (280,440,160,40)
wall_list.add(wall)

wall= Wall (360,480,80,40)
wall_list.add(wall)

wall= Wall (360,520,40,40)
wall_list.add(wall)

wall= Wall (480,480,80,40)
wall_list.add(wall)

wall= Wall (600,480,40,40)
wall_list.add(wall)

wall= Wall (1000,480,40,160)
wall_list.add(wall)

wall= Wall (80,520,80,40)
wall_list.add(wall)

wall= Wall (280,520,40,40)
wall_list.add(wall)

wall= Wall (680,520,320,40)
wall_list.add(wall)

wall= Wall (1160,480,200,40)
wall_list.add(wall)

wall= Wall (1400,480,40,160)
wall_list.add(wall)

wall= Wall (1440,520,120,40)
wall_list.add(wall)

wall= Wall (1080,520,120,40)
wall_list.add(wall)

wall= Wall (240,560,40,80)
wall_list.add(wall)

wall= Wall (440,560,120,40)
wall_list.add(wall)

wall= Wall (600,560,40,40)
wall_list.add(wall)

wall= Wall (680,560,40,80)
wall_list.add(wall)

wall= Wall (1160,560,80,40)
wall_list.add(wall)

wall= Wall (1280,560,80,40)
wall_list.add(wall)

wall= Wall (320,600,160,40)
wall_list.add(wall)

wall= Wall (600,600,40,40)
wall_list.add(wall)

wall= Wall (760,600,200,40)
wall_list.add(wall)

wall= Wall (760,600,200,40)
wall_list.add(wall)

wall= Wall (1040,600,80,40)
wall_list.add(wall)

wall= Wall (1200,600,40,40)
wall_list.add(wall)

wall= Wall (1320,600,40,40)
wall_list.add(wall)

wall= Wall (1480,600,80,40)
wall_list.add(wall)

wall= Wall (1480,640,40,80)
wall_list.add(wall)

wall= Wall (80,680,280,40)
wall_list.add(wall)

wall= Wall (320,640,40,40)
wall_list.add(wall)

wall= Wall (520,640,40,40)
wall_list.add(wall)

wall= Wall (400,680,240,40)
wall_list.add(wall)

wall= Wall (680,680,120,40)
wall_list.add(wall)

wall= Wall (760,640,40,40)
wall_list.add(wall)

wall= Wall (840,680,40,80)
wall_list.add(wall)

wall= Wall (920,640,40,80)
wall_list.add(wall)

wall= Wall (960,680,80,40)
wall_list.add(wall)

wall= Wall (1000,720,40,40)
wall_list.add(wall)

wall= Wall (1080,640,40,40)
wall_list.add(wall)

wall= Wall (1160,640,200,40)
wall_list.add(wall)

wall= Wall (1080,680,120,40)
wall_list.add(wall)

wall= Wall (1280,680,80,40)
wall_list.add(wall)

wall= Wall (1400,680,40,40)
wall_list.add(wall)

### Wall sprrites end ###

# Create the player paddle object
player = Player(1530, 650)
AIrobot = Com(880, 310)

player.walls = wall_list
AIrobot.walls = wall_list
 
all_sprites_list.add(player)
all_sprites_list.add(AIrobot)




#Initialise Map
mapp()

#Variables
clock = pygame.time.Clock()
Menus = True
done = False
Key = False
Door = False
tick = 0
move = 0
speed = 5
   

#Main running loop
while not done:

    clock.tick(60)        

### GUI ###
    if Menus == True:
        screen.blit(MenuScreen, (0,0))

        if MenuScreen == Victory:
            for event in pygame.event.get():
                if event.key == pygame.K_ESCAPE:
                    done = True

        elif MenuScreen == GameOver:
            for event in pygame.event.get():
                if event.key == pygame.K_ESCAPE:
                    done = True

        else:
            
            for event in pygame.event.get():

                #Quits game window (Press x in upper right corner)
                if event.type == pygame.QUIT:
                    done = True

                #if key is pressed 
                elif event.type == pygame.KEYDOWN:

                    #if left key is pressed
                    if event.key == pygame.K_LEFT:
                        MenuScreen = Instructions
                        screen.blit(Instructions, (0,0))

                    #if right key is pressed
                    elif event.key == pygame.K_RIGHT:
                        MenuScreen = Controls
                        screen.blit(Controls, (0,0))
                        
                    #if down key is pressed    
                    elif event.key == pygame.K_DOWN:
                        done = True

                    elif event.key == pygame.K_ESCAPE:
                        MenuScreen = MainMenu

                #Begin game
                elif event.type == pygame.KEYUP:

                    if event.key == pygame.K_UP:
                        Menus = False


        #Refresh screen
        pygame.display.update()

### GUI end ###
        
        
    else:

        #Current player coordinates
        playerCoord = player.rect.center
        playerCoord_x, playerCoord_y = playerCoord

        #Current AI coordinates
        AICoord = AIrobot.rect.center
        AICoord_x, AICoord_y = AICoord

### AI running code ###
        
        #limit AI moves per second
        tick += 1
        
        #Moves 1 block before changing direction
        if tick == 1:
            move = randint(0,3)
            
        #Limits AI moves per second
        if tick %3 == 0:

            #Left
            if move == 0:
                AIrobot.xMoveSpeed = -3 

            #Right       
            if move == 1:
                AIrobot.xMoveSpeed = 3

            #Up        
            if move == 2:
                AIrobot.yMoveSpeed = -3

            #Down        
            if move == 3:
                AIrobot.yMoveSpeed = 3

        #Reset AI speed to move in new direction            
        elif tick == 31:
            if move == 0:
                AIrobot.xMoveSpeed = 0
            if move == 1:
                AIrobot.xMoveSpeed = 0
            if move == 2:
                AIrobot.yMoveSpeed = 0
            if move == 3:
                AIrobot.yMoveSpeed = 0
            tick = 0

### AI running code end ###
       
        for event in pygame.event.get():

            #Quits game window
            if event.type == pygame.QUIT:
                done = True

### Player running code ###
                
            #When arrow keys are pressed
            elif event.type == pygame.KEYDOWN:
                
                #Left key pressed
                if event.key == pygame.K_LEFT:
                    player.playerSpeed(-speed, 0)

                #Right key pressed
                elif event.key == pygame.K_RIGHT:
                    player.playerSpeed(speed, 0)

                #Up key pressed
                elif event.key == pygame.K_UP:
                    player.playerSpeed(0, -speed)

                #Down key pressed
                elif event.key == pygame.K_DOWN:
                    player.playerSpeed(0, speed)
         
            #When keys are released, reset player model speed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.playerSpeed(speed, 0)
                elif event.key == pygame.K_RIGHT:
                    player.playerSpeed(-speed, 0)
                elif event.key == pygame.K_UP:
                    player.playerSpeed(0, speed)
                elif event.key == pygame.K_DOWN:
                    player.playerSpeed(0, -speed)
                    
### PLayer running code end ###

### Win / Lose conditions ###

        #Player passes onto block to pick up key
        if ((playerCoord_x > 200) and (playerCoord_x < 240)) and ((playerCoord_y > 400) and (playerCoord_y < 440)):
            Key = True
            backgroundImage = imageMap2

        #player passes onto door to unlock door - only works if key has been picked up
        if (Key == True) and ((playerCoord_x > 40) and (playerCoord_x < 80)) and ((playerCoord_y > 40) and (playerCoord_y < 80)):
            Door = True
            MenuScreen = Victory
            Menus = True
            
        #When player collides with AI
        if ((playerCoord_x - 10) < (AICoord_x + 10)) and ((playerCoord_x + 10) > (AICoord_x - 10)) and ((playerCoord_y - 10) < (AICoord_y + 10)) and ((playerCoord_y + 10) > (AICoord_y - 10)):
            MenuScreen = GameOver
            Menus = True

### Win / Lose conditions end ###
            

          
        #Update Sprite list
        all_sprites_list.update()

        #Draw wall sprites
        wall_list.draw(screen)  

        #Re-print image of map to remove sprite trails
        screen.blit(backgroundImage, (0, 0))
            
        #Draw all sprites
        all_sprites_list.draw(screen)

        #Refresh screen
        pygame.display.update()

#Quit game
pygame.quit()
