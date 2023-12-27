import pygame
import math

from typing import Union, List

import Assets.Weapon_Images

from Assets import Sound_Effects
from Constants import Game_Constants
from Classes import Arrow
from Classes import Character
from MyFunctions import MyFunctions_2

pygame.init()


class Weapon:
    # Dictionary of weapons with their respective images :
    Weapons_inventory = dict(Sword=Assets.Weapon_Images.Sword_Img, Bow=Assets.Weapon_Images.Bow_Img,
                             Steel_bow=Assets.Weapon_Images.Steel_Bow_Img, Gold_bow=Assets.Weapon_Images.Gold_Bow_Img,
                             none_wp=Assets.Weapon_Images.None_Weapon)

    def __init__(self, current_weapon: str = "none_wp", inverted: bool = False):

        assert (current_weapon in Weapon.Weapons_inventory), f"Given weapon doesn't exist. Try these: " \
                                                             f"{list(Weapon.Weapons_inventory.keys())}"

        self.fired = False

        self.angle = 0  # Initial angle.
        self.inverted = inverted  # Useed to create the inverted sword (ultimate)

        self.current_weapon = current_weapon
        # Gets the weapon from Weapons inventory dictionary :
        self.original_image = Weapon.Weapons_inventory.get(current_weapon)
        self.current_image = pygame.transform.rotate(self.original_image, self.angle)  # Rotates the original image.
        self.last_shot = pygame.time.get_ticks()

        self.weapon_trace = []

        if self.current_weapon == "none_wp":
            self.rect = pygame.Rect(0, 0, 0, 0)
        else:
            self.rect = self.original_image.get_rect()
        self.sword_hitbox = self.rect

    def update(self, current_player: Character) -> Union[None, Arrow.Arrow, List[Arrow.Arrow]]:

        # Updating Traces :
        for trace in self.weapon_trace:
            trace[0].set_alpha(trace[0].get_alpha() - 5)

            if trace[0].get_alpha() <= 0:
                self.weapon_trace.remove(trace)

        if self.current_weapon == "Sword":
            self.original_image = Weapon.Weapons_inventory.__getitem__("Sword")
            # Dimensions of the sword : 11 Pxl x 32 pxl
            self.rect = pygame.Rect(0, 0, 16 * Game_Constants.Sword_scale, 36 * Game_Constants.Sword_scale)

        elif self.current_weapon == "Bow":
            self.original_image = Weapon.Weapons_inventory.__getitem__("Bow")
            self.rect = self.original_image.get_rect()

        elif self.current_weapon == "Steel_bow":
            self.original_image = Weapon.Weapons_inventory.__getitem__("Steel_bow")
            self.rect = self.original_image.get_rect()

        elif self.current_weapon == "Gold_bow":
            self.original_image = Weapon.Weapons_inventory.__getitem__("Gold_bow")
            self.rect = self.original_image.get_rect()

        else:
            self.rect = pygame.Rect(0, 0, 0, 0)


        self.rect.center = current_player.rect.center  # Updates the weapon position.

        mouse_position = pygame.mouse.get_pos()
        x_distance = mouse_position[0] - current_player.rect.centerx
        # Negative because pygame "y" coordinates increase down the screen.
        y_distance = (-1) * (mouse_position[1] - current_player.rect.centery)

        self.angle = math.degrees(math.atan2(y_distance, x_distance))

        #
        # Updating the sword hitbox :
        # I couldn't figure out how to improve this section of the code.
        # It was extremely complex for me to create this dynamic hitbox, so if there are changes to the scale of
        # the game and the hitbox remains incorrect, sorry for the inconvenience.
        #
        # Feel free to troubleshoot this issue if you can, I would be forever grateful ^^.
        #

        if self.current_weapon == "Sword":
            sword_radius = Game_Constants.Sword_radius  # Distance from player to sword.

            # Coordinates from player :
            player_x = self.rect.centerx
            player_y = self.rect.centery

            # Evaluating the sword coordinates :
            if not self.inverted:
                sword_x = player_x + sword_radius * math.cos(math.radians(self.angle))
                sword_y = player_y - sword_radius * math.sin(math.radians(self.angle))
            else:
                sword_x = player_x - sword_radius * math.cos(math.radians(self.angle))
                sword_y = player_y + sword_radius * math.sin(math.radians(self.angle))

            # Changing the sword hitbox by inverting the width and heiht of the rectangle.
            self.sword_hitbox = pygame.Rect(self.rect)
            self.sword_hitbox.center = (sword_x, sword_y)

            if 0 <= self.angle <= 45 or -45 <= self.angle <= 0:
                width_aux = self.rect.width
                height_aux = self.rect.height
                self.sword_hitbox.width = height_aux
                self.sword_hitbox.height = width_aux
                self.sword_hitbox.y += 10  # Sword hitbox arbitrary deslocation
                self.sword_hitbox.x -= 10  # Sword hitbox arbitrary deslocation

            elif 135 <= self.angle <= 180 or -180 <= self.angle <= -135:
                width_aux = self.rect.width
                height_aux = self.rect.height
                self.sword_hitbox.width = height_aux
                self.sword_hitbox.height = width_aux
                self.sword_hitbox.y += 10  # Sword hitbox arbitrary deslocation
                self.sword_hitbox.x -= 10  # Sword hitbox arbitrary deslocation

            if current_player.ultimate:

                # Rotating Sword :
                rotated_sword = pygame.transform.rotate(self.original_image.copy(), self.angle - 90)

                if self.inverted:
                    rotated_sword = pygame.transform.flip(rotated_sword, True, True)

                rotated_sword.set_alpha(70)
                rotated_sword_rect = rotated_sword.get_rect(center=(sword_x, sword_y))

                self.weapon_trace.append((rotated_sword, rotated_sword_rect))

        # Shooting function :
        # Getting player clicks :
        if self.current_weapon != "none_wp":
            if self.current_weapon == "Gold_bow":
                shoot_cooldown = 800
            if self.current_weapon == "Steel_bow":
                shoot_cooldown = 500
            else:
                shoot_cooldown = 1000

            # Creating Bow Trace :
            if current_player.ultimate and self.current_weapon != "Sword":
                rotated_image = pygame.transform.rotate(self.original_image, self.angle)
                rotated_image.set_alpha(70)
                rotated_image_rect = rotated_image.get_rect()
                rotated_image_rect.center = self.rect.center
                self.weapon_trace.append((rotated_image, rotated_image_rect))

            temp_arrow = None
            mouse_pressed = pygame.mouse.get_pressed()[0]

            if mouse_pressed and (pygame.time.get_ticks() - self.last_shot >= shoot_cooldown) and not self.fired:

                if self.current_weapon == "Bow":
                    temp_arrow = Arrow.Arrow("standard_arrow", self.rect.centerx,
                                             self.rect.centery, self.angle)

                    if current_player.ultimate:
                        temp_arrow.recoil = True

                    self.last_shot = pygame.time.get_ticks()
                    self.fired = True

                    return temp_arrow

                elif self.current_weapon == "Steel_bow":
                    temp_arrow = Arrow.Arrow("spirit_arrow", self.rect.centerx,
                                             self.rect.centery, self.angle)

                    self.last_shot = pygame.time.get_ticks()
                    self.fired = True

                    return temp_arrow

                elif self.current_weapon == "Gold_bow":
                    if not current_player.ultimate:
                        temp_arrow_1 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle)
                        temp_arrow_2 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle + 15)
                        temp_arrow_3 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle - 15)

                        # Percentage of damage reduction from side arrows :
                        temp_arrow_2.damage *= Game_Constants.side_arrow_damage_reduction
                        temp_arrow_3.damage *= Game_Constants.side_arrow_damage_reduction

                        self.last_shot = pygame.time.get_ticks()
                        self.fired = True

                        Sound_Effects.Normal_Arrow_Sound.play()

                        return [temp_arrow_1, temp_arrow_2, temp_arrow_3]

                    else:
                        temp_arrow_1 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle + 15)
                        temp_arrow_2 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle + 7.5)
                        temp_arrow_3 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle - 7.5)
                        temp_arrow_4 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle - 15)
                        temp_arrow_5 = Arrow.Arrow("phantom_arrow", self.rect.centerx,
                                                   self.rect.centery, self.angle)

                        # Percentage of damage reduction from side arrows :
                        temp_arrow_1.damage *= Game_Constants.side_arrow_damage_reduction_ultimate
                        temp_arrow_2.damage *= Game_Constants.side_arrow_damage_reduction_ultimate
                        temp_arrow_3.damage *= Game_Constants.side_arrow_damage_reduction_ultimate
                        temp_arrow_4.damage *= Game_Constants.side_arrow_damage_reduction_ultimate

                        distance = MyFunctions_2.distance(current_player.rect, mouse_position)

                        temp_arrow_1.custom_movement = (distance, mouse_position, temp_arrow_5)
                        temp_arrow_2.custom_movement = (distance, mouse_position, temp_arrow_5)
                        temp_arrow_3.custom_movement = (distance, mouse_position, temp_arrow_5)
                        temp_arrow_4.custom_movement = (distance, mouse_position, temp_arrow_5)
                        temp_arrow_5.custom_movement = (distance, mouse_position, temp_arrow_5)

                        self.last_shot = pygame.time.get_ticks()
                        self.fired = True

                        Sound_Effects.Normal_Arrow_Sound.play()

                        return [temp_arrow_1, temp_arrow_2, temp_arrow_3, temp_arrow_4, temp_arrow_5]

            # Reset bow shooting :
            if not mouse_pressed:
                self.fired = False

            return temp_arrow

    def draw(self, surface: object, character: Character) -> None:
        if ((character.dashing and character.frame_index < 6) or not (character.dashing or character.end_dashing) or
            (character.end_dashing and character.frame_index > 4)) and \
                not (character.teleportation or character.end_teleportation) and character.alive:

            if not (self.current_weapon == "Sword" or self.current_weapon == "none_wp"):

                if self.current_weapon == "Bow":
                    # Adjust the rotation origin to the center of the original image.
                    rotated_image = pygame.transform.rotate(self.original_image, self.angle)
                    rotated_rect = rotated_image.get_rect(center=self.original_image.get_rect().center)

                    # Draw the rotated image in the center of the player.
                    surface.blit(rotated_image,
                                 (self.rect.centerx - rotated_rect.width / 2,
                                  self.rect.centery - rotated_rect.height / 2))
                    #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)

                else:
                    # Adjust the rotation origin to the center of the original image.
                    rotated_image = pygame.transform.rotate(self.original_image, self.angle)
                    rotated_rect = rotated_image.get_rect(center=self.original_image.get_rect().center)

                    # Draw the rotated image in the center of the player.
                    surface.blit(rotated_image,
                                 (self.rect.centerx - rotated_rect.width / 2,
                                  self.rect.centery - rotated_rect.height / 2))
                    #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)

            elif self.current_weapon == "Sword":
                sword_radius = Game_Constants.Sword_radius  # Distance from player to sword.

                # Coordinates from player :
                player_x = self.rect.centerx
                player_y = self.rect.centery

                # Evaluating the sword coordinates :
                if not self.inverted:
                    sword_x = player_x + sword_radius * math.cos(math.radians(self.angle))
                    sword_y = player_y - sword_radius * math.sin(math.radians(self.angle))
                else:
                    sword_x = player_x - sword_radius * math.cos(math.radians(self.angle))
                    sword_y = player_y + sword_radius * math.sin(math.radians(self.angle))

                # Rotating Sword :
                rotated_sword = pygame.transform.rotate(self.original_image, self.angle - 90)
                if self.inverted:
                    rotated_sword = pygame.transform.flip(rotated_sword, True, True)
                sword_rect = rotated_sword.get_rect(center=(sword_x, sword_y))

                # Drawing Sword :
                surface.blit(rotated_sword, sword_rect.topleft)
                self.rect.center = (sword_x, sword_y)

            for trace in self.weapon_trace:
                surface.blit(trace[0], (trace[1].x, trace[1].y))
            #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.sword_hitbox, 1)

