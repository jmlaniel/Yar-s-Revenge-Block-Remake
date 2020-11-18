# Game options and Settings
TITLE = "Yar's Revenge Remake"
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 60

# Color constants
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
PLAYER_COLOR = (200,174,245)

# Block Settings
BLOCKSIZE = 16

# Player Settings
PLAYER_VELOCITY = 6

# Missile Settings
MISSILE_VELOCITY = 3

# Bullet Settings
BULLET_VELOCITY = 4
BULLET_LAUNCH_TIME = 0
BULLET_DELAY = 500                  # In ms

# Enemy Settings
ENEMY_POSITION = [37,14]
ENEMY_DELAY = 1000                  # In ms
ENEMY_FLASHING_DURATION = 5000      # In ms
ENEMY_VELOCITY = 5

# Probe Settings
PROBE_POSITION = [37,14]
PROBE_VELOCITY = 0.5

# Wall Settings
WALL_AMPLITUDE = 40
WALL_FREQUENCY = 0.5

# The coordinates are for the blocks
# x and y are obtained by multiplying by blocksize(16)
WALL_POSITION = [[39,6],[39,7],[39,8],[39,21],[39,22],[39,23],\
    [38,6],[38,7],[38,8],[38,9],[38,20],[38,21],[38,22],[38,23],\
    [37,6],[37,7],[37,8],[37,9],[37,10],[37,19],[37,20],[37,21],[37,22],[37,23],\
    [36,6],[36,7],[36,8],[36,9],[36,10],[36,11],[36,18],[36,19],[36,20],[36,21],[36,22],[36,23],\
    [35,6],[35,7],[35,8],[35,9],[35,10],[35,11],[35,12],[35,17],[35,18],[35,19],[35,20],[35,21],[35,22],[35,23],\
    [34,7],[34,8],[34,9],[34,10],[34,11],[34,12],[34,13],[34,14],[34,15],[34,16],[34,17],[34,18],[34,19],[34,20],[34,21],[34,22],\
    [33,8],[33,9],[33,10],[33,11],[33,12],[33,13],[33,14],[33,15],[33,16],[33,17],[33,18],[33,19],[33,20],[33,21],\
    [32,9],[32,10],[32,11],[32,12],[32,13],[32,14],[32,15],[32,16],[32,17],[32,18],[32,19],[32,20],\
    [31,10],[31,11],[31,12],[31,13],[31,14],[31,15],[31,16],[31,17],[31,18],[31,19]\
           ]
