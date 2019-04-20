import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class representing an indivisual alien"""

    def __init__(self, ai_settings, screen):
        """init an alien and set start position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load image of alien and set rect property
        self.image = pygame.image.load('img/ufo.bmp')
        self.rect = self.image.get_rect()

        # each alien appears first on the up-left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # save the position of an alien
        self.x = float(self.rect.x)

    def blitme(self):
        """render an alien at a position"""
        self.screen.blit(self.image, self.rect)     

    def update(self):
        """move aliens to the right side"""
        self.x += (self.ai_settings.alien_speed_factor * 
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """if at the edge of screen, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True  