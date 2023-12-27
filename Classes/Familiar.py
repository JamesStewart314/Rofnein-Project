# Same as Character Class.
import pygame
import math

from typing import Union

from Assets import Familiar_Images
from MyFunctions import MyFunctions
from Constants import Game_Constants
from Classes import Character

pygame.init()


class Familiar:
    Animation_Cooldown = Game_Constants.animation_cooldown

    familiar_dict = dict(bat=Familiar_Images.Bat_Idle_Animation)

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float], current_familiar: str):

        self.frame_index = 0
        self.flip = False

        self.current_familiar = current_familiar
        self.speed = Game_Constants.Player_Speed * 9 / 10  # 90% of player's speed
        self.update_time = pygame.time.get_ticks()

        self.animation = Familiar.familiar_dict.__getitem__(current_familiar)
        self.familiar_image = self.animation[self.frame_index]
        self.rect = self.familiar_image.get_rect()
        self.rect.center = (coordinate_x, coordinate_y)

    def update(self) -> None:
        # Handle Animation and update image.
        self.familiar_image = self.animation[self.frame_index]

        # Check if enough time has passed since the last update.
        if pygame.time.get_ticks() - self.update_time >= Familiar.Animation_Cooldown:
            animation_length = len(self.animation)
            self.frame_index = (self.frame_index + 1) % animation_length
            self.update_time = pygame.time.get_ticks()

    def movement(self, dx: int, dy: int) -> None:  # Update the monster's position.

        # Checks if animation needs to be flipped :
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

        if dx != 0 and dy != 0:  # Diagonal movement.
            dx = float('%.3f' % (dx / math.sqrt(2.69)))
            dy = float('%.3f' % (dy / math.sqrt(2.69)))

        self.rect.x += dx

        self.rect.y += dy

    def ai(self, current_player: Character) -> None:

        ai_dx = 0
        ai_dy = 0

        # Check distance from the player :
        distance = math.sqrt((self.rect.centerx - current_player.rect.centerx) ** 2 +
                             (self.rect.centery - current_player.rect.centery) ** 2)

        if distance > 70:

            if self.rect.centerx > current_player.rect.centerx:
                ai_dx = (-1) * self.speed
            if self.rect.centerx < current_player.rect.centerx:
                ai_dx = self.speed

            if self.rect.centery > current_player.rect.centery:
                ai_dy = (-1) * self.speed
            if self.rect.centery < current_player.rect.centery:
                ai_dy = self.speed

            if abs(current_player.rect.centery - self.rect.centery) <= 2:  # To avoid abnormalities in enemy movement.
                ai_dy = 0

            self.movement(ai_dx, ai_dy)

    def draw(self, surface: object) -> None:  # Draws the monster on the given surface.
        flipped_img = pygame.transform.flip(self.familiar_image, self.flip, False)
        surface.blit(flipped_img, (self.rect.x, self.rect.y))
        #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)

