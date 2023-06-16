import pygame

from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, FONT_STYLE
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu.menu import Menu
from game.components.menu.menu_scores import MenuScores


class Game:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu_score = MenuScores(self.screen)
        #self.menu = Menu("Press Any Key To Start....", self.screen, self.HALF_SCREEN_WIDTH , self.HALF_SCREEN_HEIGHT)
        #self.score_menu = Menu(f"Your Score: {self.menu_score.score}", self.screen, self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)
        #self.deads_menu = Menu(f"Your deads: {self.menu_score.death_count}", self.screen, self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)
        #self.high_score_menu = Menu(f"Highest Score: {max(self.menu_score.list_scores)}", self.screen, self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)
        self.running = False


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu_game() 

        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.menu_score.score = 0

        for enemy in self.enemy_manager.enemies:
            self.enemy_manager.enemies.remove(enemy)

        for enemy_bullet in self.bullet_manager.enemy_bullets:
            self.bullet_manager.enemy_bullets.remove(enemy_bullet)
        # Game loop: events - update - draw
        
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.menu_score.update()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.menu_score.draw_score(self.screen)
        pygame.display.update()
        #pygame.display.flip()
        

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu_game(self):
        self.menu_score.show_menu(self.screen)
        self.menu_score.menu.update(self)
        self.menu_score.score_menu.update(self)
        self.menu_score.deads_menu.update(self)
        self.menu_score.high_score_menu.update(self)





