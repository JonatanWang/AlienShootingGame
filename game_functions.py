import sys
import pygame

def check_events():
    """reponse to key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # move ship to right
                ship.rect.centerx += 1

def update_screen(ai_settings, screen, ship):
    """update images on the screen & switch to the new screen"""
    # re-paint the screen within each loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # enable the visualbility of the current screen
    pygame.display.flip()

