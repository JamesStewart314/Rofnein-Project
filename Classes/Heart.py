import pygame

from typing import Union

import Assets.Heart_Images

from Constants import Game_Constants


pygame.init()


class Heart:

    # dictionary of hearts with their respective images :
    hearts_dict = dict(full_heart=Assets.Heart_Images.Full_Heart_Anim,
                       half_heart=Assets.Heart_Images.Half_Heart_Anim,
                       empty_heart=Assets.Heart_Images.Empty_Heart_Anim)

    def __init__(self, heart_type: str, coordinate_x: Union[int, float], coordinate_y: Union[int, float]):

        assert (heart_type in Heart.hearts_dict), f"Given heart name doesn't exist. Try these: " \
                                                          f"{list(Heart.hearts_dict.keys())}"

        self.update_time = pygame.time.get_ticks()
        self.frame_index = 0

        self.current_heart = heart_type
        self.animation = Heart.hearts_dict.__getitem__(self.current_heart)
        self.image = self.animation[self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (coordinate_x, coordinate_y)

    def update(self) -> None:

        self.image = self.animation[self.frame_index]

        if pygame.time.get_ticks() - self.update_time > Game_Constants.animation_hearts_cooldown:
            self.update_time = pygame.time.get_ticks()

            # Heart animation always have 8 frames, it is unnecessary to spend processing time calculating the size of
            # animations with each update :
            self.frame_index = (self.frame_index + 1) % 8

    def draw(self, surface: object) -> None:
        surface.blit(self.image, (self.rect.x, self.rect.y))
        #pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)
