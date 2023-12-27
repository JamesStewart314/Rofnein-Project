import pygame
import math

from Constants import Game_Constants
from typing import Union

pygame.init()


class FloatingText(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float], text_sprite: object,
                 amplitude: Union[int, float] = Game_Constants.text_oscilation_amplitude,
                 speed: Union[int, float] = Game_Constants.floating_text_oscilation_speed):

        pygame.sprite.Sprite.__init__(self)
        self.image = text_sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (coordinate_x, coordinate_y)
        self.original_x, self.original_y = self.rect.x, self.rect.y
        self.counter = pygame.time.get_ticks()
        self.oscilation_speed = speed
        self.oscilation_position = 0
        self.text_showing_time = Game_Constants.level_text_time
        self.oscilation_amplitude = amplitude
        self.update_time = pygame.time.get_ticks()

        self.opacity_change_rate = 5
        self.fade_in = True
        self.fade_out = False
        self.image.set_alpha(0)
        self.do = True

    def update(self) -> None:
        if self.do:
            if self.fade_in:
                self.image.set_alpha(self.image.get_alpha() + self.opacity_change_rate)

                if self.image.get_alpha() >= 255:
                    self.fade_in = False
                    self.opacity_time = pygame.time.get_ticks()

            if not self.fade_in and pygame.time.get_ticks() - self.opacity_time >= self.text_showing_time:
                self.fade_out = True

            if self.fade_out:
                self.image.set_alpha(self.image.get_alpha() - self.opacity_change_rate)

                if self.image.get_alpha() <= 0:
                    self.fade_in = True
                    self.fade_out = False
                    self.do = False

            # Move Text Up and Down :
            self.rect.y = self.original_y + self.oscilation_amplitude * math.sin(self.oscilation_position)

            self.oscilation_position %= 2 * math.pi

            if pygame.time.get_ticks() - self.update_time > Game_Constants.floating_text_oscilation_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.oscilation_position += self.oscilation_speed

    def update_2(self) -> None:

        if self.fade_in:
            self.image.set_alpha(self.image.get_alpha() + self.opacity_change_rate)

            if self.image.get_alpha() >= 255:
                self.fade_in = False

        if self.fade_out:
            self.image.set_alpha(self.image.get_alpha() - self.opacity_change_rate)

            if self.image.get_alpha() <= 0:
                self.fade_in = True
                self.fade_out = False

        # Move Text Up and Down :
        self.rect.y = self.original_y + self.oscilation_amplitude * math.sin(self.oscilation_position)

        #self.oscilation_position %= 2 * math.pi

        if pygame.time.get_ticks() - self.update_time > Game_Constants.floating_text_oscilation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.oscilation_position += self.oscilation_speed

    def draw(self, screen: object) -> None:
        if self.do:
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def restart(self) -> None:
        self.do = True
        self.fade_in = True
        self.fade_out = False

        self.image.set_alpha(0)




