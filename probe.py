import pygame
import settings
import math

class Probe(pygame.sprite.Sprite):
    def __init__(self,game,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        # Create the image of a block of appropriate size
        self.image = pygame.Surface((settings.BLOCKSIZE,settings.BLOCKSIZE/4))

        # Fill the image of the block
        self.image.fill(color)

        # Fetch the retangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y
        # This is where our block will appear
        self.rect.x = x
        self.rect.y = y

        # Probe coordinates
        self.x = x
        self.y = y

    def update(self):
        # Update position of missile
        d_x = self.game.player.rect.x - self.rect.x
        d_y = self.game.player.rect.y - self.rect.y + settings.BLOCKSIZE/2
        r = math.sqrt(d_x ** 2 + d_y ** 2)
        self.x += settings.PROBE_VELOCITY*d_x/r
        self.rect.x = self.x
        self.y += settings.PROBE_VELOCITY*d_y/r
        self.rect.y = self.y

        # Check for collision between player and probe. Exception : player is in the zone
        if pygame.sprite.collide_rect(self,self.game.player):
            # End game
            self.game.playing = False
            self.game.running = False

