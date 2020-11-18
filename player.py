import pygame
import settings
import missile
import block
import bullet

class Player(pygame.sprite.Sprite):
    def __init__(self,game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game

        self.width = settings.BLOCKSIZE
        self.height = settings.BLOCKSIZE
        
        # Make out top-left corner the passed-in location
        self.image = pygame.Surface((self.width,self.height))
        self.image.fill((settings.PLAYER_COLOR))

        self.rect = self.image.get_rect()

        # Set initial player location
        self.rect.x = 0
        self.rect.y = 240 + settings.BLOCKSIZE/2

        # Player coordinates
        self.x = self.rect.x
        self.y = self.rect.y

        # Player presence in zone
        self.player_in_zone = False

    def update(self):
        # Check if player is inside the zone
        self.player_in_zone = pygame.sprite.collide_rect(self,self.game.zone)
        
        # Check for collision between player and blocks
        if pygame.sprite.spritecollide(self,self.game.blocks,True):
            self.bounce()
            # Create missile sprite if none exist
            if (len(self.game.missiles) == 0):
                # Add missile sprite if there are none already flying
                self.game.missile = missile.Missile(self.game,settings.BLUE,self.rect.y)
                self.game.missiles.add(self.game.missile)
                self.game.missile.missileState = 1
        
       # Check for collision between player and enemy (not flying)
        if (self.game.enemy.enemyState != 2):
            if pygame.sprite.collide_rect(self,self.game.enemy):
                # Create missile sprite if none exist
                if (len(self.game.missiles) == 0):
                    # Add missile sprite if there are none already flying
                    self.game.missile = missile.Missile(self.game,settings.BLUE,self.rect.y)
                    self.game.missiles.add(self.game.missile)
                    self.game.missile.missileState = 1
 
        # Read keyboard
        self.keys = pygame.key.get_pressed()
        # Update player position according to speed
        if self.keys[pygame.K_LEFT]:
            self.x -= settings.PLAYER_VELOCITY
            self.rect.x = int(self.x)
        if self.keys[pygame.K_RIGHT]:
            self.x += settings.PLAYER_VELOCITY
            self.rect.x = int(self.x)
        if self.keys[pygame.K_UP]:
            self.y -= settings.PLAYER_VELOCITY
            self.rect.y = self.y
        if self.keys[pygame.K_DOWN]:
            self.y += settings.PLAYER_VELOCITY
            self.rect.y = self.y
        # Fire pressed
        if self.keys[pygame.K_SPACE]:
            # Test if player is outside the zone
            if (not self.player_in_zone):
                # Launch missile if one is set
                if (len(self.game.missiles) != 0):
                    self.game.missile.missileState = 2
                # Create bullets if there is no missile set or flying
                if (len(self.game.missiles) == 0):
                    if (pygame.time.get_ticks() - settings.BULLET_LAUNCH_TIME >= settings.BULLET_DELAY):
                        self.game.bullet = bullet.Bullet(self.game,settings.GREEN,self.rect.x,self.rect.y)
                        self.game.bullets.add(self.game.bullet)
        
        # Make sure the player don't exit the screen
        if self.rect.x < 0:
            self.x = 0
            self.rect.x = self.x
        if self.rect.x > settings.SCREEN_WIDTH-settings.BLOCKSIZE:
            self.x = settings.SCREEN_WIDTH-settings.BLOCKSIZE
            self.rect.x = self.x
        # If the the players to the bottom or top, make it appears at the opposite
        if self.rect.y < 0:
            self.y = settings.SCREEN_HEIGHT-settings.BLOCKSIZE
            self.rect.y = self.y
        if self.rect.y > settings.SCREEN_HEIGHT-settings.BLOCKSIZE:
            self.y = 0
            self.rect.y = self.y

    def bounce(self):
        # blocks repels player in y direction after collision
        self.x -= settings.BLOCKSIZE
        self.rect.x = int(self.x)    