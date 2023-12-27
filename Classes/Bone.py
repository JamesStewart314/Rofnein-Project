import pygame
import math
import random

from typing import Union, Tuple

import Assets.Weapon_Images

from Assets import Sound_Effects
from Constants import Game_Constants
from MyFunctions import MyFunctions
from Classes import Character

pygame.init()


class Bone(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float], target_coordinates: Tuple[Union[int, float]]):

        pygame.sprite.Sprite.__init__(self)

        self.recoil_probability = 10  # Prob. = (self.recoil_prob.) ^ (-1)

        self.original_image = Assets.Weapon_Images.Bone
        self.damage = Game_Constants.bone_base_damage
        y_distance = (-1) * (target_coordinates[1] - coordinate_y)
        x_distance = (target_coordinates[0] - coordinate_x)
        self.angle = math.degrees(math.atan2(y_distance, x_distance))
        self.speed = Game_Constants.Bone_standard_speed
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (coordinate_x, coordinate_y)

        # Calculating horizontal and vertical speed based on the angle :
        self.dx = math.cos(math.radians(self.angle)) * self.speed
        # Negative because pygame "y" coordinates increase down the screen.
        self.dy = (-1) * (math.sin(math.radians(self.angle)) * self.speed)

    def update(self, current_player: Character, obstacles: list) -> None:

        # reposition based on bone speed :
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check if bone has gone off screen :
        if self.rect.right < 0 or self.rect.left > Game_Constants.Window_width or \
                self.rect.bottom < 0 or self.rect.top > Game_Constants.Window_height:
            self.kill()

        # check if bone has collided with objects :
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle[1]) and obstacle[2]:
                if random.randint(1, self.recoil_probability) == self.recoil_probability:
                    self.recoil_probability += 1
                    if (self.rect.center[1] > obstacle[1].bottom and self.dy < 0) or (self.rect.center[1] < obstacle[1].top and self.dy > 0):
                        self.dy *= (-1)
                        self.angle *= (-1)
                    else:
                        self.dx *= (-1)
                        self.angle = MyFunctions.sign(self.angle) * (180 - abs(self.angle))
                else:
                    Sound_Effects.Bone_Impact.play()
                    self.kill()

        # check if bone has collided with player and deals damage :
        if self.rect.colliderect(current_player.hitbox):
            if not current_player.hit:
                current_player.health -= self.damage
                current_player.hit = True
                current_player.last_hit = pygame.time.get_ticks()
                random.choice(Sound_Effects.Damage_Sound_Effect).play()
                self.kill()

    def draw(self, surface: object) -> None:
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.original_image.get_rect().center)

        surface.blit(rotated_image,
                     (self.rect.centerx - rotated_rect.width / 2, self.rect.centery - rotated_rect.height / 2))
        #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)
