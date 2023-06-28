
import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/ENEMY_3.png"))

INFINITE_BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_3.png"))
BULLET_TYPE = 'bullet'
GIFT = pygame.image.load(os.path.join(IMG_DIR, "Bullet/regalo_power.png"))

SPACESHIP_UPDATE = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_power_up.png"))
MENU_IMAGE = pygame.image.load(os.path.join(IMG_DIR, "Other/imagen_menu.png"))

SPACESHIP_MENU = pygame.image.load(os.path.join(IMG_DIR, "Animation_menu/spaceship_menu.png"))
SPACESHIP_MENU_2 = pygame.image.load(os.path.join(IMG_DIR, "Animation_menu/spaceship_menu2.png"))
IMAGE_LIST = []
for image in range(1, 11):
    IMAGE_LIST.append(pygame.image.load(os.path.join(IMG_DIR, f"explotion/explotion_{image}.png")))
FONT_STYLE = 'freesansbold.ttf'
