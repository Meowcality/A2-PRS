import pygame
import random

WHITE = (255, 255, 255)

clock = pygame.time.Clock()

class Com(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        #Loading all base components to make up AI 
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        #self.image = pygame.image.load('Com.png')
        #self.rect = pygame.rect.Rect(55, 55) #, self.image.get_size())

        timehascome = 0
        move = 0
            
        #def update(self):
        dt = clock.tick(60)
        last = self.rect.copy()

        #makes it so that ai only moves every 10 clock ticks
        if(timehascome%10==0):
            self.move = random.randint(1,5)
        timehascome += 1
                
        #Ai moves 200 * clocktick in any given direction 
        if self.move == 1:
            self.rect.x -= 200 * dt
        if self.move == 2:
            self.rect.x += 200 * dt
        if self.move == 3:
            self.rect.y -= 200 * dt
        if self.move == 4:
            self.rect.y += 200 * dt
                        
            #during collisions ai self rectifies and tries to move in a different direction
    """
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last
            self.move = random.randint(1,5)"""
