import pygame
import math
import random

from typing import Union, Tuple

import Assets.Weapon_Images

from Assets import Sound_Effects
from Constants import Game_Constants
from MyFunctions import MyFunctions
from Classes import Character
from Classes import Weapon

pygame.init()


class Boss_Fireball(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float],
                 target_coordinates: Tuple[Union[int, float]], angle_increment: Union[int, float] = 0):

        pygame.sprite.Sprite.__init__(self)

        self.recoil_probability = 2  # Prob. = (self.recoil_prob.) ^ (-1)

        self.original_image = Assets.Weapon_Images.Fireball
        self.damage = Game_Constants.fireball_base_damage
        y_distance = (-1) * (target_coordinates[1] - coordinate_y)
        x_distance = (target_coordinates[0] - coordinate_x)
        self.angle = math.degrees(math.atan2(y_distance, x_distance)) + angle_increment
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.speed = Game_Constants.Fireball_standard_speed
        self.rect = self.image.get_rect()
        self.rect.center = (coordinate_x, coordinate_y)

        self.fire_trace = []

        # Calculating horizontal and vertical speed based on the angle :
        self.dx = math.cos(math.radians(self.angle)) * self.speed

        # Negative because pygame "y" coordinates increase down the screen.
        self.dy = (-1) * (math.sin(math.radians(self.angle)) * self.speed)

    def update(self, current_player: Character, obstacles: list) -> None:

        fire_trace_aux = self.original_image.copy()
        fire_trace_aux_rect = fire_trace_aux.get_rect()
        fire_trace_aux_rect.center = self.rect.center

        self.fire_trace.append([fire_trace_aux, fire_trace_aux_rect])

        for fireball_trace_aux in self.fire_trace:
            fireball_trace_aux[0].set_alpha(fireball_trace_aux[0].get_alpha() - 30)

            if fireball_trace_aux[0].get_alpha() <= 0:
                self.fire_trace.remove(fireball_trace_aux)

        # reposition based on arrow speed :
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check if fireball has gone off-screen :
        if self.rect.right < 0 or self.rect.left > Game_Constants.Window_width or \
                self.rect.bottom < 0 or self.rect.top > Game_Constants.Window_height:
            self.kill()

        for obstacle in obstacles:

            # If fireball has collided with object and object has collision enabled :
            if self.rect.colliderect(obstacle[1]) and obstacle[2]:
                if random.randint(1, self.recoil_probability) == self.recoil_probability:
                    self.recoil_probability += 1

                    if (self.rect.center[1] > obstacle[1].bottom and self.dy < 0) or (
                            self.rect.center[1] < obstacle[1].top and self.dy > 0):
                        self.dy *= (-1)
                        self.angle *= (-1)
                    else:
                        self.dx *= (-1)
                        self.angle = MyFunctions.sign(self.angle) * (180 - abs(self.angle))

                    Sound_Effects.Fireball_Recoil.play()
                else:
                    self.kill()
                    Sound_Effects.Fireball_Impact.play()

        if self.rect.colliderect(current_player.hitbox) and current_player.take_damage and not current_player.hit:
            current_player.health -= self.damage
            random.choice(Sound_Effects.Damage_Sound_Effect).play()
            current_player.hit = True
            self.kill()

    def draw(self, surface: object) -> None:
        rotated_image = pygame.transform.rotate(self.original_image, self.angle - 90)
        rotated_rect = rotated_image.get_rect(center=self.original_image.get_rect().center)

        surface.blit(rotated_image,
                     (self.rect.centerx - rotated_rect.width / 2, self.rect.centery - rotated_rect.height / 2))

        for fire_trace in self.fire_trace:
            surface.blit(fire_trace[0], (fire_trace[1].x, fire_trace[1].y))
        #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)
