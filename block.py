import pygame
import math
import settings

class Block(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)

        # Create the image of a block of appropriate size
        self.image = pygame.Surface((settings.BLOCKSIZE,settings.BLOCKSIZE))

        # Fill the image of the block
        self.image.fill(color)

        # Fetch the retangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y
        # This is where our block will appear
        self.rect.x = x
        self.rect.y = y

        # Store original coordinates of each block sprite
        self.OriginalX = x
        self.OriginalY = y

    def update(self):
        # Update position of block imposing sinusoidal mouvement
        d_y = settings.WALL_AMPLITUDE*math.cos(2*math.pi*settings.WALL_FREQUENCY*pygame.time.get_ticks()/1000)
        self.rect.y = self.OriginalY + d_y 
