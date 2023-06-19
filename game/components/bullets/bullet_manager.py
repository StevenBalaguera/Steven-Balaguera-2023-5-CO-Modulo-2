import pygame
import os

from game.utils.constants import SHIELD_TYPE, MUSIC_DIR

class BulletManager:
  def __init__(self):
    self.bullets = []
    self.enemy_bullets = []

  def music_effect(self):
    kill_enemy_effect = pygame.mixer.Sound(os.path.join(MUSIC_DIR, "Music/Minecraft_kill_enemy.mp3"))
    canal_1 = pygame.mixer.Channel(1)
    canal_1.play(kill_enemy_effect)
    canal_1.set_volume(0.15) 

  def effect_spaceship_kill(self):
    kill_spaceship = pygame.mixer.Sound(os.path.join(MUSIC_DIR, "Music/villager.mp3"))
    canal_2 = pygame.mixer.Channel(2)
    canal_2.play(kill_spaceship)
    canal_2.set_volume(0.15)

  def enemy_laser_effect(self):
    enemy_laser = pygame.mixer.Sound(os.path.join(MUSIC_DIR, "Music/Enemy_laser.mp3"))
    canal_3 = pygame.mixer.Channel(3)
    canal_3.play(enemy_laser)
    canal_3.set_volume(0.15)

  def shield_effect(self):
    shield = pygame.mixer.Sound(os.path.join(MUSIC_DIR, "Music/shield_effect.mp3"))
    canal_4 = pygame.mixer.Channel(4)
    canal_4.play(shield)
    canal_4.set_volume(0.15)
    
  def update(self, game):
    for bullet in self.bullets:
      bullet.update(self.bullets)

      for enemy in game.enemy_manager.enemies:
        if (bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player') or (bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player_update'):
            game.enemy_manager.enemies.remove(enemy)
            self.bullets.remove(bullet)
            game.score.update()
            self.music_effect()

    for bullet in self.enemy_bullets:
      bullet.update(self.enemy_bullets)
      
      if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
        self.enemy_bullets.remove(bullet)
        if game.player.power_up_type == SHIELD_TYPE:
          self.shield_effect()

        if game.player.power_up_type != SHIELD_TYPE:
          self.effect_spaceship_kill()
          game.death_count.update()
          game.playing = False
          pygame.time.delay(1000)
          break
  
  def draw(self, screen):
    for bullet in self.enemy_bullets:
      bullet.draw(screen)
    
    for bullet in self.bullets:
      bullet.draw(screen)
      
  def add_bullet(self, bullet):
    if bullet.owner == 'player' and len(self.bullets) < 3:
      self.bullets.append(bullet)
      self.enemy_laser_effect()
    
    elif bullet.owner == 'enemy' and len(self.enemy_bullets) < 2:
      self.enemy_bullets.append(bullet)
      self.enemy_laser_effect()

    elif bullet.owner == 'player_update' and len(self.bullets) < 10:
      self.bullets.append(bullet)
    
  def reset(self):
    self.bullets = []
    self.enemy_bullets = []