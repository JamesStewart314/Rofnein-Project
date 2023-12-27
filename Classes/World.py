import pygame

from Assets import Background_Images
from Constants import Game_Constants

pygame.init()


class World:

    tiles_dict = {-1: Background_Images.Black_Tile, 0: Background_Images.Tiny_Grass,
                  1: Background_Images.Large_Grass, 2: Background_Images.White_Flowers,
                  3: Background_Images.Yellow_Flowers, 4: Background_Images.Outside_Wall_Ruin_1,
                  5: Background_Images.Outside_Wall_Ruin_2, 6: Background_Images.Bigger_Outside_Wall,
                  7: Background_Images.Outside_Wall_Window, 8: Background_Images.Stone_Tile_Horizontal_Path,
                  9: Background_Images.Stone_Tile_Vertical_Path_1, 10: Background_Images.Stone_Tile_Vertical_Path_2,
                  11: Background_Images.Stone_Tile_Vertical_Path_3, 12: Background_Images.Outside_Wall_Top_Left,
                  13: Background_Images.Outside_Wall_Left_1, 14: Background_Images.Outside_Wall_Left_2,
                  15: Background_Images.Portal, 16: Background_Images.Portal_With_Door_Closed,
                  17: Background_Images.Portal_With_Door_Open, 18: Background_Images.Outside_Wall_Right_1,
                  19: Background_Images.Outside_Wall_Right_2, 20: Background_Images.Outside_Wall_Top_Right,
                  21: Background_Images.Outside_Wall_Bottom_Left, 22: Background_Images.Outside_Wall_Bottom,
                  23: Background_Images.Outside_Wall_Bottom_Right, 24: Background_Images.Unitary_Stone_Path_1,
                  25: Background_Images.Unitary_Stone_Path_2, 26: Background_Images.Unitary_Stone_Path_3,
                  27: Background_Images.Tombstone_1, 28: Background_Images.Tombstone_2,
                  29: Background_Images.Tombstone_3, 30: Background_Images.Tombstone_4,
                  31: Background_Images.Altar, 32: Background_Images.Statue, 33: Background_Images.Tree,
                  34: Background_Images.Stone_Floor, 35: Background_Images.Dungeon_Purple_Floor,
                  36: Background_Images.Dungeon_Front_Wall, 37: Background_Images.Dungeon_Back_Wall,
                  38: Background_Images.Dungeon_Left_Wall, 39: Background_Images.Dungeon_Right_Wall,
                  40: Background_Images.Dungeon_Closed_Door, 41: Background_Images.Dungeon_Candle_Holder,
                  42: Background_Images.Dungeon_Opened_Door}

    def __init__(self):
        self.map_tiles = []

    def process_data(self, data: list) -> None:
        # Iterate Through Each Value in Level Data File :
        for coordinate_y, row in enumerate(data):
            for coordinate_x, tile in enumerate(row):
                image = World.tiles_dict.get(tile, None)

                if image:
                    image_rect = image.get_rect()

                    image_rect.x, image_rect.y = (Game_Constants.grid_spacing * coordinate_x,
                                         Game_Constants.grid_spacing * coordinate_y)

                    tile_data = [image, image_rect, image_rect.center]

                    # Add Image Data to Main Tiles List :
                    self.map_tiles.append(tile_data)

    def draw(self, surface: object) -> None:
        for tile in self.map_tiles:
            surface.blit(tile[0], tile[1])
