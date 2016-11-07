def controls():

    PLAYER = pygame.image.load(".png").convert_alpha()  #Player Image
    PlayerPos = [0,0]   #Player position [X,Y]

    #*by TILESIZE to scale model to match tile pixels,
    #e.g. is 1 pixel to start, scales so moves 1 tile instead of 1 pixel
    DISPLAYSURF.blit(PLAYER,(PlayerPos[0]*TILESIZE,PlayerPos[1]*TILESIZE))

    for event in pygame.event.get():
        if event.type == KEYDOWN: #Key is pressed

            if (event.key == K_RIGHT) and PlayerPos[0] < MAPWIDTH -1:
                PlayerPos[0] += 1    #Move player 1 increment right

            elif (event.key == K_LEFT) and PlayerPos[0] >0:
                PlayerPos[0] -= 1    #Move player 1 increment left

            elif (event.key == K_UP) and PlayerPos[1] >0:
                PlayerPos[1] -= 1    #Move player 1 increment up

            elif (event.key == K_DOWN) and PlayerPos[1] < MAPHEIGHT -1:
                PlayerPos[1] += 1    #Move player 1 increment down

