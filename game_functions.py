import sys
from time import sleep
import pygame

from pygame.locals import *
from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """reponse to keydown"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(bullets, ai_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit(0)

def fire_bullets(bullets, ai_settings, screen, ship):
    """if bullets limit is not reached, fire a bullet"""

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """response to keyup"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, 
    ship, aliens, bullets, scoreboard):
    """reponse to key and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_pay_button(ai_settings, screen, stats, ship, 
            aliens, bullets, play_button, scoreboard, mouse_x, mouse_y)

def check_pay_button(ai_settings, screen, stats, play_button, 
    ship, aliens, bullets, scoreboard, mouse_x, mouse_y):
    """start game when play button clicked"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game settings
        ai_settings.initialize_dynamic_settings()

        # hide cursor
        pygame.mouse.set_visible(False)

        # reset stats of game
        stats.reset_stats()
        stats.game_active = True

        # reset scoreboard
        scoreboard.prep_score()
        scoreboard.prep_high_score()
        scoreboard.prep_level()
        scoreboard.prep_ships()

        # empty alien list & bullets list
        aliens.empty()
        bullets.empty()

        # create a new fleet of aliens & place them in the middle
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, screen, stats, scoreboard, 
    ship, aliens, bullets, play_button):
    """update images on the screen & switch to the new screen"""
    # re-paint the screen within each loop
    screen.fill(ai_settings.bg_color)
    scoreboard.show_score()

    # re-paint all bullets after ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()

    # enable the visualbility of the current screen
    pygame.display.flip()

def update_bullets(ai_settings, stats, scoreboard, 
    screen, ship, aliens, bullets):
    """update positions of bullets & delete the vanished bullets"""
    # update positions of bullets
    bullets.update()

    # delete the vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # check if any bullet hits an alien
    # if yes, delete the bullet and alien
    check_bullet_alien_collisions(bullets, stats, scoreboard, aliens, ai_settings, screen, ship)

def check_bullet_alien_collisions(bullets, stats, scoreboard, 
    aliens, ai_settings, screen, ship):
    """response collisions of bullet and alien"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, 
        True, True)
    
    if collisions:
        for aliens in collisions.value():
            stats.score += ai_settings.alien_points * len(aliens)
            scoreboard.prep_score()
        check_high_score(stats, scoreboard)

    if len(aliens) == 0:
        # delete all bullets and create a new fleet of aliens
        bullets.empty()
        ai_settings.increase_speed()

        # increase level
        stats.level += 1
        scoreboard.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def create_fleet(ai_settings, screen, ship, aliens):
    """create alien fleet"""
    # create an alien and calculate how many aliens can be place in a row
    # the distance between two aliens is the width of an alien
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    print("number_alien = " + str(number_aliens_x) 
    + " number_rows = " + str(number_rows))

    # create first row of aliens
    for row_number in range(number_rows):
        # create an alien and add it in the current row
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and add it in the current row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
        
def get_number_aliens_x(ai_settings, alien_width):
    """calcualte how many aliens in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """calculate how many rows of aliens can be place in  the screen"""
    available_space_y = (ai_settings.screen_height - 3 * (alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    
    return number_rows

def ship_hit(ai_settings, stats, scoreboard, screen, ship, aliens, bullets):
    """response to the ship hits"""
    if stats.ships_left > 0:
        # reduce ships_left by 1
        stats.ships_left -= 1

        # update scoreboard
        scoreboard.prep_ships()

        # empty aliens list and bullets list
        aliens.empty()
        bullets.empty()

        # create a new fleet of aliens & place them at the bottom of screen
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings, stats, scoreboard, screen, ship, aliens, bullets):
    """check if an alien at edge & adjust positions of all aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check collision between aliens and ship
    if pygame.sprite.spritecollideany(ship, aliens):
        print("ship hit")
        ship_hit(ai_settings, stats, scoreboard, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, scoreboard, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
    """take measures if an alien reaches edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            check_fleet_direction(ai_settings, aliens)
            break

def check_fleet_direction(ai_settings, aliens):
    """move the fleet of aliens downwards & change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, scoreboard, screen, 
    ship, aliens, bullets):
    """check if any alien reaches the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # hanle it as to handle ships
            ship_hit(ai_settings, stats, scoreboard, screen, 
            ship, aliens, bullets)
            break

def check_high_score(stats, scoreboard):
    """check if new highest score exists"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        scoreboard.prep_high_score
