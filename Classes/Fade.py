import pygame

from typing import Union

from Constants import Game_Constants

pygame.init()


class Fade(pygame.sprite.Sprite):

    def __init__(self, fade_type: str, change_rate: Union[int, float] = Game_Constants.fade_transition_rate):

        assert fade_type in {"fade_in", "fade_out"}, f"Given fade type doesn't exist. Try these: " \
                                                     f'["fade_in", "fade_out"]'

        pygame.sprite.Sprite.__init__(self)
        self.fade_type = fade_type
        self.frame_index = 0
        self.change_rate = change_rate
        self.image = pygame.Surface((Game_Constants.Window_width, Game_Constants.Window_height)).convert()
        self.image.fill(Game_Constants.BLACK_COLOR)
        self.image.set_alpha(255) if fade_type == "fade_out" else self.image.set_alpha(0)
        self.end_fade = False

    def update(self):

        if (self.image.get_alpha() >= 255 and self.fade_type == "fade_in") or (self.image.get_alpha() <= 0 and self.fade_type == "fade_out"):
            self.end_fade = True

        if not self.end_fade:
            if self.fade_type == "fade_in":
                self.image.set_alpha(self.image.get_alpha() + self.change_rate)
            else:
                self.image.set_alpha(self.image.get_alpha() - self.change_rate)

    def restart(self):
        self.image.set_alpha(0) if self.fade_type == "fade_in" else self.image.set_alpha(255)
        self.end_fade = False

    def draw(self, screen: object):
        if not self.end_fade:
            screen.blit(self.image, (0, 0))
