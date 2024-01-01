import pygame

from MyFunctions import MyFunctions
from Constants import Game_Constants

pygame.init()

Blank_Player_Image = MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Original_Tiles/Blank_Image.png"), Game_Constants.SCALE)

Player_Idle_Animation = [
    MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Original_Tiles/tile{i:0>3}.png"),
                                 Game_Constants.SCALE) for i in range(6)]

Player_Running_Animation = [
    MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Original_Tiles/tile{i:0>3}.png"),
                                 Game_Constants.SCALE) for i in range(9, 17)]

Player_Appering_Animation = [
    MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Appearing_Animation/Appear{i}.png"),
                                 Game_Constants.SCALE) for i in range(1, 4)]

Player_First_Dash = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Nicolau_Dash/"
                                                                    f"first_dash-{i}.png"),
                                                  Game_Constants.SCALE) for i in range(10)]

Player_Second_Dash = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Nicolau_Dash/"
                                                                     f"second_dash-{i}.png"),
                                                   Game_Constants.SCALE) for i in range(6)]

Player_First_Dash_Ultimate = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/"
                                                                             f"Default_Character"
                                                                             f"/Nicolau_Dash_Ultimate/first_dash-"
                                                                             f"{i}.png"),
                                                           Game_Constants.SCALE) for i in range(10)]

Player_Second_Dash_Ultimate = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/"
                                                                             f"Default_Character"
                                                                             f"/Nicolau_Dash_Ultimate/second_dash-"
                                                                             f"{i}.png"),
                                                           Game_Constants.SCALE) for i in range(6)]

Player_Global_Teleport_Ending = [MyFunctions.pygame_scale_img(pygame.image.load(f""
                                                                                f"Assets/Default_Character"
                                                                                f"/Nicolau_Global_Teleport"
                                                                                f"/Nicolau_Global_Teleport-{i}.png"),
                                                              Game_Constants.SCALE) for i in range(8)]

Player_Global_Teleport_Start = Player_Global_Teleport_Ending[::-1]

Player_Idle_Ultimate_Animation = [
    MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Nicolau_Ultimate_Skin/tile{i:0>3}.png"),
                                 Game_Constants.SCALE) for i in range(6)]

Player_Running_Ultimate_Animation = [
    MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/Nicolau_Ultimate_Skin/tile{i:0>3}.png"),
                                 Game_Constants.SCALE) for i in range(9, 17)]

Player_Global_Ultimate_Teleport_Ending = [
    MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Default_Character/"
                                                   f"Nicolau_Global_Teleport_Ultimate/"
                                                   f"Nicolau_Global_Teleport_Ultimate-{i}.png"),
                                 Game_Constants.SCALE) for i in range(7)]

Player_Global_Ultimate_Teleport_Start = Player_Global_Ultimate_Teleport_Ending[::-1]

Player_Death_Animation = [MyFunctions.pygame_scale_img(
    pygame.image.load(f"Assets/Default_Character/Original_Tiles/tile{i:0>3}.png"), Game_Constants.SCALE)
    for i in range(27, 37)]

Health_bar = MyFunctions.pygame_scale_img(pygame.image.load("Assets/"
                                                            "Default_Character/"
                                                            "Original_Assets/Health_Bar.png"), Game_Constants.SCALE)
