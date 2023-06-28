import pygame
from pygame.sprite import Sprite
from game.utils.constants import IMAGE_LIST, SCREEN_WIDTH, SCREEN_HEIGHT

class Explotion(Sprite):
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    SIZE_WIDTH = 70
    SIZE_HEIGHT = 70
    def __init__(self):
        self.image = pygame.transform.scale(IMAGE_LIST[0], (self.SIZE_WIDTH, self.SIZE_HEIGHT))
        self.rect = self.image.get_rect()
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self, screen):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            if self.frame != len(IMAGE_LIST) - 1:
                self.frame += 1
            self.image = pygame.transform.scale(IMAGE_LIST[self.frame], (self.SIZE_WIDTH, self.SIZE_HEIGHT))
            self.rect = self.image.get_rect()
            screen.blit(self.image, (self.HALF_SCREEN_WIDTH - 150, self.HALF_SCREEN_HEIGHT - 180))
            screen.blit(self.image, (self.HALF_SCREEN_WIDTH + 60, self.HALF_SCREEN_HEIGHT - 180))



            