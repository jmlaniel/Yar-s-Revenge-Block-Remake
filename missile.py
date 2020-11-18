import pygame
import settings
import player

class Missile(pygame.sprite.Sprite):
    def __init__(self,game,color,y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        # Create the image of a block of appropriate size
        self.image = pygame.Surface((settings.BLOCKSIZE,settings.BLOCKSIZE))

        # Fill the image of the block
        self.image.fill(color)

        # Fetch the retangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y
        # This is where our block will appear
        self.rect.x = 0
        self.rect.y = y

        # Timer for delayed launch
        self.MissileClock = pygame.time.get_ticks()

        # Missile state variable
        # 1 = missile set
        # 2 = missile flying
        self.missileState = 1

    def update(self):
        # Update position of missile
        if (self.missileState == 1):
            self.rect.y = self.game.player.rect.y
        elif (self.missileState == 2):
            self.rect.x += settings.MISSILE_VELOCITY

        # Destroy sprite when it reach right side of screen
        if self.rect.x > settings.SCREEN_WIDTH-settings.BLOCKSIZE:
            self.kill()
            self.missileState = 1

        # Check for collision between missile and blocks
        if pygame.sprite.spritecollide(self,self.game.blocks,True):
            # Destroy block and missile
            self.kill()

        # Check for collision between missile and player
        if pygame.sprite.collide_rect(self.game.player,self):
            # End game
            self.game.playing = False
            self.game.running = False

        # Check for collision between missile and enemy (flying or not)
        if pygame.sprite.collide_rect(self.game.enemy,self):
            # End game
            self.game.playing = False
            self.game.running = False

