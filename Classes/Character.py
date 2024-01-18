import pygame
import math
from typing import Union

import Assets

from Assets import Player_Images
from Assets import Sound_Effects
from Assets import Worlds
from Constants import Game_Constants
from MyFunctions import MyFunctions
from Classes import Weapon

pygame.init()


class Character:

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float],
                 health: int = Game_Constants.player_standard_health):

        self.alive = True
        self.take_damage = True
        self.can_attack = True
        self.can_change_weapon = True
        self.can_dash = False
        self.can_interact = True
        self.can_move = True
        self.can_teleport = True
        self.can_regenerate = True
        self.can_ultimate = True
        self.dashing = False
        self.end_dashing = False
        self.flip = False
        self.teleportation = False
        self.end_teleportation = False
        self.ultimate = False
        self.hit = False
        self.new_teleport_position = None

        self.moving = (0, 0)
        self.weapons_inventory = ["Sword", "Bow"]

        self.frame_index = 0
        self.money = 0
        self.update_time = pygame.time.get_ticks()
        self.weapon_change_time = pygame.time.get_ticks()
        self.dash_time = pygame.time.get_ticks()
        self.teleport_time = pygame.time.get_ticks()
        self.ultimate_time = pygame.time.get_ticks()
        self.regenerate_time = pygame.time.get_ticks()
        self.ultimate_transition = pygame.time.get_ticks()
        self.last_hit = pygame.time.get_ticks()
        self.health = health

        self.dash_velocity = Game_Constants.dash_velocity
        self.Animation_Cooldown = Game_Constants.animation_cooldown

        self.animation = Player_Images.Player_Idle_Animation
        self.player_image = self.animation[self.frame_index]
        self.rect = pygame.Rect(0, 0, 25 * Game_Constants.SCALE, 30 * Game_Constants.SCALE)
        self.rect.center = (coordinate_x, coordinate_y)
        self.hitbox = self.rect.copy()
        self.hitbox.width -= 10 * Game_Constants.SCALE
        self.hitbox.height -= 11 * Game_Constants.SCALE

        self.ultimate_trace = []

    def update(self, weapon: Weapon) -> None:
        self.can_attack = not self.dashing and not self.end_dashing and \
                          not self.teleportation and not self.end_teleportation

        self.take_damage = self.can_attack

        if weapon.current_weapon == "none_wp" and self.ultimate:
            self.take_damage = False

        if self.can_attack:
            self.Animation_Cooldown = Game_Constants.animation_cooldown

        # Check if character has died :
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.ultimate = False
            self.take_damage = False
            self.Animation_Cooldown = Game_Constants.animation_death_cooldown
            MyFunctions.set_animation(self, Player_Images.Player_Death_Animation)
            Sound_Effects.Death_Sound_Effect.play_once()

        if pygame.time.get_ticks() - self.dash_time > Game_Constants.dash_cooldown and not self.can_dash:
            self.dash_time = pygame.time.get_ticks()
            self.can_dash = True

        if pygame.time.get_ticks() - self.teleport_time > Game_Constants.teleport_cooldown and not self.can_teleport:
            self.teleport_time = pygame.time.get_ticks()
            self.can_teleport = True

        if pygame.time.get_ticks() - self.ultimate_time > Game_Constants.ultimate_cooldown and not self.can_ultimate:
            self.can_ultimate = True

        if pygame.time.get_ticks() - self.ultimate_time > Game_Constants.ultimate_using_time and self.ultimate:  # Time to turn off Ultimate.
            self.ultimate_time = pygame.time.get_ticks()
            self.ultimate = False

        if pygame.time.get_ticks() - self.regenerate_time > Game_Constants.regenerate_cooldown and not self.can_regenerate:
            self.regenerate_time = pygame.time.get_ticks()
            self.can_regenerate = True

        if pygame.time.get_ticks() - self.last_hit > Game_Constants.hit_cooldown:
            self.hit = False

        if not self.can_change_weapon and (pygame.time.get_ticks() - self.weapon_change_time > Game_Constants.weapon_change_cooldown):
            self.weapon_change_time = pygame.time.get_ticks()
            self.can_change_weapon = True

        if self.ultimate and (Game_Constants.ultimate_using_time - (pygame.time.get_ticks() - self.ultimate_time) <= 2000):
            # The player begins to alternate colors to warn of the end of the ultimate.
            if not ((self.dashing or self.end_dashing) or (self.teleportation or self.end_teleportation)):  # Not Teleporting and Dashing
                if self.frame_index % 2 == 0:
                    if self.moving[0] or self.moving[1]:
                        self.animation = Assets.Player_Images.Player_Running_Ultimate_Animation
                    else:
                        if self.animation == Assets.Player_Images.Player_Running_Ultimate_Animation or\
                                self.animation == Assets.Player_Images.Player_Running_Animation:

                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Idle_Ultimate_Animation)
                        else:
                            self.animation = Assets.Player_Images.Player_Idle_Ultimate_Animation
                else:
                    if self.moving[0] or self.moving[1]:
                        self.animation = Assets.Player_Images.Player_Running_Animation
                    else:
                        if self.animation == Assets.Player_Images.Player_Running_Ultimate_Animation or\
                                self.animation == Assets.Player_Images.Player_Running_Animation:

                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Idle_Animation)
                        else:
                            self.animation = Assets.Player_Images.Player_Idle_Animation
            else:
                if self.animation in (Assets.Player_Images.Player_Running_Ultimate_Animation,
                                      Assets.Player_Images.Player_Idle_Ultimate_Animation,
                                      Assets.Player_Images.Player_Running_Animation,
                                      Assets.Player_Images.Player_Idle_Animation):
                    if self.dashing:
                        if self.frame_index % 2 == 0:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_First_Dash_Ultimate)
                        else:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_First_Dash)
                    else:  # Player is Teleporting
                        if self.frame_index % 2 == 0:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Global_Ultimate_Teleport_Start)
                        else:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Global_Teleport_Start)

                if self.dashing or self.end_dashing:
                    if self.dashing and not self.end_dashing:
                        if self.frame_index % 2 == 0:
                            self.animation = Assets.Player_Images.Player_First_Dash_Ultimate
                        else:
                            self.animation = Assets.Player_Images.Player_First_Dash
                    else:
                        if self.frame_index % 2 == 0:
                            self.animation = Assets.Player_Images.Player_Second_Dash_Ultimate
                        else:
                            self.animation = Assets.Player_Images.Player_Second_Dash

        # Handle Animation and update image.
        self.player_image = self.animation[self.frame_index]

        # Updating Traces :
        for trace in self.ultimate_trace:
            trace[0].set_alpha(trace[0].get_alpha() - 15)

            if trace[0].get_alpha() <= 0:
                self.ultimate_trace.remove(trace)

        # Speed Trace from Ultimate :
        if self.ultimate:
            trace_aux = pygame.transform.flip(self.player_image, self.flip, False).copy()
            trace_aux.set_alpha(70)
            trace_aux_rect = trace_aux.get_rect()
            trace_aux_rect.x, trace_aux_rect.y = self.rect.x - Game_Constants.OFFSET, self.rect.y - Game_Constants.OFFSET

            self.ultimate_trace.append((trace_aux, trace_aux_rect))

        if self.hit and self.alive:
            if self.frame_index % 2 == 0:
                self.player_image.set_alpha(125)
            else:
                self.player_image.set_alpha(255)
        else:
            self.player_image.set_alpha(255)

        # Check if enough time has passed since the last update.
        if pygame.time.get_ticks() - self.update_time > self.Animation_Cooldown:
            if self.alive:
                if not self.teleportation:

                    animation_length = len(self.animation)
                    self.frame_index = (self.frame_index + 1) % animation_length

                    if self.end_dashing and self.frame_index == 0:  # End of the second dash animation.
                        self.dashing = False
                        self.end_dashing = False
                        self.can_dash = False
                        self.dash_velocity = Game_Constants.dash_velocity
                        self.Animation_Cooldown = Game_Constants.animation_cooldown
                        self.take_damage = True

                    if self.dashing and self.frame_index == 0:  # End of the first dash animation.
                        self.can_dash = False
                        if self.moving[0] or self.moving[1]:
                            # I'm not going to divide the diagonals by sqrt(2), it's an irrelevant difference
                            self.rect.centerx += self.moving[0] * Game_Constants.dash_horizontal_distance
                            self.rect.centery += self.moving[1] * Game_Constants.dash_vertical_distance
                        else:
                            if not self.flip:
                                self.rect.centerx += Game_Constants.dash_horizontal_distance
                            else:
                                self.rect.centerx -= Game_Constants.dash_horizontal_distance
                        if not self.ultimate:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Second_Dash)
                        else:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Second_Dash_Ultimate)
                        self.dash_velocity = Game_Constants.dash_velocity
                        self.Animation_Cooldown *= 2
                        self.end_dashing = True

                else:
                    if not self.end_teleportation:
                        animation_length = len(self.animation)
                        self.frame_index += 1
                        if self.frame_index == animation_length:
                            if not self.ultimate:
                                MyFunctions.set_animation(self, Assets.Player_Images.Player_Global_Teleport_Ending)
                            else:
                                MyFunctions.set_animation(self, Assets.Player_Images.Player_Global_Ultimate_Teleport_Ending)
                            new_position = self.new_teleport_position
                            self.rect.centerx, self.rect.centery = new_position[0], new_position[1]
                            self.end_teleportation = True
                    else:
                        animation_length = len(self.animation)
                        self.frame_index += 1
                        if self.frame_index == animation_length:
                            if not self.ultimate:
                                MyFunctions.set_animation(self, Assets.Player_Images.Player_Idle_Animation)
                            else:
                                MyFunctions.set_animation(self, Assets.Player_Images.Player_Idle_Ultimate_Animation)
                            self.teleportation = False
                            self.end_teleportation = False
            else:
                self.frame_index += 1

                if self.frame_index > 9:
                    self.frame_index = 9

            self.update_time = pygame.time.get_ticks()

    def movement(self, dx: Union[int, float], dy: Union[int, float], obstacles: list, tiles_matrix: list) -> None:  # Update the player's position.

        if self.can_move:  # Movement Locker.
            if not self.dashing and not self.teleportation:
                if not self.ultimate:
                    if dx != 0 or dy != 0:  # Movement animation.
                        MyFunctions.set_animation(self, Assets.Player_Images.Player_Running_Animation)
                        self.moving = (MyFunctions.sign(dx), MyFunctions.sign(dy))
                    else:  # Idle animation.
                        MyFunctions.set_animation(self, Assets.Player_Images.Player_Idle_Animation)
                        self.moving = (0, 0)
                else:  # Movement in Ultimate :
                    if dx != 0 or dy != 0:  # Movement animation.
                        if Game_Constants.ultimate_using_time - (pygame.time.get_ticks() - self.ultimate_time) > 2000:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Running_Ultimate_Animation)
                        self.moving = (MyFunctions.sign(dx), MyFunctions.sign(dy))
                    else:  # Idle animation.
                        if Game_Constants.ultimate_using_time - (pygame.time.get_ticks() - self.ultimate_time) > 2000:
                            MyFunctions.set_animation(self, Assets.Player_Images.Player_Idle_Ultimate_Animation)
                        self.moving = (0, 0)

                # Checks if animation needs to be flipped :
                if dx < 0:
                    self.flip = True
                if dx > 0:
                    self.flip = False

                if dx != 0 and dy != 0:  # Diagonal movement.
                    dx /= math.sqrt(2)
                    dy /= math.sqrt(2)

                if self.moving[0] or self.moving[1]:
                    if Worlds.current_level == 1:  # Custom Movement Sound (Grass and Stone Paths)
                        Stone_Walk = False
                        for STR in Worlds.Stone_Tiles_Rects:
                            if STR.colliderect(self.hitbox):
                                Stone_Walk = True
                        if Stone_Walk:
                            Sound_Effects.Grass_Walking_Sound.stop()
                            Sound_Effects.Walking_Sound.play_loop()
                        else:
                            Sound_Effects.Walking_Sound.stop()
                            Sound_Effects.Grass_Walking_Sound.play_loop()
                    elif Worlds.current_level == 2:  # Custom Movement Sound ( Level 2 )

                        current_tile_x = self.rect.centerx // 32
                        current_tile_y = self.rect.centery // 32

                        # The matrix map is transposed :
                        if tiles_matrix[current_tile_y][current_tile_x] in {8, 34}:
                            Sound_Effects.Grass_Walking_Sound.stop()
                            Sound_Effects.Walking_Sound.play_loop()
                        else:
                            Sound_Effects.Walking_Sound.stop()
                            Sound_Effects.Grass_Walking_Sound.play_loop()
                    else:
                        Sound_Effects.Echo_Walking_Sound.play_loop()
                else:
                    Sound_Effects.Echo_Walking_Sound.stop()
                    Sound_Effects.Walking_Sound.stop()
                    Sound_Effects.Grass_Walking_Sound.stop()

                self.rect.x += dx

                for obstacle in obstacles:
                    if obstacle[2]:
                        if obstacle[1].colliderect(self.rect):
                            if dx > 0:
                                self.rect.right = obstacle[1].left
                            if dx < 0:
                                self.rect.left = obstacle[1].right

                self.rect.y += dy

                for obstacle in obstacles:
                    if obstacle[2]:
                        if obstacle[1].colliderect(self.rect):
                            if dy > 0:
                                self.rect.bottom = obstacle[1].top
                            if dy < 0:
                                self.rect.top = obstacle[1].bottom

            elif self.teleportation:
                pass  # Not move during teleportation animation

            else:  # if it's dashing :

                self.can_dash = False

                if not self.end_dashing:  # Speed increment and decrement of first part of dash :
                    if self.frame_index < 5:
                        self.dash_velocity *= 1.2
                    else:
                        self.dash_velocity /= 1.1

                else:  # Deceleration of the second part of the dash :
                    self.dash_velocity /= 1.1

                if not self.moving[0] and not self.moving[1]:  # Stopped dash :
                    if not self.flip:  # Check the direction of the dash :
                        self.rect.x += self.dash_velocity
                    else:
                        self.rect.x -= self.dash_velocity

                    for obstacle in obstacles:
                        if obstacle[2]:
                            if obstacle[1].colliderect(self.rect):

                                dx = 1 if not self.flip else (-1)

                                if dx > 0:
                                    self.rect.right = obstacle[1].left
                                if dx < 0:
                                    self.rect.left = obstacle[1].right

                else:  # Moving dash :
                    if self.moving[0] and self.moving[1]:  # Diagonal Dash
                        # Just an arbitrary suitable speed reduction value :
                        self.rect.x += self.moving[0] * self.dash_velocity / 2.6 * math.sqrt(2)

                        for obstacle in obstacles:
                            if obstacle[2]:
                                if obstacle[1].colliderect(self.rect):

                                    dx = MyFunctions.sign(self.moving[0] * self.dash_velocity / 2.6 * math.sqrt(2))

                                    if dx > 0:
                                        self.rect.right = obstacle[1].left
                                    if dx < 0:
                                        self.rect.left = obstacle[1].right

                        self.rect.y += self.moving[1] * self.dash_velocity / 2.6 * math.sqrt(2)

                        for obstacle in obstacles:
                            if obstacle[2]:
                                if obstacle[1].colliderect(self.rect):

                                    dy = MyFunctions.sign(self.moving[1] * self.dash_velocity / 2.6 * math.sqrt(2))

                                    if dy > 0:
                                        self.rect.bottom = obstacle[1].top
                                    if dy < 0:
                                        self.rect.top = obstacle[1].bottom

                    else:
                        if not self.moving[0]:  # Only vertical dash movement :
                            # Just an arbitrary suitable speed reduction value :
                            self.rect.y += self.moving[1] * self.dash_velocity / 1.3

                            for obstacle in obstacles:
                                if obstacle[2]:
                                    if obstacle[1].colliderect(self.rect):

                                        dy = MyFunctions.sign(self.moving[1] * self.dash_velocity / 1.3)

                                        if dy > 0:
                                            self.rect.bottom = obstacle[1].top
                                        if dy < 0:
                                            self.rect.top = obstacle[1].bottom

                        else:  # Only horizontal dash movement :
                            self.rect.x += self.moving[0] * self.dash_velocity

                            for obstacle in obstacles:
                                if obstacle[2]:
                                    if obstacle[1].colliderect(self.rect):

                                        dx = MyFunctions.sign(self.moving[0] * self.dash_velocity)

                                        if dx > 0:
                                            self.rect.right = obstacle[1].left
                                        if dx < 0:
                                            self.rect.left = obstacle[1].right

            self.hitbox.center = self.rect.center

    def dash(self) -> None:
        if self.can_dash:
            self.dashing = True
            self.can_dash = False
            self.end_dashing = False
            self.take_damage = False

            self.dash_velocity = Game_Constants.dash_velocity
            self.Animation_Cooldown = Game_Constants.dash_animation_cooldown

            self.dash_time = pygame.time.get_ticks()

            if not self.ultimate:
                MyFunctions.set_animation(self, Assets.Player_Images.Player_First_Dash)
            else:
                MyFunctions.set_animation(self, Assets.Player_Images.Player_First_Dash_Ultimate)

            Sound_Effects.Walking_Sound.stop()
            Sound_Effects.Grass_Walking_Sound.stop()
            Sound_Effects.Echo_Walking_Sound.stop()
            Sound_Effects.Dash_Sound.play()

    def teleport(self, new_position: tuple) -> None:
        if self.can_teleport:
            self.take_damage = False
            self.can_attack = False
            self.can_teleport = False
            self.teleportation = True
            self.end_teleportation = False

            self.new_teleport_position = new_position
            self.Animation_Cooldown = Game_Constants.animation_teleport_cooldown

            self.teleport_time = pygame.time.get_ticks()

            if not self.ultimate:
                MyFunctions.set_animation(self, Assets.Player_Images.Player_Global_Teleport_Start)
            else:
                MyFunctions.set_animation(self, Assets.Player_Images.Player_Global_Ultimate_Teleport_Start)

            Sound_Effects.Walking_Sound.stop()
            Sound_Effects.Grass_Walking_Sound.stop()
            Sound_Effects.Echo_Walking_Sound.stop()
            Sound_Effects.Teleport_Sound.play()

    def ultimate_cast(self):
        if self.can_ultimate:
            self.ultimate = True
            self.can_ultimate = False
            self.ultimate_time = pygame.time.get_ticks()
            Sound_Effects.Ultimate_Sound.play()

    def regenerate(self):
        if self.can_regenerate and self.health <= 90 and self.money >= 100:

            self.can_regenerate = False
            self.regenerate_time = pygame.time.get_ticks()

            self.health += 10
            self.money -= 100

            Sound_Effects.Regeneration_Sound.play()

    def draw(self, surface: object) -> None:  # Draws the character on the given surface.
        flipped_img = pygame.transform.flip(self.player_image, self.flip, False)
        surface.blit(flipped_img, (self.rect.x - Game_Constants.OFFSET,
                                   self.rect.y - Game_Constants.OFFSET))

        for trace in self.ultimate_trace:
            surface.blit(trace[0], (trace[1].x, trace[1].y))
        # pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)
        # pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.hitbox, 1)
