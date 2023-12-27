import pygame

from MyFunctions import MyFunctions
from Constants import Game_Constants

pygame.init()

Coin = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Items/Coins/Coin/tile{i:0>3}.png"),
                                     Game_Constants.item_scale) for i in range(5)]

Coin_Width = Coin[0].get_width()
Coin_Height = Coin[0].get_height()

# Coin Image Used in Player Info :
Static_Coin = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Items/Coins/Coin/tile{i:0>3}.png"),
                                     (int(Coin_Width * Game_Constants.static_coin_scale),
                                      int(Coin_Height * Game_Constants.static_coin_scale))) for i in range(5)]

Silver_Coin = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Items/Coins/Silver_Coin/tile{i:0>3}.png"),
                                     Game_Constants.item_scale) for i in range(5)]

Red_Coin = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Items/Coins/Red_Coin/tile{i:0>3}.png"),
                                     Game_Constants.item_scale) for i in range(5)]

Emerald = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Items/Coins/Emerald/tile{i:0>3}.png"),
                                     Game_Constants.item_scale) for i in range(4)]

Red_Potion = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Items/Potions/Red_Potion/tile{i:0>3}.png"),
                                     Game_Constants.item_scale) for i in range(8)]
