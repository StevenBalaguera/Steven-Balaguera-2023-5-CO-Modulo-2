import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    X_POS_LIST = list(range(50, 1100, 50))
    Y_POS = 20
    SPEED_X = 5
    SPEED_Y = 4
    MOV_X = { 0: 'left', 1: 'right'}
    IMAGE_DICT = { 0: ENEMY_1, 1: ENEMY_2}

    def __init__(self):
        self.random_image = self.IMAGE_DICT[(random.randint(0, 1))]
        self.image = pygame.transform.scale(self.random_image, (self.ENEMY_WIDTH, self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[(random.randint(0, 20))]
        self.rect.y = self.Y_POS
        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.move_x_player_2 = 8
        self.move_y_player_2 = 3
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30, 50)


    def update(self, ships, game):
        if self.random_image == ENEMY_2:
            self.speed_y = self.SPEED_Y + self.move_y_player_2
            self.speed_x = self.SPEED_X + self.move_x_player_2
            self.move_x_for = random.randint(20, 50)

        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x  
            self.change_movement_x()  
        
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)  

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0

    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
        self.shooting_time += random.randint(30, 50)