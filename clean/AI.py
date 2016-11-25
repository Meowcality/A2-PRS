import pygame
import random

#Colours
PURPLE = (255, 0, 255)

class Com(pygame.sprite.Sprite):
    
    #AI sprite
    def __init__(self, x, y):
        super().__init__() 
 
        #Model for AI sprite
        self.image = pygame.Surface([20, 20])
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        #Ai sprite speed variable
        self.xMoveSpeed = 0
        self.yMoveSpeed = 0

    def playerSpeed(self, x, y):
        self.xMoveSpeed += x
        self.yMoveSpeed += y

    def update(self):
        self.rect.x += self.xMoveSpeed
     ### Start of Mateusz contribution ### 
        #Checks for collision with other sprites
        check_collision = pygame.sprite.spritecollide(self, self.walls, False)
        for collision in check_collision:
            
            #front becomes direction of travel           
            if self.xMoveSpeed > 0:
                self.rect.right = collision.rect.left

            #front becomes direction of travel
            else:
                self.rect.left = collision.rect.right
 

        self.rect.y += self.yMoveSpeed
 
        #Checks for collision with other sprites
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            #front becomes direction of travel
            if self.yMoveSpeed > 0:
                self.rect.bottom = block.rect.top

            #front becomes direction of travel
            else:
                self.rect.top = block.rect.bottom
    ### End of Mateusz contribution ### 

