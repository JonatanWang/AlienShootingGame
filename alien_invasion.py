import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # init game and create a screen object
    pygame.init()
    ai_settings = Settings()
    stats = GameStats(ai_settings)
    screen = pygame.display.set_mode((ai_settings.screen_width, 
    ai_settings.screen_height))
    scoreboard = Scoreboard(ai_settings, screen, stats)
    pygame.display.set_caption("Alien Invasion")
    
    # create Play button
    play_button = Button(ai_settings, screen, "PLAY")

    # create a ship
    ship = Ship(ai_settings, screen)

    # create a group of bullets
    bullets = Group()

    # create a group of aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # start the main loop of the game
    while True:

        # monitor keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, play_button, 
        ship, aliens, bullets, scoreboard)

        if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, stats, scoreboard, screen, ship, aliens, bullets)
                gf.update_aliens(ai_settings, scoreboard, stats, screen, ship, aliens, bullets)

        # update screen
        gf.update_screen(ai_settings, screen, stats, scoreboard, ship, 
        aliens, bullets, play_button)

run_game()