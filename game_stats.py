class GameStats():
    """track the stat info of the game"""
    def __init__(self, ai_settings):
        """init stat info"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """init stat info which can be changed during the game"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
