import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_STYLE, ICON


class MenuScores:
    def __init__(self):
        self.score = 0
        self.death_count = 0

    def update(self):
        pygame.display.update()
    
    def draw(self):
        pass

    def update_score(self):
        self.score += 1

    def draw_score(self, screen):
        font =pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f'Score: {self.score}', True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        screen.blit(text, text_rect)
