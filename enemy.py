import pygame
import math
import settings

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        # Create the image of a block of appropriate size (2*BLOCKSIZE)
        self.image = pygame.Surface((settings.BLOCKSIZE*2,settings.BLOCKSIZE*2))

        # Fill the image of the block
        self.image.fill(color)

        # Fetch the retangle object that has the dimensions of the image
        self.rect = self.image.get_rect()

        # Move the top left of the rectangle to x,y
        # This is where our block will appear
        self.rect.x = x
        self.rect.y = y

        # Enemy coordinates
        self.x = x
        self.y = y

        # Store original coordinates of each block sprite
        self.OriginalX = x
        self.OriginalY = y
        
        # Velocity vector
        self.xVelocity = 0
        self.yVelocity = 0

        # Timer for enemy state durations
        self.enemyClock = pygame.time.get_ticks()
        self.flashClock = 0

        # Enemy state variable
        # 0 = doing nothing
        # 1 = flashing
        # 2 = attacking
        self.enemyState = 0

    def update(self):
        # Update position of block imposing sinusoidal mouvement when not attacking
        if (self.enemyState !=2):
            d_y = settings.WALL_AMPLITUDE*math.cos(2*math.pi*settings.WALL_FREQUENCY*pygame.time.get_ticks()/1000)
            self.y = self.OriginalY + d_y
            self.rect.y = self.y

        # Test for flash sequence start
        if (pygame.time.get_ticks() - self.enemyClock > settings.ENEMY_DELAY) and (self.enemyState == 0):
            # Set flashing state
            self.enemyState = 1
            # Reset clock
            self.flashClock = pygame.time.get_ticks()
            # Set initial color for flash state
            self.image.fill(settings.BLUE)

        # Test for attack sequence start
        if (pygame.time.get_ticks() - self.enemyClock > settings.ENEMY_FLASHING_DURATION) and (self.enemyState == 1):
            # Set flashing state
            self.enemyState = 2
            # Set initial color for attack state
            self.image.fill(settings.RED)
            # Establish velocity vector
            d_x = self.game.player.rect.x - self.rect.x - settings.BLOCKSIZE/2
            d_y = self.game.player.rect.y - self.rect.y - settings.BLOCKSIZE/2
            r = math.sqrt(d_x ** 2 + d_y ** 2)
            self.xVelocity = settings.ENEMY_VELOCITY*d_x/r
            self.yVelocity = settings.ENEMY_VELOCITY*d_y/r

        # Flashing state (flash 10 times)
        if self.enemyState == 1:
            if pygame.time.get_ticks() - self.flashClock < settings.ENEMY_FLASHING_DURATION/20:
                self.image.fill(settings.BLUE)
            elif pygame.time.get_ticks() - self.flashClock > settings.ENEMY_FLASHING_DURATION/20:
                self.image.fill(settings.YELLOW)
            if pygame.time.get_ticks() - self.flashClock >= settings.ENEMY_FLASHING_DURATION/10:
                self.flashClock = pygame.time.get_ticks()

        # Attack state - move the enemy according to initial target
        if self.enemyState == 2:
            self.x += self.xVelocity
            self.y += self.yVelocity
            self.rect.x = int(self.x)
            self.rect.y = int(self.y)

        # Reset Enemy if it exits the screen
        if (self.rect.x > settings.SCREEN_WIDTH) or (self.rect.x < -settings.BLOCKSIZE*2) or (self.rect.y > settings.SCREEN_HEIGHT) or (self.rect.y < 0 - settings.BLOCKSIZE*2):
            self.image.fill(settings.CYAN)
            self.x = self.OriginalX
            self.rect.x = self.x
            self.enemyClock = pygame.time.get_ticks()
            self.enemyState = 0

        # Check for collision between enemy and player (flying)
        if (self.enemyState == 2) and (pygame.sprite.collide_rect(self,self.game.player)):
            # End game
            self.game.playing = False
            self.game.running = False


     