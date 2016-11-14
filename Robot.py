import pygame
WHITE = (255, 255, 255)

class Robot(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        #Color of robot, its X Y position, its width and height
        #Set the background color to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        #Draw the robot (a rectangle)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        #In order to load an image to the the robot
        #self.image = pygame.image.load("robot.png").convert_alpha()

        #Fetch rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        
    def moveForward(self, pixels):
        self.rect.y -= pixels

    def moveBackward(self, pixels):
        self.rect.y += pixels
        
