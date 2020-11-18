import pygame
import settings

class Zone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Create the image of a block of appropriate size
        self.image = pygame.Surface((settings.BLOCKSIZE*8,settings.BLOCKSIZE*39))

        # Fill the image of the block
        self.image.fill(settings.GRAY)

        # Fetch the retangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y
        # This is where our block will appear
        self.rect.x = settings.BLOCKSIZE*10
        self.rect.y = settings.BLOCKSIZE*0
