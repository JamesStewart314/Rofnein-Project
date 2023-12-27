import pygame

from typing import List, Union

from Constants import Game_Constants

pygame.init()


class Animation:
    def __init__(self, animation: list, animation_cooldown: Union[int, float],
                 coordinate_x: List[Union[int, float]] = 0, coordinate_y: List[Union[int, float]] = 0):

        self.animation = animation
        self.frame_index = 0
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.image = self.animation[self.frame_index]
        self.animation_length = len(self.animation)
        self.end_animation = False
        self.update_time = pygame.time.get_ticks()
        self.animation_cooldown = animation_cooldown

    def update(self):

        if not self.end_animation:

            self.image = self.animation[self.frame_index]

            if pygame.time.get_ticks() - self.update_time > Game_Constants.fade_death_cooldown:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1

            if self.frame_index >= self.animation_length:
                self.frame_index = self.animation_length
                self.end_animation = True

    def update_loop(self):

        self.image = self.animation[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > Game_Constants.fade_death_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            self.frame_index %= self.animation_length

    def draw(self, screen: object):
        if not self.end_animation:
            screen.blit(self.image, (self.coordinate_x, self.coordinate_y))
