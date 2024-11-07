SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

THEME_MAIN_COLOR = WHITE
THEME_SECONDARY_COLOR = BLACK

BACKGROUND_COLOR = THEME_MAIN_COLOR
TEXT_COLOR = THEME_SECONDARY_COLOR

# Defense line
DEFENSE_LINE_WIDTH = 25
DEFENSE_LINE_POS_X = 150
DEFENSE_LINE_COLOR = THEME_SECONDARY_COLOR

# Player health point
HEALTH_WIDTH = 30
HEALTH_HEIGHT = 30
HEALTH_POS_X = SCREEN_WIDTH - 50
HEALTH_POS_Y = 50 - HEALTH_HEIGHT
HEALTH_COLOR = RED

# Player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
INITIAL_PLAYER_POS_X = 25
INITIAL_PLAYER_POS_Y = SCREEN_HEIGHT / 2
PLAYER_COLOR = (51, 51, 51)
PLAYER_SPEED = 5
PLAYER_HEALTH = 3

# Projectile
PROJECTILE_SPEED = 8
PROJECTILE_DAMAGE = 1
INITIAL_PROJECTILE_COOLDOWN = 750 # milliseconds
projectile_cooldown = INITIAL_PROJECTILE_COOLDOWN
PROJECTILE_WIDTH = 20
PROJECTILE_HEIGHT = 10
PROJECTILE_COLOR = PLAYER_COLOR

# Enemy A
ENEMY_A_WIDTH = 50
ENEMY_A_HEIGHT = 50
ENEMY_A_COLOR = RED
ENEMY_A_SPEED = 1
ENEMY_A_HEALTH = 2

# Enemy B
ENEMY_B_WIDTH = 60
ENEMY_B_HEIGHT = 60
ENEMY_B_COLOR = BLUE
ENEMY_B_SPEED = 1.75
ENEMY_B_HEALTH = 1

# Boss
BOSS_WIDTH = 250
BOSS_HEIGHT = 250
BOSS_COLOR = (87, 8, 97) # Deep purple
BOSS_SPEED = 0.5
BOSS_HEALTH = 50
BOSS_WAVE = 20

# Entity border
BORDER_COLOR = THEME_SECONDARY_COLOR