import pygame

from game.utils.constants import FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, MENU_IMAGE

class Menu:
  HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
  HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2

  def __init__(self, screen):
    screen.fill((0, 25, 51))
    self.font = pygame.font.Font(FONT_STYLE, 30)
    self.image = pygame.transform.scale(MENU_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
  
  def update(self, game):
    pygame.display.update()
    
    self.handle_events_on_menu(game)
  
  def draw(self, screen, message, x = HALF_SCREEN_WIDTH, y = HALF_SCREEN_HEIGHT, color = (211, 84, 0)):
    text = self.font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)
    
  def handle_events_on_menu(self, game):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game.running = False
        game.playing = False
      elif event.type == pygame.KEYDOWN:
        game.run()
        
  def reset(self, screen):
    screen.blit(self.image, (0, 0))
    
  def update_message(self, message):
    self.text = self.font.render(message, True, (255, 255, 255))
    self.text_rect = self.text.get_rect()
    self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
        