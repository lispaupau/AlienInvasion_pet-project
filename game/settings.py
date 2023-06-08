class Settings:
    # class to collection all settings for game Alien Invasion

    def __init__(self):
        # initializes static game settings
        # init game settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (20, 20, 20)

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (143, 0, 255)
        self.bullets_allowed = 3

        # aliens settings
        self.fleet_drop_speed = 10

        # game acceleration rate
        self.speedup_scale = 1.1
        # alien value growth rate
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # initializes settings that change during the game
        self.ship_speed_factor = 3.0
        self.bullet_speed_factor = 6.0
        self.alien_speed_factor = 1.5

        # fleet_direction = 1 movement points to the right; -1 - to the left
        self.fleet_direction = 1

        # scoring
        self.alien_points = 50

    def increase_speed(self):
        # increases alien speed and cost settings
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)