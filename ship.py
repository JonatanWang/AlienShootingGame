import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        ''''init ship and set position'''
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and get its rectangle
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust position of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # update rect object based on self.center
        self.rect.centerx = self.center

    def blitme(self):
        """render ship at the appointed position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """place the ship at the middle of screen"""
        self.center = self.screen_rect.centerx