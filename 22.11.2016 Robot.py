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
 
        #Set size and colour
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        #Align the sprite
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        #Speed of sprite
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        #Alter the speed of the player sprite
        self.change_x += x
        self.change_y += y
 
    def update(self):
        #Update the player position relative to the X axis
        self.rect.x += self.change_x
 
        #Is there a wall in the way?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            
            #When moving right, right side becomes front-facing edge
            if self.change_x > 0:
                self.rect.right = block.rect.left

            #When moving left, left side becomes front-facing edge
            else:
                self.rect.left = block.rect.right
 
        #Update player position relative to the Y axis
        self.rect.y += self.change_y
 
        #Is there a wall in the way?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            #When moving upward, the top side becomes the front-facing edge
            if self.change_y > 0:
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
