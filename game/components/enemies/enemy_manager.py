import random

from game.components.enemies.enemy import Enemy


class EnemyManager:
  def __init__(self):
    self.enemies = []
    
  def update(self, game):
    self.add_enemy()

    for enemy in self.enemies:
      enemy.update(self.enemies, game)
  
  def draw(self, screen):
    for enemy in self.enemies:
      enemy.draw(screen)
      
  def add_enemy(self):
    self.enemy_type = random.randint(1, 3)
    enemy_random = random.randint(1, 3)
    x_speed_random = random.randint(2, 6)
    y_speed_random = 2

    if self.enemy_type == 1:
      enemy = Enemy()
      enemy_2 = Enemy(enemy_random, x_speed_random, y_speed_random)
      enemy_3 = Enemy(enemy_random, x_speed_random, y_speed_random)
      enemy_4 = Enemy(enemy_random, x_speed_random, y_speed_random)

    elif self.enemy_type == 2:
      x_speed = 10
      y_speed = 2
      move_x_for = [1000, 2000]
      enemy = Enemy(self.enemy_type, x_speed, y_speed, move_x_for)
      enemy_2 = Enemy(enemy_random, x_speed_random, y_speed_random)
      enemy_3 = Enemy(enemy_random, x_speed_random, y_speed_random)
      enemy_4 = Enemy(enemy_random, x_speed_random, y_speed_random)
      
    else:
      x_speed = 5
      y_speed = 2
      move_x_for = [1000, 1200]
      enemy = Enemy(self.enemy_type, x_speed, y_speed, move_x_for)
      enemy_2 = Enemy(enemy_random, x_speed_random, y_speed_random)
      enemy_3 = Enemy(enemy_random, x_speed_random, y_speed_random)
      enemy_4 = Enemy(enemy_random, x_speed_random, y_speed_random)

    if len(self.enemies) < 1:
      self.enemies.append(enemy)
      self.enemies.append(enemy_2)
      self.enemies.append(enemy_3)
      self.enemies.append(enemy_4)
      
  def reset(self):
    self.enemies = []
    