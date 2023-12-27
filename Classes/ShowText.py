import pygame

from typing import Union

from Constants import Game_Constants

pygame.init()

Atari_Classic_Font = pygame.font.Font("Assets/Fonts/AtariClassic.ttf", Game_Constants.damage_text_size)
Micro_Font = pygame.font.Font("Assets/Fonts/Micro_font.ttf", Game_Constants.damage_text_size)

# Dictionary of all fonts :
fonts_dict = dict(AtariClassic=Atari_Classic_Font, Micro=Micro_Font)


def draw_text(text: str, font: str, text_color: Union[tuple, list],
              coordinate_x: Union[int, float], coordinate_y: Union[int, float], screen: object, opacity: int = 255):

    image = fonts_dict.__getitem__(font).render(text, True, text_color)
    image.set_alpha(opacity)
    screen.blit(image, (coordinate_x, coordinate_y))


class ShowText(pygame.sprite.Sprite):

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float], damage: str, color: list,
                 font: str, kill_time: Union[int, float] = Game_Constants.damage_text_cooldown,
                 speed: Union[int, float] = Game_Constants.damage_text_speed):

        assert (font in fonts_dict), f"Given font doesn't exist. Try these: " \
                                                          f"{list(fonts_dict.keys())}"

        pygame.sprite.Sprite.__init__(self)
        self.image = fonts_dict.__getitem__(font).render(damage, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (coordinate_x, coordinate_y)
        self.counter = pygame.time.get_ticks()
        self.kill_time = kill_time
        self.speed = speed

    def update(self) -> None:

        # Move Damage Text Up :
        self.rect.y -= self.speed

        # Delete After Image Vanished :
        self.image.set_alpha(max(0, self.image.get_alpha() - Game_Constants.opacity_change_rate))

        if self.image.get_alpha() <= 0:
            self.kill()



