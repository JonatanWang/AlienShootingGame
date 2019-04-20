import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class to manange the bullets fired by the ship"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the position of the ship"""
        super().__init__()
        self.screen = screen

        # create a rectangle representing a bullet at (0, 0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # save bullet position by float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullet upwards"""
        # update the float representing the position of the bullet
        self.y -= self.speed_factor
        # update the rect position of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """render bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)