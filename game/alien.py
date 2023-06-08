import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    # a class representing a single alien
    def __init__(self, ai_game):
        # initializes the alien and sets its initial position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # uploading an alien image and assigning a rect attribute
        self.image = pygame.image.load('game/resources/images/alien_green.bmp')
        self.rect = self.image.get_rect()

        # each new alien appears in the upper left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # maintaining the exact horizontal position of the alien
        self.x = float(self.rect.x)

    def check_edges(self):
        # returns true if the alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # moves alien to the right or to the left
        self.x += (self.settings.alien_speed_factor *
                   self.settings.fleet_direction)
        self.rect.x = self.x
