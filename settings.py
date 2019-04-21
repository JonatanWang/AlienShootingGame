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
        self.fleet_drop_speed = 10

        # fleet_direction 1 ->, -1 <-
        self.fleet_direction = 1

        # game acceloration speed
        self.speedup_scale = 1.1

        # score speedup
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """init settings properties"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction == 1 -> right, or == -1 -> left
        self.fleet_direction = 1

        # score
        self.alien_points = 50

    def increase_speed(self):
        """increase speed setting"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
