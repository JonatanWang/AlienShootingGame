import pygame

class Ship():
    
    def __init__(self, screen):
        ''''init ship and set position'''
        self.screen = screen

        # load ship image and get its rectangle
        self.image = pygame.image.load('img/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set each new ship at the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """render ship at the appointed position"""
        self.screen.blit(self.image, self.rect)