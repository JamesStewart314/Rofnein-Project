import pygame
import math

from Constants import Game_Constants
from typing import Union

pygame.init()


class FloatingText(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float], text_sprite: object,
                 amplitude: Union[None, int, float] = None, speed: Union[None, int, float] = None):

        pygame.sprite.Sprite.__init__(self)
        self.image = text_sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (coordinate_x, coordinate_y)
        self.original_x, self.original_y = self.rect.x, self.rect.y
        self.counter = pygame.time.get_ticks()
        self.oscilation_speed = Game_Constants.floating_text_oscilation_speed if not speed else speed
        self.oscilation_position = 0
        self.oscilation_amplitude = Game_Constants.text_oscilation_amplitude if not amplitude else amplitude
        self.update_time = pygame.time.get_ticks()

    def update(self) -> None:

        # Move Damage Text Up :
        self.rect.y = self.original_y + self.oscilation_amplitude * math.sin(self.oscilation_position)

        self.oscilation_position %= 2 * math.pi

        if pygame.time.get_ticks() - self.update_time > Game_Constants.floating_text_oscilation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.oscilation_position += self.oscilation_speed

    def draw(self, screen: object) -> None:
        screen.blit(self.image, (self.rect.x, self.rect.y))




