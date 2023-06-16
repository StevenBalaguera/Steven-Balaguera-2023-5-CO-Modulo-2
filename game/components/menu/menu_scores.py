import pygame
from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, FONT_STYLE, ICON
from game.components.menu.menu import Menu

class MenuScores:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    def __init__(self, screen):
        self.score = 0
        self.death_count = 0
        self.list_scores = [0]
        self.score_player = []
        self.menu = Menu("Press Any Key To Start....", screen, self.HALF_SCREEN_WIDTH , self.HALF_SCREEN_HEIGHT)
        self.score_menu = Menu(f"Your Score: {self.score}", screen, self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)
        self.deads_menu = Menu(f"Your deads: {self.death_count}", screen, self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        self.high_score_menu = Menu(f"Highest Score: {max(self.list_scores)}", screen, self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)


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

    def list_of_scores(self):
        self.list_scores.append(self.score)
        self.score_player.append(self.score)

    def show_menu(self, screen):
        self.list_of_scores()
        self.menu.reset(screen)
        if self.death_count > 0:
            self.menu.update_message("Game Over", self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)
            self.deads_menu.update_message(f"Your Deads: {self.death_count}", self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
            self.score_menu.update_message(f"Your Score: {self.score_player.pop()}", self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)
            self.high_score_menu.update_message(f"Highest Score: {max(self.list_scores)}", self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)

        self.menu.draw(screen)
        self.score_menu.draw(screen)
        self.deads_menu.draw(screen)
        self.high_score_menu.draw(screen)

        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        icon = pygame.transform.scale(ICON, (80, 120))
        screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))
