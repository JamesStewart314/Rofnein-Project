import pygame

from MyFunctions import MyFunctions

pygame.init()

Restart_Button = pygame.image.load("Assets/Buttons/Restart_Button.png")
Restart_Button_Width = Restart_Button.get_width()
Restart_Button_Height = Restart_Button.get_height()
Restart_Button = MyFunctions.pygame_scale_img(Restart_Button,
                                              (int(Restart_Button_Width / 6), int(Restart_Button_Height / 6)))
Restart_Button_Rect = Restart_Button.get_rect()

Restart_Button_Pressed = pygame.image.load("Assets/Buttons/Restart_Button_Pressed(3).png")
Restart_Button_Pressed_Width = Restart_Button_Pressed.get_width()
Restart_Button_Pressed_Height = Restart_Button_Pressed.get_height()
Restart_Button_Pressed = MyFunctions.pygame_scale_img(Restart_Button_Pressed, (int(Restart_Button_Pressed_Width / 6),
                                                                               int(Restart_Button_Pressed_Height / 6)))
Restart_Button_Pressed_Rect = Restart_Button_Pressed.get_rect()

# -------------------------------------------------------------------------------------------------------------------- #

Menu_Button = pygame.image.load("Assets/Buttons/Menu_Button.png")
Menu_Button_Width = Menu_Button.get_width()
Menu_Button_Height = Menu_Button.get_height()
Menu_Button = MyFunctions.pygame_scale_img(Menu_Button, (int(Menu_Button_Width / 6.5), int(Menu_Button_Height / 6.5)))
Menu_Button_Rect = Menu_Button.get_rect()

Menu_Button_Pressed = pygame.image.load("Assets/Buttons/Menu_Button_Pressed.png")
Menu_Button_Pressed_Width = Menu_Button_Pressed.get_width()
Menu_Button_Pressed_Height = Menu_Button_Pressed.get_height()
Menu_Button_Pressed = MyFunctions.pygame_scale_img(Menu_Button_Pressed,
                                                   (int(Menu_Button_Width / 6.5), int(Menu_Button_Height / 6.5)))
Menu_Button_Pressed_Rect = Menu_Button_Pressed.get_rect()

# -------------------------------------------------------------------------------------------------------------------- #

Play_Button = pygame.image.load("Assets/Buttons/Play_Button.png")
Play_Button_Width = Play_Button.get_width()
Play_Button_Height = Play_Button.get_height()
Play_Button = MyFunctions.pygame_scale_img(Play_Button, (int(Play_Button_Width / 5), int(Play_Button_Height / 5)))
Play_Button_Rect = Play_Button.get_rect()

Play_Button_Pressed = pygame.image.load("Assets/Buttons/Play_Button_Pressed.png")
Play_Button_Pressed_Width = Play_Button_Pressed.get_width()
Play_Button_Pressed_Height = Play_Button_Pressed.get_height()
Play_Button_Pressed = MyFunctions.pygame_scale_img(Play_Button_Pressed,
                                                   (int(Play_Button_Width / 5), int(Play_Button_Height / 5)))
Play_Button_Pressed_Rect = Play_Button_Pressed.get_rect()

# -------------------------------------------------------------------------------------------------------------------- #

Quit_Button = pygame.image.load("Assets/Buttons/Quit_Button.png")
Quit_Button_Width = Quit_Button.get_width()
Quit_Button_Height = Quit_Button.get_height()
Quit_Button = MyFunctions.pygame_scale_img(Quit_Button, (int(Quit_Button_Width / 6), int(Quit_Button_Height / 6)))
Quit_Button_Rect = Quit_Button.get_rect()

Quit_Button_Pressed = pygame.image.load("Assets/Buttons/Quit_Button_Pressed.png")
Quit_Button_Pressed_Width = Quit_Button_Pressed.get_width()
Quit_Button_Pressed_Height = Quit_Button_Pressed.get_height()
Quit_Button_Pressed = MyFunctions.pygame_scale_img(Quit_Button_Pressed,
                                           (int(Quit_Button_Pressed_Width / 6), int(Quit_Button_Pressed_Height / 6)))
Quit_Button_Pressed_Rect = Quit_Button_Pressed.get_rect()

# -------------------------------------------------------------------------------------------------------------------- #

Button_1 = pygame.image.load("Assets/Buttons/1_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_2 = pygame.image.load("Assets/Buttons/2_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_3 = pygame.image.load("Assets/Buttons/3_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_4 = pygame.image.load("Assets/Buttons/4_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_E = pygame.image.load("Assets/Buttons/E_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_R = pygame.image.load("Assets/Buttons/R_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_F11 = pygame.image.load("Assets/Buttons/F11_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_Shift = pygame.image.load("Assets/Buttons/Shift_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

Button_G = pygame.image.load("Assets/Buttons/G_Button.png")

# -------------------------------------------------------------------------------------------------------------------- #

