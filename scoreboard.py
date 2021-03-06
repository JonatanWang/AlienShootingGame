import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """class to show the score info"""
    def __init__(self, ai_settings, screen, stats):
        """init properties about score"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # show the font about score
        self.text_color = 30, 30, 30
        self.font = pygame.font.SysFont(None, 48)

        # prepare init score image
        self.prep_score()

        # save the highest score
        self.prep_high_score()

        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """convert score to a rendered image"""
        rounded_sccore = int(round(self.stats.score, -1))
        score_str ="{:,}".format(rounded_sccore)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # place score at the upper right corner of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """save the higheset score to rendered image"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # place highest score in the middle of top screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.high_score_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """convert level to rendered image"""
        self.level_image = self.font.render(str(self.stats.level), 
        True, self.text_color, self.ai_settings.bg_color)
        #show level under score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.level_rect.right
        self.level_rect.top = self.level_rect.bottom + 10

    def prep_ships(self):
        """show the remained ships"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """show score, level & higheset score in the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # render ship
        self.ships.draw(self.screen)