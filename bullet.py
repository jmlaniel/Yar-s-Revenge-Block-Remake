import pygame
import settings

class Bullet(pygame.sprite.Sprite):
    def __init__(self,game,color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        # Create the image of a block of appropriate size
        self.image = pygame.Surface((settings.BLOCKSIZE/2,settings.BLOCKSIZE/2))

        # Fill the image of the block
        self.image.fill(color)

        # Fetch the retangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y
        # This is where our block will appear
        self.rect.x = x + settings.BLOCKSIZE/4
        self.rect.y = y + settings.BLOCKSIZE/4

       # Bullet coordinates
        self.x = self.rect.x
        self.y = self.rect.y

        # Time at bullet creation
        settings.BULLET_LAUNCH_TIME = pygame.time.get_ticks()

        # Bullet state variable
        # 0 = no bullet
        # 1 = missile set
        self.bulletState = 0

    def update(self):
        # Update position of block imposing sinusoidal mouvement
        self.x += settings.BULLET_VELOCITY
        self.rect.x = int(self.x)
    
        # Destroy sprite when it reach right side of screen
        if self.rect.x > settings.SCREEN_WIDTH-settings.BLOCKSIZE/4:
            self.kill()
        
        # Check for collision between bullet and blocks
        pygame.sprite.groupcollide(self.game.bullets,self.game.blocks,True,True)
