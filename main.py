import pygame

from pygame import Surface

import Assets.Player_Images  # To avoid circular import

from Assets import Background_Images
from Assets import Worlds
from Constants import Game_Constants
from MyFunctions import MyFunctions_2

pygame.init()  # Initializing Pygame.

is_fullscreen: bool = False

pygame.display.set_caption("Rofnein")  # Setting the Title
pygame.display.set_icon(Background_Images.Board_Leaf_Icon)  # Changing the Window Icon.

# Creating the Game Window :
Screen: Surface = pygame.display.set_mode(
    (Game_Constants.Window_width, Game_Constants.Window_height)) if not is_fullscreen \
    else pygame.display.set_mode((Game_Constants.Window_width, Game_Constants.Window_height), pygame.FULLSCREEN)

try:
    MyFunctions_2.menu(Screen)
except pygame.error:
    pass
