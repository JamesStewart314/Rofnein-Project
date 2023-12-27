import pygame

from typing import Union

from Assets import Background_Images
from Assets import Buttons
from Classes import Character
from Classes import ShowText
from Classes import ShowFloatingText
from Constants import Game_Constants

pygame.init()


class Sign:
    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float]):

        self.image = Background_Images.Tutorial_Sign
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coordinate_x, coordinate_y
        self.hitbox = self.rect.copy()
        self.hitbox.width /= 1.5
        self.hitbox.height /= 1.6
        self.hitbox.center = (self.rect.centerx, self.rect.centery + 4)
        self.interaction_box = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 3, Game_Constants.grid_spacing * 3)
        self.interaction_box.center = self.rect.center

        self.buttons_sprite_group = pygame.sprite.Group()

        # Loading Buttons :
        self.button_1 = ShowFloatingText.FloatingText(Game_Constants.grid_spacing * 33 - 8, Game_Constants.grid_spacing * 3,
                                                 Buttons.Button_1, speed=0.2, amplitude=5)
        self.button_2 = ShowFloatingText.FloatingText(Game_Constants.grid_spacing * 33 - 8, Game_Constants.grid_spacing * 4,
                                                 Buttons.Button_2, speed=0.2, amplitude=5)
        self.button_e = ShowFloatingText.FloatingText(Game_Constants.grid_spacing * 33 - 8, Game_Constants.grid_spacing * 5,
                                                 Buttons.Button_E, speed=0.2, amplitude=5)
        self.button_r = ShowFloatingText.FloatingText(Game_Constants.grid_spacing * 33 - 8, Game_Constants.grid_spacing * 6,
                                                 Buttons.Button_R, speed=0.2, amplitude=5)
        self.button_g = ShowFloatingText.FloatingText(Game_Constants.grid_spacing * 33 - 8, Game_Constants.grid_spacing * 7,
                                                      Buttons.Button_G, speed=0.2, amplitude=5)
        self.button_shift = ShowFloatingText.FloatingText(Game_Constants.grid_spacing * 33 - 16, Game_Constants.grid_spacing * 8,
                                                 Buttons.Button_Shift, speed=0.2, amplitude=5)
        self.button_f11 = ShowFloatingText.FloatingText(Game_Constants.grid_spacing * 33 - 16, Game_Constants.grid_spacing * 9,
                                                 Buttons.Button_F11, speed=0.2, amplitude=5)

        # Loading Texts :
        Sword_Text = lambda screen: ShowText.draw_text("sword", "AtariClassic", Game_Constants.WHITE_COLOR,
                           self.button_1.rect.x + 38, self.button_1.rect.y + 8, screen,
                           opacity=self.button_1.image.get_alpha())

        Bow_Text = lambda screen: ShowText.draw_text("bow", "AtariClassic", Game_Constants.WHITE_COLOR,
                                                     self.button_2.rect.x + 38, self.button_2.rect.y + 8, screen,
                                                     opacity=self.button_2.image.get_alpha())

        Teleport_Text = lambda screen: ShowText.draw_text("teleport", "AtariClassic", Game_Constants.WHITE_COLOR,
                                                          self.button_e.rect.x + 38, self.button_e.rect.y + 8, screen,
                                                          opacity=self.button_e.image.get_alpha())

        Ultimate_Text = lambda screen: ShowText.draw_text("ultimate", "AtariClassic", Game_Constants.WHITE_COLOR,
                                                          self.button_r.rect.x + 38, self.button_r.rect.y + 8, screen,
                                                          opacity=self.button_r.image.get_alpha())

        Regeneration_Text = lambda screen: ShowText.draw_text("Regen (100 c)", "AtariClassic", Game_Constants.WHITE_COLOR,
                                                              self.button_g.rect.x + 38, self.button_g.rect.y + 8,
                                                              screen, opacity=self.button_g.image.get_alpha())

        Dash_Text = lambda screen: ShowText.draw_text("dash", "AtariClassic", Game_Constants.WHITE_COLOR,
                                                      self.button_shift.rect.x + 52, self.button_shift.rect.y + 8,
                                                      screen, opacity=self.button_shift.image.get_alpha())

        Fullscreen_Text = lambda screen: ShowText.draw_text("fullscreen", "AtariClassic", Game_Constants.WHITE_COLOR,
                                                      self.button_f11.rect.x + 52, self.button_f11.rect.y + 8,
                                                      screen, opacity=self.button_f11.image.get_alpha())

        Interaction_Text_1 = lambda screen: ShowText.draw_text("press right click", "AtariClassic",
                                                             Game_Constants.WHITE_COLOR, self.button_f11.rect.x - Game_Constants.grid_spacing,
                                                             self.button_f11.rect.y + Game_Constants.grid_spacing + 8,
                                                             screen, opacity=self.button_f11.image.get_alpha())

        Interaction_Text_2 = lambda screen: ShowText.draw_text("to interact with", "AtariClassic",
                                                             Game_Constants.WHITE_COLOR, self.button_f11.rect.x - Game_Constants.grid_spacing + 8,
                                                             self.button_f11.rect.y + Game_Constants.grid_spacing * 2 + 8,
                                                             screen, opacity=self.button_f11.image.get_alpha())

        Interaction_Text_3 = lambda  screen: ShowText.draw_text("doors", "AtariClassic",
                                                             Game_Constants.WHITE_COLOR, self.button_f11.rect.x + Game_Constants.grid_spacing + 16,
                                                             self.button_f11.rect.y + Game_Constants.grid_spacing * 3 + 8,
                                                             screen, opacity=self.button_f11.image.get_alpha())

        self.buttons_list = (self.button_1, self.button_2, self.button_e, self.button_r, self.button_g, self.button_shift, self.button_f11)
        self.texts_list = (Sword_Text, Bow_Text, Teleport_Text, Ultimate_Text, Dash_Text, Regeneration_Text, Fullscreen_Text, Interaction_Text_1, Interaction_Text_2, Interaction_Text_3)

    def draw(self, screen: object, current_player: Character) -> None:

        screen.blit(self.image, (self.rect.x, self.rect.y))

        for button in self.buttons_list:
            button.draw(screen)
            button.update_2()

        if self.interaction_box.colliderect(current_player.hitbox):
            for button in self.buttons_list:
                button.fade_in = True
                button.fade_out = False
        else:
            for button in self.buttons_list:
                button.fade_in = False
                button.fade_out = True

        for text in self.texts_list:
            text(screen)

        #pygame.draw.rect(screen, Game_Constants.WHITE_COLOR, self.interaction_box, 1)
