import pygame

from MyFunctions import MyFunctions
from Classes import ShowFloatingText
from Constants import Game_Constants

pygame.init()

Boss_Health_Bar_Base = pygame.image.load("Assets/Health_Bar/Boss_Health_Bar_Base.png")
Boss_Health_Bar_Base = MyFunctions.pygame_scale_img(Boss_Health_Bar_Base, 3)
Boss_Health_Bar_Base_Rect = Boss_Health_Bar_Base.get_rect()
Boss_Health_Bar_Base_Rect.center = Game_Constants.grid_spacing * 4, Game_Constants.grid_spacing * 2

Boss_Health_Bar_Base = ShowFloatingText.FloatingText(Boss_Health_Bar_Base_Rect.x, Boss_Health_Bar_Base_Rect.y,
                                                     Boss_Health_Bar_Base, amplitude=3)

Boss_Health_Bar = pygame.image.load("Assets/Health_Bar/Boss_Health_Bar.png")
Boss_Health_Bar = MyFunctions.pygame_scale_img(Boss_Health_Bar, 3)
Boss_Health_Bar_Rect = Boss_Health_Bar.get_rect()
Boss_Health_Bar_Rect.center = Boss_Health_Bar_Base_Rect.centerx, Boss_Health_Bar_Base_Rect.centery + 20