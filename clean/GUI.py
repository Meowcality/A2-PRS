import pygame

def Menu():
    #game window    
    screen = pygame.display.set_mode()
    #importing images
    MainMenu = pygame.image.load("MainMenu.png")
    Instructions = pygame.image.load("Instructions.png")
    Controls = pygame.image.load("Controls.png")
    Victory = pygame.image.load("Victory.png")
    GameOver = pygame.image.load("GameOver.png")

    #GUI
        if Menus == True:
            screen,blot(MenuScreen, (0,0))

            if MenuScreen == Victory:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True
                            
            elif MenuScreen == GameOver:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            done = True
else:

    for event in pygame.event.get():

        #if key is pressed 
        if event.type == pygame.KEYDOWN:

            #if left key is pressed
           if event.key == pygame.K_LEFT:
                #displays image on screen
                screen.blit(Instructions, (0,0))

            #if right key is pressed
            elif event.key == pygame.K_RIGHT:
                #displays image on screen
                screen.blit(Controls, (0,0))
            #if up key is pressed
            elif event.key == pygame.K_UP:
                pass
            #if down key is pressed    
            elif event.key == pygame.K_DOWN:
                pygame.quit()

            elif event.key == pygame.K_ESCAPE:
                screen.blit(MainMenu, (0,0))
                
            
