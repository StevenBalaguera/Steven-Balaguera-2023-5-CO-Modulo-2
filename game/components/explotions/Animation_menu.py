import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP_MENU, SPACESHIP_MENU_2, SCREEN_WIDTH, SCREEN_HEIGHT

class Animation(Sprite):
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    SIZE_WIDTH = 120
    SIZE_HEIGHT = 120
    def __init__(self, image, x_pos):
        self.image = pygame.transform.scale(image, (self.SIZE_WIDTH, self.SIZE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = self.HALF_SCREEN_HEIGHT + 150

    def draw_image(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        self.rect.y -= 10
        if self.rect.y == 0 - self.SIZE_HEIGHT:
            self.reset()

    def reset(self):
        self.rect.y = self.HALF_SCREEN_HEIGHT + 150
        
        