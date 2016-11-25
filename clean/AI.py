import pygame
import random

class Com(pygame.sprite.Sprite):
    dt = clock.tick(30)
    def __init__(self, *groups):
        #Loading all base components to make up AI 
        super(Com, self).__init__(*groups)
        self.image = pygame.image.load('Com.png')
        self.rect = pygame.rect.Rect((55, 55), self.image.get_size())
        self.timehascome = 0
        self.move = 0

    def update(self, dt, game):
        last = self.rect.copy()
        #makes it so that ai only moves every 10 clock ticks
        if(self.timehascome%10==0):
            self.move = random.randint(1,5)
        self.timehascome += 1
            
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
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last
            self.move = random.randint(1,5)
