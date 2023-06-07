import pygame.font


class Button():
    def __init__(self, ai_game, msg):
        # initializes the button attributes
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # assignment of sizes and properties of buttons
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # building a rect button object and aligning it to the center of the screen
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # the button message is created only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # converts the msg to a rectangle and aligns the text to the center
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # displaying an empty button and displaying a message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


