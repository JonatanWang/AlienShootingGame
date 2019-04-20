class Settings():

    '''save all the settings'''

    def __init__(self):
        '''init settings of the game'''
        # screen settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (111, 210, 219)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 10

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 100
        # fleet_direction 1 ->, -1 <-
        self.fleet_direction = 1
        
        