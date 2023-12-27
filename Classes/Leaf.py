import pygame
import math

from Assets import Background_Images
from Constants import Game_Constants
from typing import Union

pygame.init()


class Leaf(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float], leaf_sprite: object,
                 amplitude: Union[int, float] = Game_Constants.text_oscilation_amplitude,
                 speed: Union[int, float] = Game_Constants.floating_text_oscilation_speed):

        pygame.sprite.Sprite.__init__(self)
        self.image = leaf_sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = (coordinate_x, coordinate_y)
        self.original_x, self.original_y = self.rect.x, self.rect.y
        self.counter = pygame.time.get_ticks()
        self.oscilation_speed = speed
        self.horizontal_leaf_speed = Game_Constants.horizontal_leaf_speed
        self.oscilation_position = 0
        self.angle = 0
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        self.angle_change_speed = 0.5
        self.text_showing_time = Game_Constants.level_text_time
        self.oscilation_amplitude = amplitude
        self.update_time = pygame.time.get_ticks()

        self.leaf_trace = []

    def update(self) -> None:

        # Move Leaf Towards the Screen :
        self.rect.y = self.original_y + self.oscilation_amplitude * math.sin(self.oscilation_position)

        self.angle -= self.angle_change_speed

        self.oscilation_position %= 2 * math.pi
        self.angle %= 360

        if pygame.time.get_ticks() - self.update_time > Game_Constants.Board_Leaf_Cooldown:
            self.update_time = pygame.time.get_ticks()
            self.oscilation_position += self.oscilation_speed
            self.rect.x += self.horizontal_leaf_speed

        if self.rect.bottom < 0 or self.rect.top > Game_Constants.Window_height or \
                self.rect.left > Game_Constants.Window_width:
            self.kill()

        leaf_trace_aux = Background_Images.Gray_Square.copy()
        leaf_trace_aux_rect = leaf_trace_aux.get_rect()
        leaf_trace_aux_rect.center = self.rect.centerx, self.rect.centery

        self.leaf_trace.append([leaf_trace_aux, leaf_trace_aux_rect])

        for leaf_trace_aux in self.leaf_trace:
            leaf_trace_aux[0].set_alpha(leaf_trace_aux[0].get_alpha() - 20)

            if leaf_trace_aux[0].get_alpha() <= 0:
                self.leaf_trace.remove(leaf_trace_aux)

    def draw(self, screen: object) -> None:
        for leaf_trace in self.leaf_trace:
            screen.blit(leaf_trace[0], (leaf_trace[1].x, leaf_trace[1].y))

        self.rotated_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(self.rotated_image, (self.rect.x, self.rect.y))





