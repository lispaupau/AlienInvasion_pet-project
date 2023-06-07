import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    # class for control bullets

    def __init__(self, ai_game):
        # create object of bullets in ship position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet in pisition (0,0)
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # the position of the projectile is stored in real form
        self.y = float(self.rect.y)

    def update(self):
        # moves the projectile up the screen
        # updating the position of the projectile in real format
        self.y -= self.settings.bullet_speed_factor
        # updating the position of the rectangle
        self.rect.y = self.y

    def draw_bullet(self):
        # launching a projectile on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
