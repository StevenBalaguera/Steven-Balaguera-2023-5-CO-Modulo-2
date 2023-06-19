import pygame
import random 
import os

from game.components.power_ups.shield import Shield
from game.components.power_ups.infinite_bullet import MaxBullet

from game.utils.constants import SPACESHIP_SHIELD, SPACESHIP_UPDATE, MUSIC_DIR, DEFAULT_TYPE



class PowerUpManager:
    MIN_TIME_POWER_UP = 5000
    MAX_TIME_POWER_UP = 10000

    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP)
        self.duration = random.randint(3, 5)

    def generate_effect(self):
        level_up_effect = pygame.mixer.Sound(os.path.join(MUSIC_DIR, "Music/hp-level-up-mario.mp3"))
        CANAL_3 = pygame.mixer.Channel(1)
        CANAL_3.play(level_up_effect)
        CANAL_3.set_volume(0.15)

    def generate_power_up(self):
        self.type_power = random.randint(0, 1)
        if self.type_power == 0:
            self.power_up = Shield()
            self.when_appears += random.randint(self.MIN_TIME_POWER_UP, self.MAX_TIME_POWER_UP) 
            self.power_ups.append(self.power_up)

        elif self.type_power == 1:
            self.power_up = MaxBullet()
            self.when_appears += random.randint(self.MIN_TIME_POWER_UP, self.MIN_TIME_POWER_UP) 
            self.power_ups.append(self.power_up)
            
    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if self.type_power == 0:
                if game.player.rect.colliderect(power_up):
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.set_image((65, 75), SPACESHIP_SHIELD)
                    self.generate_effect()
                    self.power_ups.remove(power_up)                

            elif self.type_power == 1:
                if game.player.rect.colliderect(power_up):
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.has_power_up = True
                    game.player.power_time_up = power_up.start_time + (self.duration * 1000)
                    game.player.type = "player_update"
                    game.player.set_image((65, 75), SPACESHIP_UPDATE)
                    self.generate_effect()
                    self.power_ups.remove(power_up)
                    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appears = random.randint(now + self.MIN_TIME_POWER_UP, now + self.MAX_TIME_POWER_UP)
        self.power_up = DEFAULT_TYPE