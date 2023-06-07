class GameStats():
    # statistics tracking for Alien Invasion game

    def __init__(self, ai_game):
        # initializes statistics
        self.settings = ai_game.settings
        self.reset_stats()

        # the game starts in inactive state
        self.game_active = False

        # the record should not be reset
        self.high_score = 0
    def reset_stats(self):
        # initializes statistics that change during the game
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

