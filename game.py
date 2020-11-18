import pygame
import settings
import player
import block
import missile
import bullet
import enemy
import probe
import zone

class Game:
    def __init__(self):
        # Initialise game code
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.playing = True

    def new(self):
        # Start a new game
        # Set sprite groups
        self.players = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        self.probes = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Add Player Sprite
        self.player = player.Player(self)
        self.players.add(self.player)

        # Add Block Sprites that will form the wall
        for i in range(0,len(settings.WALL_POSITION)):
            block_iter = block.Block(settings.RED,settings.WALL_POSITION[i][0]*16,settings.WALL_POSITION[i][1]*16)
            self.blocks.add(block_iter)

        # Add Enemy Sprite (behind wall)
        self.enemy = enemy.Enemy(self,settings.CYAN,settings.ENEMY_POSITION[0]*16,settings.ENEMY_POSITION[1]*16)
        self.enemies.add(self.enemy)

        # Add Zone Sprite
        self.zone = zone.Zone()
        self.zones.add(self.zone)

        # Add Probe sprite
        self.probe = probe.Probe(self,settings.YELLOW,settings.PROBE_POSITION[0]*16,settings.PROBE_POSITION[1]*16)
        self.probes.add(self.probe)

        # Run Game Loop
        self.run()

    def run(self):
        # Game Loop Code
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        # Game Loop Events Handler
        for event in pygame.event.get():
            # CHeck for closing the window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def update(self):
        # Game Loop Update Method
        self.blocks.update()
        self.players.update()
        self.missiles.update()
        self.probes.update()
        self.bullets.update()
        self.enemies.update()

    def draw(self):
        # Game Loop Draw Screen
        self.screen.fill(settings.BLACK)

        # Draw all sprites
        self.zones.draw(self.screen)
        self.blocks.draw(self.screen)
        self.enemies.draw(self.screen)
        self.probes.draw(self.screen)
        self.bullets.draw(self.screen)
        self.missiles.draw(self.screen)
        self.players.draw(self.screen)

        # Update screen
        pygame.display.update()

    def showStartScreen(self):
        # Show the start screen of the game
        pass

    def showGameOverScreen():
        # Show the Game Over screen
        pass
