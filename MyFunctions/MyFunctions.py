import math

import pygame

from typing import Union, Tuple

from Assets import Player_Images
from Assets import Animations

from Constants import Game_Constants

pygame.init()


def pygame_scale_img(image: object, scale: Union[int, tuple]) -> object:  # Resizes an image by an integer scalar.
    img_width = image.get_width()
    img_height = image.get_height()
    if isinstance(scale, int):
        return pygame.transform.scale(image, (img_width * scale, img_height * scale))
    if isinstance(scale, tuple):
        return pygame.transform.scale(image, (scale[0], scale[1]))


def set_animation(my_object: object, current_animation: list) -> None:
    if my_object.animation != current_animation:
        my_object.frame_index = 0
        my_object.animation = current_animation
        my_object.update_time = pygame.time.get_ticks()


def appearing_animation(screen: object, current_player: object, game_clock: object, background: object) -> None:
    current_player.Animation_Cooldown = 300
    current_player.animation = Player_Images.Player_Appering_Animation

    while True:  # Appearing animation.
        game_clock.tick(Game_Constants.FPS)
        screen.blit(background, (0, 0))
        current_player.draw(screen)

        if pygame.time.get_ticks() - current_player.update_time > current_player.Animation_Cooldown:
            current_player.update_time = pygame.time.get_ticks()
            current_player.frame_index += 1

        current_player.player_image = current_player.animation[current_player.frame_index]
        pygame.display.update()

        if current_player.frame_index == len(Player_Images.Player_Appering_Animation) - 1:
            break

    current_player.Animation_Cooldown = Game_Constants.animation_cooldown


def sign(value: Union[int, float]) -> int:  # Signal Function.
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0
