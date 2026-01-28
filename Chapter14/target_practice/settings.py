class Settings:
    '''A class to store all settings for Target Practice.'''

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (11, 17, 38)

        # Ship settings
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (255, 255, 0)
        self.bullets_allowed = 3

        # Target settings
        self.target_height = 200
        self.target_width = 20
        self.target_color = (255, 0, 0)
        self.target_speed = 1.0

        # Misses
        self.miss_limit = 3