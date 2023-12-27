import pygame

import MyFunctions.MyFunctions

pygame.init()

Pointer = pygame.image.load("Assets/Cursors/Game_Cursor.png")

Board_Leaf_Icon = pygame.image.load("Assets/Game_Icon/Board_Leaf.png")

Tiny_Board_Leaf = pygame.image.load("Assets/Game_Icon/Tiny_Board_Leaf.png")

Gray_Square = pygame.image.load("Assets/Game_Icon/Gray_Square.png")

First_World_Mask = pygame.image.load("Assets/Background/Mask/First_World_Mask(1).png")

Black_Tile = pygame.image.load("Assets/Background/Tile_Maps/Black_Tile.png")

Tiny_Grass = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Tiny_Grass.png")
Large_Grass = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Large_Grass.png")
White_Flowers = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Grass_White_Flowers.png")
Yellow_Flowers = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Grass_Yellow_Flowers.png")

Outside_Wall_Ruin_1 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Top(1).png")
Outside_Wall_Ruin_2 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Top(2).png")

Outside_Wall_Top_Left = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Top_Left.png")
Outside_Wall_Top_Right = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Top_Right.png")

Outside_Wall_Bottom_Right = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Bottom_Right.png")
Outside_Wall_Bottom_Left = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Bottom_Left.png")
Outside_Wall_Bottom = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Bottom.png")

Unitary_Stone_Path_1 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Unitary_Stone_Path(1).png")
Unitary_Stone_Path_2 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Unitary_Stone_Path(2).png")
Unitary_Stone_Path_3 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Unitary_Stone_Path(3).png")

Outside_Wall_Left_1 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Left.png")
Outside_Wall_Left_2 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Left(2).png")

Outside_Wall_Right_1 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Right.png")
Outside_Wall_Right_2 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Right(2).png")

Bigger_Outside_Wall = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Bigger_Outside_Wall.png")
Outside_Wall_Window = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Outside_Wall_Window.png")

Stone_Tile_Horizontal_Path = pygame.image.load("Assets/Background/Tile_Maps/"
                                               "Outside_Ruins/Stone_Tile_Horizontal_Path.png")
Stone_Tile_Vertical_Path_1 = pygame.image.load("Assets/Background/Tile_Maps/"
                                               "Outside_Ruins/Stone_Tile_Vertical_Path(1).png")
Stone_Tile_Vertical_Path_2 = pygame.image.load("Assets/Background/Tile_Maps/"
                                               "Outside_Ruins/Stone_Tile_Vertical_Path(2).png")
Stone_Tile_Vertical_Path_3 = pygame.image.load("Assets/Background/Tile_Maps/"
                                               "Outside_Ruins/Stone_Tile_Vertical_Path(3).png")

Portal = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Portal.png")
Portal_With_Door_Closed = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Portal_With_Door_Closed.png")
Portal_With_Door_Open = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Portal_With_Door_Open.png")

Tombstone_1 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Tombstone.png")
Tombstone_2 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Tombstone(1).png")
Tombstone_3 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Tombstone(2).png")
Tombstone_4 = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Tombstone(3).png")

Altar = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Altar.png")
Statue = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Statue.png")
Tree = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Tree.png")

Stone_Floor = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Stone_Floor.png")

Tutorial_Sign = pygame.image.load("Assets/Background/Tile_Maps/Outside_Ruins/Sign.png")
Tutorial_Sign_Width = Tutorial_Sign.get_width()
Tutorial_Sign_Height = Tutorial_Sign.get_height()
Tutorial_Sign = MyFunctions.MyFunctions.pygame_scale_img(Tutorial_Sign, (int(Tutorial_Sign_Width * 1.5),
                                                                         int(Tutorial_Sign_Height * 1.5)))

# ------------------------------------------------------------------------------------------------- #

Dungeon_Purple_Floor = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Floor_Tile.png"), 2)

Dungeon_Front_Wall = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Front_Dungeon_Wall.png"), 2)

Dungeon_Back_Wall = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Back_Dungeon_Wall.png"), 2)

Dungeon_Candle_Holder = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Candle_Holder.png"), 2)

Dungeon_Closed_Door = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Dungeon_Closed_Door.png"), 2)

Dungeon_Opened_Door = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Dungeon_Opened_Door.png"), 2)

Dungeon_Right_Wall = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Right_Wall_Dungeon.png"), 2)

Dungeon_Left_Wall = MyFunctions.MyFunctions.pygame_scale_img(
    pygame.image.load("Assets/Background/Tile_Maps/Dungeon/Left_Wall_Dungeon.png"), 2)
