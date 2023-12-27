import pygame

from Constants import Game_Constants
from MyFunctions import MyFunctions

pygame.init()

button_width = pygame.image.load("Assets/Buttons/UI_Buttons/w_button.png").get_width()
button_height = button_width

W_Button = pygame.image.load("Assets/Buttons/UI_Buttons/w_button.png")
W_Button = MyFunctions.pygame_scale_img(W_Button, (int(button_width * Game_Constants.UI_Icons_Scale),
                                                   int(button_height * Game_Constants.UI_Icons_Scale)))
W_Button_Rect = W_Button.get_rect()
W_Button_Rect.center = Game_Constants.grid_spacing * 37, Game_Constants.grid_spacing * 19 - 8


W_Button_Pressed = pygame.image.load("Assets/Buttons/UI_Buttons/w_button_pressed.png")
W_Button_Pressed_Width = W_Button_Pressed.get_width()
W_Button_Pressed_Height = W_Button_Pressed.get_height()
W_Button_Pressed = MyFunctions.pygame_scale_img(W_Button_Pressed,
                                                (int(button_width * Game_Constants.UI_Icons_Scale),
                                                 int(button_height * Game_Constants.UI_Icons_Scale)))
W_Button_Pressed_Rect = W_Button_Pressed.get_rect()
W_Button_Pressed_Rect.center = W_Button_Rect.center


A_Button = pygame.image.load("Assets/Buttons/UI_Buttons/a_button.png")
A_Button = MyFunctions.pygame_scale_img(A_Button, (int(button_width * Game_Constants.UI_Icons_Scale),
                                                   int(button_height * Game_Constants.UI_Icons_Scale)))
A_Button_Rect = A_Button.get_rect()
A_Button_Rect.center = Game_Constants.grid_spacing * 36 - 8, Game_Constants.grid_spacing * 20


A_Button_Pressed = pygame.image.load("Assets/Buttons/UI_Buttons/a_button_pressed.png")
A_Button_Pressed = MyFunctions.pygame_scale_img(A_Button_Pressed, (int(button_width * Game_Constants.UI_Icons_Scale),
                                                                   int(button_height * Game_Constants.UI_Icons_Scale)))
A_Button_Pressed_Rect = A_Button_Pressed.get_rect()
A_Button_Pressed_Rect.center = A_Button_Rect.center


S_Button = pygame.image.load("Assets/Buttons/UI_Buttons/s_button.png")
S_Button = MyFunctions.pygame_scale_img(S_Button, (int(button_width * Game_Constants.UI_Icons_Scale),
                                                   int(button_height * Game_Constants.UI_Icons_Scale)))
S_Button_Rect = S_Button.get_rect()
S_Button_Rect.center = Game_Constants.grid_spacing * 37, Game_Constants.grid_spacing * 20


S_Button_Pressed = pygame.image.load("Assets/Buttons/UI_Buttons/s_button_pressed.png")
S_Button_Pressed = MyFunctions.pygame_scale_img(S_Button_Pressed, (int(button_width * Game_Constants.UI_Icons_Scale),
                                                                   int(button_height * Game_Constants.UI_Icons_Scale)))
S_Button_Pressed_Rect = S_Button_Pressed.get_rect()
S_Button_Pressed_Rect.center = S_Button_Rect.center


D_Button = pygame.image.load("Assets/Buttons/UI_Buttons/d_button.png")
D_Button = MyFunctions.pygame_scale_img(D_Button, (int(button_width * Game_Constants.UI_Icons_Scale),
                                                   int(button_height * Game_Constants.UI_Icons_Scale)))
D_Button_Rect = D_Button.get_rect()
D_Button_Rect.center = Game_Constants.grid_spacing * 38 + 8, Game_Constants.grid_spacing * 20


D_Button_Pressed = pygame.image.load("Assets/Buttons/UI_Buttons/d_button_pressed.png")
D_Button_Pressed = MyFunctions.pygame_scale_img(D_Button_Pressed, (int(button_width * Game_Constants.UI_Icons_Scale),
                                                                   int(button_height * Game_Constants.UI_Icons_Scale)))
D_Button_Pressed_Rect = D_Button_Pressed.get_rect()
D_Button_Pressed_Rect.center = D_Button_Rect.center

Teleport_Orb_Active = pygame.image.load("Assets/Orbs/Teleport_Orb_Active.png")
Teleport_Orb_Active = MyFunctions.pygame_scale_img(Teleport_Orb_Active, 2)
Teleport_Orb_Active_Rect = Teleport_Orb_Active.get_rect()
Teleport_Orb_Active_Rect.center = Game_Constants.grid_spacing * 7 - 10, Game_Constants.grid_spacing * 2 - 6

Teleport_Orb_Deactive = pygame.image.load("Assets/Orbs/Teleport_Orb_Deactive.png")
Teleport_Orb_Deactive = MyFunctions.pygame_scale_img(Teleport_Orb_Deactive, 2)
Teleport_Orb_Deactive_Rect = Teleport_Orb_Deactive.get_rect()
Teleport_Orb_Deactive_Rect.center = Teleport_Orb_Active_Rect.center

Ultimate_Orb_Active = pygame.image.load("Assets/Orbs/Ultimate_Orb_Active.png")
Ultimate_Orb_Active = MyFunctions.pygame_scale_img(Ultimate_Orb_Active, 2)
Ultimate_Orb_Active_Rect = Ultimate_Orb_Active.get_rect()
Ultimate_Orb_Active_Rect.center = Game_Constants.grid_spacing * 8 - 10, Game_Constants.grid_spacing * 2 - 6

Ultimate_Orb_Deactive = pygame.image.load("Assets/Orbs/Ultimate_Orb_Deactive.png")
Ultimate_Orb_Deactive = MyFunctions.pygame_scale_img(Ultimate_Orb_Deactive, 2)
Ultimate_Orb_Deactive_Rect = Ultimate_Orb_Deactive.get_rect()
Ultimate_Orb_Deactive_Rect.center = Ultimate_Orb_Active_Rect.center

Regeneration_Orb_Active = pygame.image.load("Assets/Orbs/Regeneration_Orb_Active.png")
Regeneration_Orb_Active = MyFunctions.pygame_scale_img(Regeneration_Orb_Active, 2)
Regeneration_Orb_Active_Rect = Regeneration_Orb_Active.get_rect()
Regeneration_Orb_Active_Rect.center = Game_Constants.grid_spacing * 7 + 7, Game_Constants.grid_spacing * 3 - 10

Regeneration_Orb_Deactive = pygame.image.load("Assets/Orbs/Regeneration_Orb_Deactive.png")
Regeneration_Orb_Deactive = MyFunctions.pygame_scale_img(Regeneration_Orb_Deactive, 2)
Regeneration_Orb_Deactive_Rect = Regeneration_Orb_Deactive.get_rect()
Regeneration_Orb_Deactive_Rect.center = Regeneration_Orb_Active_Rect.center
