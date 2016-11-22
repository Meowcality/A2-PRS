""" The website http://programarcadegames.com/python_examples/show_file.php?file=move_with_walls_example.py (22/11/2016)
was used to aid creation of the code used for sprite collisions."""


import pygame
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#Player sprite class
class Player(pygame.sprite.Sprite):

    #Player sprite
    def __init__(self, x, y):
        super().__init__() 
 
        #Create the sprite model
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        #Sets the speed variables of the player sprite to be zero.
        self.speedX = 0
        self.speedY = 0

	#Increments the speed of the player based on the axis of the player.
	#X for left and right.
        #Y for up and down.
    def playerSpeed(self, x, y):
        self.speedX += x
        self.speedY += y

	#Updates the player sprite for X axis.
        #Based on the speed of the player.
        #Current position + speed.
    def update(self):
        self.rect.x += self.speedX
 
        #Checks if there's a wall in the way when the player is moving.
        check_collision = pygame.sprite.spritecollide(self, self.walls, False)
        for collision in check_collision:
            
            
            if self.speedX > 0:
                self.rect.right = collision.rect.left

            #When moving left, left side becomes front-facing edge
            else:
                self.rect.left = collision.rect.right
 
        #Update player position relative to the Y axis
        self.rect.y += self.speedY
 
        #Is there a wall in the way?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            #When moving upward, the top side becomes the front-facing edge
            if self.speedY > 0:
                self.rect.bottom = block.rect.top

            #When moving downward, the top side becomes the front-facing edge
            else:
                self.rect.top = block.rect.bottom


#Wall class sprite
class Wall (pygame.sprite.Sprite):

    def __init__(self, x, y, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])

        #Set position of the sprites
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
