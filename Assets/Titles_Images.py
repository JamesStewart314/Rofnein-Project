import pygame

from MyFunctions import MyFunctions

pygame.init()

Death_Title = pygame.image.load("Assets/Titles/Dead_Title(3).png")
Death_Title_Width = Death_Title.get_width()
Death_Title_Height = Death_Title.get_height()
Death_Title = MyFunctions.pygame_scale_img(Death_Title, (int(Death_Title_Width / 3), int(Death_Title_Height / 3)))
Death_Title_Rect = Death_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #

Game_Title = pygame.image.load("Assets/Titles/Game_Title(1).png")
Game_Title_Width = Game_Title.get_width()
Game_Title_Height = Game_Title.get_height()
Game_Title = MyFunctions.pygame_scale_img(Game_Title, (int(Game_Title_Width / 3), int(Game_Title_Height / 3)))
Game_Title_Rect = Game_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #

Level_1_Title = pygame.image.load("Assets/Titles/Level_1.png")
Level_1_Title_Width = Level_1_Title.get_width()
Level_1_Title_Height = Level_1_Title.get_height()
Level_1_Title = MyFunctions.pygame_scale_img(Level_1_Title, (int(Level_1_Title_Width / 7), int(Level_1_Title_Height / 7)))
Level_1_Title_Rect = Level_1_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #

Level_2_Title = pygame.image.load("Assets/Titles/Level_2.png")
Level_2_Title_Width = Level_2_Title.get_width()
Level_2_Title_Height = Level_2_Title.get_height()
Level_2_Title = MyFunctions.pygame_scale_img(Level_2_Title, (int(Level_2_Title_Width / 7), int(Level_2_Title_Height / 7)))
Level_2_Title_Rect = Level_2_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #

Level_3_Title = pygame.image.load("Assets/Titles/Level_3(1).png")
Level_3_Title_Width = Level_3_Title.get_width()
Level_3_Title_Height = Level_3_Title.get_height()
Level_3_Title = MyFunctions.pygame_scale_img(Level_3_Title, (int(Level_3_Title_Width / 7), int(Level_3_Title_Height / 7)))
Level_3_Title_Rect = Level_3_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #

Level_4_and_5_Title = pygame.image.load("Assets/Titles/Level_4&5.png")
Level_4_and_5_Title_Width = Level_4_and_5_Title.get_width()
Level_4_and_5_Title_Height = Level_4_and_5_Title.get_height()
Level_4_and_5_Title = MyFunctions.pygame_scale_img(Level_4_and_5_Title, (int(Level_4_and_5_Title_Width / 7),
                                                                         int(Level_4_and_5_Title_Height / 7)))
Level_4_and_5_Title_Rect = Level_4_and_5_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #

Level_6_Title = pygame.image.load("Assets/Titles/Level_6.png")
Level_6_Title_Width = Level_6_Title.get_width()
Level_6_Title_Height = Level_6_Title.get_height()
Level_6_Title = MyFunctions.pygame_scale_img(Level_6_Title, (int(Level_6_Title_Width / 7), Level_6_Title_Height / 7))
Level_6_Title_Rect = Level_6_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #

Level_7_Title = pygame.image.load("Assets/Titles/Level_7.png")
Level_7_Title_Width = Level_7_Title.get_width()
Level_7_Title_Height = Level_7_Title.get_height()
Level_7_Title = MyFunctions.pygame_scale_img(Level_7_Title, (int(Level_7_Title_Width / 7), int(Level_7_Title_Height / 7)))
Level_7_Title_Rect = Level_7_Title.get_rect()

# ------------------------------------------------------------------------------------------------------------------ #
