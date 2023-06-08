import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    # class for control the ship

    def __init__(self, ai_game):
        # init ship and get started position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load image ship and get rectangle
        self.image = pygame.image.load('game/resources/images/ship.bmp')
        self.rect = self.image.get_rect()
        # each new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # saving the real coordinate of the center of ship
        self.x = float(self.rect.x)
        # move flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # updates the position of the ship based on the flag
        # updates attribute x object ship, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed_factor
        # update attribute rect on base atribute x
        self.rect.x = self.x

    def blitme(self):
        # draws the ship at the current position
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        # places the ship in the center of the bottom side
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
