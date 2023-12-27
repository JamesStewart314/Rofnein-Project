import pygame
import math
import random

from typing import Union

import Assets.Weapon_Images

from Assets import Sound_Effects
from Constants import Game_Constants
from MyFunctions import MyFunctions
from MyFunctions import MyFunctions_2
from Classes import Character
from Classes import Weapon

pygame.init()


class Arrow(pygame.sprite.Sprite):

    # dictionary of arrows with their respective images and damage :
    arrows_dict = dict(standard_arrow=[Assets.Weapon_Images.Standard_Arrow, Game_Constants.standard_arrow_damage],
                       spirit_arrow=[Assets.Weapon_Images.Spirit_Arrow, Game_Constants.spirit_arrow_damage],
                       phantom_arrow=[Assets.Weapon_Images.Phantom_Arrow, Game_Constants.phantom_arrow_damage])

    def __init__(self, arrow_name: str, coordinate_x: Union[int, float], coordinate_y: Union[int, float],
                 shoot_angle: Union[int, float]):

        assert (arrow_name in Arrow.arrows_dict), f"Given arrow doesn't exist. Try these: " \
                                                          f"{list(Arrow.arrows_dict.keys())}"

        pygame.sprite.Sprite.__init__(self)

        self.custom_movement = None
        self.recoil = False
        self.dissipate = True

        self.arrow_hits = set()

        self.original_image = Arrow.arrows_dict.__getitem__(arrow_name)[0]
        self.damage = Arrow.arrows_dict.__getitem__(arrow_name)[1]
        self.angle = shoot_angle
        self.speed = Game_Constants.Arrow_standard_speed
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (coordinate_x, coordinate_y)

        self.dissipate_cooldown = pygame.time.get_ticks()

        # Calculating horizontal and vertical speed based on the angle :
        self.dx = math.cos(math.radians(self.angle)) * self.speed

        # Negative because pygame "y" coordinates increase down the screen.
        self.dy = (-1) * (math.sin(math.radians(self.angle)) * self.speed)

    def update(self, monsters_list: list, current_player: Character, weapon: Weapon, obstacles: list) -> tuple:

        # Reseting Variables :
        return_damage = 0
        damage_position = None

        if self.custom_movement:

            if MyFunctions_2.distance(self.rect.center, self.custom_movement[1]) <= 10:
                if pygame.time.get_ticks() - self.dissipate_cooldown >= 100:
                    self.dissipate = False
            else:
                self.dissipate_cooldown = pygame.time.get_ticks()

            if MyFunctions_2.distance(self.custom_movement[2].rect.center, self.custom_movement[1]) <=\
                    self.custom_movement[0] / 2 and self.dissipate:

                x_distance = self.custom_movement[1][0] - self.rect.centerx
                # Negative because pygame "y" coordinates increase down the screen.
                y_distance = (-1) * (self.custom_movement[1][1] - self.rect.centery)

                self.angle = math.degrees(math.atan2(y_distance, x_distance))

                # Calculating horizontal and vertical speed based on the angle :
                self.dx = math.cos(math.radians(self.angle)) * self.speed

                # Negative because pygame "y" coordinates increase down the screen.
                self.dy = (-1) * (math.sin(math.radians(self.angle)) * self.speed)

        # reposition based on arrow speed :
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Check if arrow has gone off screen :
        if self.rect.right < 0 or self.rect.left > Game_Constants.Window_width or \
                self.rect.bottom < 0 or self.rect.top > Game_Constants.Window_height:
            if not self.recoil:
                self.kill()
            else:
                self.recoil = False
                if self.rect.x < 0 or self.rect.x > Game_Constants.Window_width - self.rect.width:
                    self.dx *= (-1)
                    self.angle = MyFunctions.sign(self.angle) * (180 - abs(self.angle))
                if self.rect.y < 0 or self.rect.y > Game_Constants.Window_height - self.rect.height:
                    self.dy *= (-1)
                    self.angle *= (-1)
                Sound_Effects.Arrow_Recoil.play()

        for obstacle in obstacles:
            if self.rect.colliderect(obstacle[1]) and obstacle[2]:
                if not self.recoil:
                    self.kill()
                else:
                    self.recoil = False
                    if (self.rect.center[1] > obstacle[1].bottom and self.dy < 0) or (self.rect.center[1] < obstacle[1].top and self.dy > 0):
                        self.dy *= (-1)
                        self.angle *= (-1)
                    else:
                        self.dx *= (-1)
                        self.angle = MyFunctions.sign(self.angle) * (180 - abs(self.angle))

                    Sound_Effects.Arrow_Recoil.play()

        # Check collision between the arrow and enemies :
        for monster in monsters_list:
            if not (current_player.ultimate and weapon.current_weapon == "Steel_bow"):
                if monster.rect.colliderect(self.rect) and monster.alive:
                    Sound_Effects.Arrow_Impact.play()
                    current_damage = self.damage + random.randint((-1) * (int(self.damage * 3 / 10)),
                                                                  int((self.damage * 3 / 10)))
                    return_damage = current_damage
                    damage_position = monster.rect
                    monster.health -= int(current_damage)
                    monster.hit = True
                    self.kill()
                    break
            else:
                # Steel bow ultimate to pierce enemies with arrows and inflict damage just once :
                if not (monster in self.arrow_hits):
                    if monster.rect.colliderect(self.rect) and monster.alive:
                        Sound_Effects.Arrow_Impact.play()
                        current_damage = self.damage + random.randint((-1) * (int(self.damage * 3 / 10)),
                                                                      int((self.damage * 3 / 10)))
                        return_damage = current_damage
                        damage_position = monster.rect
                        monster.health -= int(current_damage)
                        monster.hit = True
                        self.arrow_hits.add(monster)

        # Returns an Integer Approximation For The Damage And The Damage Position :
        return int(return_damage), damage_position

    def draw(self, surface: object) -> None:
        rotated_image = pygame.transform.rotate(self.original_image, self.angle - 90)
        rotated_rect = rotated_image.get_rect(center=self.original_image.get_rect().center)

        surface.blit(rotated_image,
                     (self.rect.centerx - rotated_rect.width / 2, self.rect.centery - rotated_rect.height / 2))
        #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)
