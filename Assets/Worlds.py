import pygame
import csv

import Assets.Player_Images

from Assets import Titles_Images
from Assets import Masks
from Assets import Buttons
from Constants import Game_Constants
from Classes import Character
from Classes import Fade
from Classes import Familiar
from Classes import Item
from Classes import Monster
from Classes import Sign
from Classes import ShowFloatingText
from Classes import World
from MyFunctions import MyFunctions_2

pygame.init()

Screen = pygame.display.set_mode((Game_Constants.Window_width, Game_Constants.Window_height))

current_level = 1

raid_index = 0

current_mask = Masks.First_World_Mask_1

draw_mask = True

end_game = False

current_player = Character.Character(Game_Constants.Window_width / 2 - 16 * Game_Constants.grid_spacing - 16,
                                     Game_Constants.Window_height / 2 + 18, Game_Constants.player_standard_health)

familiar = Familiar.Familiar(current_player.rect.x, current_player.rect.y, "bat")

Fade_Animation = [Fade.Fade("fade_in", change_rate=2.5), Fade.Fade("fade_out", change_rate=2.5)]
Current_Fade_Animation = Fade_Animation[1]
Do_Fade = 1
Start_Fade = True

button_3 = ShowFloatingText.FloatingText(current_player.rect.centerx, current_player.rect.y - 30,
                                                 Buttons.Button_3, speed=0.3, amplitude=4)
button_4 = ShowFloatingText.FloatingText(current_player.rect.centerx, current_player.rect.y - 30,
                                                 Buttons.Button_4, speed=0.3, amplitude=4)

# ------------------------------------------- WORLD GENERATION ------------------------------------ #

World_Data = []

for row in range(Game_Constants.Map_Rows):
    First_World_Row = [-2] * Game_Constants.Map_Columns
    World_Data.append(First_World_Row)

with open(f"Levels/Level_{current_level}.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=";")

    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            World_Data[x][y] = int(tile)

# ---------------------------------------- FIRST WORLD OBJECTS ------------------------------------- #

First_World_Objects = []
First_World_Rect_Interactions = []
First_World_Trees = []
Stone_Tiles_Rects = []

Tutorial_Sign = Sign.Sign(Game_Constants.grid_spacing * 11 + 16, Game_Constants.grid_spacing * 4)
First_World_Objects.append((None, Tutorial_Sign.hitbox, True))

Statue = World.World.tiles_dict.__getitem__(32)
Statue_rect = Statue.get_rect()
Statue_rect.x, Statue_rect.y = Game_Constants.grid_spacing * 19 + 14, Game_Constants.grid_spacing * 6
Statue = (Statue, Statue_rect, True)
First_World_Objects.append(Statue)

Altar = World.World.tiles_dict.__getitem__(31)
Altar_rect = Altar.get_rect()
Altar_rect.x, Altar_rect.y = Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing * 11
Altar = (Altar, Altar_rect, False)
First_World_Objects.append(Altar)

Tombstone = World.World.tiles_dict.__getitem__(30)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 8 + 3, Game_Constants.grid_spacing * 14
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(29)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 10 + 1, Game_Constants.grid_spacing * 14 + 10
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(28)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 12 + 1, Game_Constants.grid_spacing * 14 + 5
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(29)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 14 + 1, Game_Constants.grid_spacing * 14 + 10
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(30)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 16 + 3, Game_Constants.grid_spacing * 14
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(27)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 8, Game_Constants.grid_spacing * 15
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(27)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 10, Game_Constants.grid_spacing * 15
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(27)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 12, Game_Constants.grid_spacing * 15
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(27)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 14, Game_Constants.grid_spacing * 15
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tombstone = World.World.tiles_dict.__getitem__(27)
Tombstone_rect = Tombstone.get_rect()
Tombstone_rect.x, Tombstone_rect.y = Game_Constants.grid_spacing * 16, Game_Constants.grid_spacing * 15
Tombstone = (Tombstone, Tombstone_rect, True)
First_World_Objects.append(Tombstone)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 36, Game_Constants.grid_spacing * 15
Tree = (Tree, Tree_rect, False)
First_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
First_World_Objects.append(Tree_Rect)

Wall_Rect_1 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 19, 44)
Wall_Rect_1 = (None, Wall_Rect_1, True)
First_World_Objects.append(Wall_Rect_1)

Wall_Rect_1 = pygame.rect.Rect(Game_Constants.grid_spacing * 21, 0, Game_Constants.grid_spacing * 19, 44)
Wall_Rect_1 = (None, Wall_Rect_1, True)
First_World_Objects.append(Wall_Rect_1)

Wall_Rect_2 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing - 30, Game_Constants.grid_spacing * 22)
Wall_Rect_2 = (None, Wall_Rect_2, True)
First_World_Objects.append(Wall_Rect_2)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 40, 0,
                               Game_Constants.grid_spacing, Game_Constants.grid_spacing * 22)
Wall_Rect_3 = (None, Wall_Rect_3, True)
First_World_Objects.append(Wall_Rect_3)

Wall_Rect_4 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 22, Game_Constants.grid_spacing * 40,
                               Game_Constants.grid_spacing)
Wall_Rect_4 = (None, Wall_Rect_4, True)
First_World_Objects.append(Wall_Rect_4)

Closed_Door = World.World.tiles_dict.__getitem__(16)
Closed_Door_Rect = Closed_Door.get_rect()
Closed_Door_Rect.height -= 20
Closed_Door_Rect.x, Closed_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
Interaction_Door_Rect = pygame.rect.Rect(Closed_Door_Rect.x, Closed_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                         Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)
Closed_Door = [Closed_Door, Closed_Door_Rect, True]  # Need to be mutable
First_World_Objects.append(Closed_Door)

# The first argument informs the sprites and collisions of the door, the second informs the collision rectangle, the
# third informs whether the interaction between the player and the event has already occurred and the fourth informs
# the interaction function:

First_World_Rect_Interactions.append([Closed_Door, World.World.tiles_dict.__getitem__(17), Interaction_Door_Rect, False,
                                      MyFunctions_2.open_door])

# Stone Tiles Rects :
STR_1 = pygame.rect.Rect(Game_Constants.grid_spacing * 10, Game_Constants.grid_spacing * 3,
                         Game_Constants.grid_spacing * 20, Game_Constants.grid_spacing / 3)
STR_2 = pygame.rect.Rect(Game_Constants.grid_spacing * 10, Game_Constants.grid_spacing * 3,
                         Game_Constants.grid_spacing, Game_Constants.grid_spacing * 8 - 24)
STR_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 29, Game_Constants.grid_spacing * 3,
                         Game_Constants.grid_spacing, Game_Constants.grid_spacing * 8 - 24)
STR_4 = pygame.rect.Rect(Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing * 11,
                         Game_Constants.grid_spacing * 28, Game_Constants.grid_spacing * 2 - 24)
STR_5 = pygame.rect.Rect(Game_Constants.grid_spacing * 19, Game_Constants.grid_spacing * 2,
                         Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing * 2 - 24)
STR_6 = pygame.rect.Rect(Game_Constants.grid_spacing * 20, Game_Constants.grid_spacing * 11,
                         Game_Constants.grid_spacing * 1, Game_Constants.grid_spacing * 8 - 24)
STR_7 = pygame.rect.Rect(Game_Constants.grid_spacing * 8, Game_Constants.grid_spacing * 17,
                         Game_Constants.grid_spacing * 12, Game_Constants.grid_spacing * 2 - 24)

Stone_Tiles_Rects.extend([STR_1, STR_2, STR_3, STR_4, STR_5, STR_6, STR_7])

# ------------------------------------------------------------------------------------------------- #

# --------------------------------------- SECOND WORLD OBJECTS ------------------------------------ #

Second_World_Objects = []
Second_World_Rect_Interactions = []
Second_World_Trees = []

Candle_Holder = World.World.tiles_dict.__getitem__(41)
Candle_Holder_rect = Candle_Holder.get_rect()
Candle_Holder_rect.x, Candle_Holder_rect.y = Game_Constants.grid_spacing * 18, Game_Constants.grid_spacing
Candle_Holder_rect.height -= 20
Candle_Holder = (Candle_Holder, Candle_Holder_rect, True)
Second_World_Objects.append(Candle_Holder)

Candle_Holder = World.World.tiles_dict.__getitem__(41)
Candle_Holder_rect = Candle_Holder.get_rect()
Candle_Holder_rect.x, Candle_Holder_rect.y = Game_Constants.grid_spacing * 21 + 12, Game_Constants.grid_spacing
Candle_Holder_rect.height -= 20
Candle_Holder = (Candle_Holder, Candle_Holder_rect, True)
Second_World_Objects.append(Candle_Holder)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 33, Game_Constants.grid_spacing * 13
Tree = (Tree, Tree_rect, False)
Second_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
Second_World_Objects.append(Tree_Rect)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 37, Game_Constants.grid_spacing * 3
Tree = (Tree, Tree_rect, False)
Second_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
Second_World_Objects.append(Tree_Rect)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 32, Game_Constants.grid_spacing
Tree = (Tree, Tree_rect, False)
Second_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
Second_World_Objects.append(Tree_Rect)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 8, Game_Constants.grid_spacing * 5
Tree = (Tree, Tree_rect, False)
Second_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
Second_World_Objects.append(Tree_Rect)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 6, Game_Constants.grid_spacing * 14
Tree = (Tree, Tree_rect, False)
Second_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
Second_World_Objects.append(Tree_Rect)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing
Tree = (Tree, Tree_rect, False)
Second_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
Second_World_Objects.append(Tree_Rect)

Tree = World.World.tiles_dict.__getitem__(33)
Tree_rect = Tree.get_rect()
Tree_rect.x, Tree_rect.y = Game_Constants.grid_spacing * 13, Game_Constants.grid_spacing / 10
Tree = (Tree, Tree_rect, False)
Second_World_Trees.append(Tree)

Tree_Rect = Tree_rect.copy()
Tree_Rect.height /= 10
Tree_Rect.y += 8.5 * Tree_Rect.height
Tree_Rect.width /= 10
Tree_Rect.x += 4.2 * Tree_Rect.width
Tree_Rect = (None, Tree_Rect, True)
Second_World_Objects.append(Tree_Rect)

Wall_Rect_1 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 19, 44)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Second_World_Objects.append(Wall_Rect_1)

Wall_Rect_1 = pygame.rect.Rect(Game_Constants.grid_spacing * 21, 0, Game_Constants.grid_spacing * 19, 44)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Second_World_Objects.append(Wall_Rect_1)

Wall_Rect_2 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing - 30, Game_Constants.grid_spacing * 22)
Wall_Rect_2 = (None, Wall_Rect_2, True)
Second_World_Objects.append(Wall_Rect_2)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 40, 0,
                               Game_Constants.grid_spacing, Game_Constants.grid_spacing * 22)
Wall_Rect_3 = (None, Wall_Rect_3, True)
Second_World_Objects.append(Wall_Rect_3)

Wall_Rect_4 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 22, Game_Constants.grid_spacing * 40,
                               Game_Constants.grid_spacing)
Wall_Rect_4 = (None, Wall_Rect_4, True)
Second_World_Objects.append(Wall_Rect_4)

Closed_Dungeon_Door = World.World.tiles_dict.__getitem__(40)
Closed_Dungeon_Door_Rect = Closed_Dungeon_Door.get_rect()
Closed_Dungeon_Door_Rect.height -= 20
Closed_Dungeon_Door_Rect.x, Closed_Dungeon_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
Interaction_Door_Rect = pygame.rect.Rect(Closed_Dungeon_Door_Rect.x,
                                         Closed_Dungeon_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                         Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)

# [ < Sprite >, < Rectangle >, < Collision > ] :
Closed_Dungeon_Door = [Closed_Dungeon_Door, Closed_Dungeon_Door_Rect, True]  # Need to be mutable
Second_World_Objects.append(Closed_Dungeon_Door)

# [ < Previous Object >, < Open Door Sprite >, < Interaction Rectangle >,
# < Interaction ( tells if the interaction happened ) >, < Function of Interaction > ] :
Second_World_Rect_Interactions.append([Closed_Dungeon_Door, World.World.tiles_dict.__getitem__(42),
                                       Interaction_Door_Rect, False, MyFunctions_2.open_door])

# --------------------------------------- SECOND WORLD ENEMIES ------------------------------------ #

Second_World_Enemies = []

Imp_1 = Monster.Monster(Game_Constants.grid_spacing * 10, Game_Constants.grid_spacing * 7, "imp")
Second_World_Enemies.append(Imp_1)

Imp_2 = Monster.Monster(Game_Constants.grid_spacing * 36 + 16, Game_Constants.grid_spacing * 4, "imp")
Second_World_Enemies.append(Imp_2)

Imp_3 = Monster.Monster(Game_Constants.grid_spacing * 8, Game_Constants.grid_spacing * 17, "imp")
Second_World_Enemies.append(Imp_3)

# ------------------------------------------------------------------------------------------------- #

# ---------------------------------------- THIRD WORLD OBJECTS ------------------------------------ #

Third_World_Objects = []
Third_World_Rect_Interactions = []

Wall_Rect_1 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 19 - 8, Game_Constants.grid_spacing * 9)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Third_World_Objects.append(Wall_Rect_1)

Wall_Rect_2 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 13 - 16,
                               Game_Constants.grid_spacing * 19 - 8, Game_Constants.grid_spacing * 9)
Wall_Rect_2 = (None, Wall_Rect_2, True)
Third_World_Objects.append(Wall_Rect_2)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 21 + 8, 0,
                               Game_Constants.grid_spacing * 19, Game_Constants.grid_spacing * 9)
Wall_Rect_3 = (None, Wall_Rect_3, True)
Third_World_Objects.append(Wall_Rect_3)

Wall_Rect_4 = pygame.rect.Rect(Game_Constants.grid_spacing * 21 + 8, Game_Constants.grid_spacing * 13 - 16,
                               Game_Constants.grid_spacing * 19, Game_Constants.grid_spacing * 9)
Wall_Rect_4 = (None, Wall_Rect_4, True)
Third_World_Objects.append(Wall_Rect_4)

Closed_Dungeon_Door = World.World.tiles_dict.__getitem__(40)
Closed_Dungeon_Door_Rect = Closed_Dungeon_Door.get_rect()
Closed_Dungeon_Door_Rect.height -= 20
Closed_Dungeon_Door_Rect.x, Closed_Dungeon_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
Interaction_Door_Rect = pygame.rect.Rect(Closed_Dungeon_Door_Rect.x,
                                         Closed_Dungeon_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                         Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)

# [ < Sprite >, < Rectangle >, < Collision > ] :
Closed_Dungeon_Door = [Closed_Dungeon_Door, Closed_Dungeon_Door_Rect, True]  # Need to be mutable
Third_World_Objects.append(Closed_Dungeon_Door)

# [ < Previous Object >, < Open Door Sprite >, < Interaction Rectangle >,
# < Interaction ( tells if the interaction happened ) >, < Function of Interaction > ] :
Third_World_Rect_Interactions.append([Closed_Dungeon_Door, World.World.tiles_dict.__getitem__(42),
                                      Interaction_Door_Rect, False, MyFunctions_2.open_door])

Door_Rect = pygame.rect.Rect(Game_Constants.grid_spacing * 19, Game_Constants.grid_spacing * 21 + 8,
                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing * 2)
Door_Rect = (None, Door_Rect, True)
Third_World_Objects.append(Door_Rect)

# ------------------------------------------------------------------------------------------------- #

# --------------------------------------- FOURTH WORLD OBJECTS ------------------------------------ #

Fourth_World_Objects = []
Fourth_World_Interactions = []

Wall_Rect_1 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 40, Game_Constants.grid_spacing - 16)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Fourth_World_Objects.append(Wall_Rect_1)

Wall_Rect_2 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing - 8, Game_Constants.grid_spacing * 22)
Wall_Rect_2 = (None, Wall_Rect_2, True)
Fourth_World_Objects.append(Wall_Rect_2)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 39 + 8, 0,
                               Game_Constants.grid_spacing, Game_Constants.grid_spacing * 10 - 16)
Wall_Rect_3 = (None, Wall_Rect_3, True)
Fourth_World_Objects.append(Wall_Rect_3)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 39 + 8, Game_Constants.grid_spacing * 13 - 16,
                               Game_Constants.grid_spacing, Game_Constants.grid_spacing * 8)
Wall_Rect_3 = (None, Wall_Rect_3, True)
Fourth_World_Objects.append(Wall_Rect_3)

Wall_Rect_4 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 21 + 16, Game_Constants.grid_spacing * 40,
                               Game_Constants.grid_spacing)
Wall_Rect_4 = (None, Wall_Rect_4, True)
Fourth_World_Objects.append(Wall_Rect_4)

# ------------------------------------------------------------------------------------------------- #

# --------------------------------------- FIFTH WORLD OBJECTS ------------------------------------- #

Fifth_World_Objects = []
Fifth_World_Interactions = []

Wall_Rect_1 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 40, Game_Constants.grid_spacing - 16)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Fifth_World_Objects.append(Wall_Rect_1)

Wall_Rect_2 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing - 8, Game_Constants.grid_spacing * 10 - 16)
Wall_Rect_2 = (None, Wall_Rect_2, True)
Fifth_World_Objects.append(Wall_Rect_2)

Wall_Rect_2 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 13 - 16, Game_Constants.grid_spacing - 8,
                               Game_Constants.grid_spacing * 8)
Wall_Rect_2 = (None, Wall_Rect_2, True)
Fifth_World_Objects.append(Wall_Rect_2)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 39 + 8, 0,
                               Game_Constants.grid_spacing, Game_Constants.grid_spacing * 22)
Wall_Rect_3 = (None, Wall_Rect_3, True)
Fifth_World_Objects.append(Wall_Rect_3)

Wall_Rect_4 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 21 + 16, Game_Constants.grid_spacing * 40,
                               Game_Constants.grid_spacing)
Wall_Rect_4 = (None, Wall_Rect_4, True)
Fifth_World_Objects.append(Wall_Rect_4)

# ------------------------------------------------------------------------------------------------- #

# --------------------------------------- SIXTH WORLD OBJECTS ------------------------------------- #

Sixth_World_Objects = []
Sixth_World_Interactions = []

Wall_Rect_1 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 19, 44)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Sixth_World_Objects.append(Wall_Rect_1)

Wall_Rect_1 = pygame.rect.Rect(Game_Constants.grid_spacing * 21, 0, Game_Constants.grid_spacing * 19, 44)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Sixth_World_Objects.append(Wall_Rect_1)

Wall_Rect_2 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing - 8, Game_Constants.grid_spacing * 22)
Wall_Rect_2 = (None, Wall_Rect_2, True)
Sixth_World_Objects.append(Wall_Rect_2)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 40 - 24, 0,
                               Game_Constants.grid_spacing, Game_Constants.grid_spacing * 22)
Wall_Rect_3 = (None, Wall_Rect_3, True)
Sixth_World_Objects.append(Wall_Rect_3)

Wall_Rect_4 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 22 - 16, Game_Constants.grid_spacing * 40,
                               Game_Constants.grid_spacing)
Wall_Rect_4 = (None, Wall_Rect_4, True)
Sixth_World_Objects.append(Wall_Rect_4)

Closed_Dungeon_Door = World.World.tiles_dict.__getitem__(40)
Closed_Dungeon_Door_Rect = Closed_Dungeon_Door.get_rect()
Closed_Dungeon_Door_Rect.height -= 20
Closed_Dungeon_Door_Rect.x, Closed_Dungeon_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
Interaction_Door_Rect = pygame.rect.Rect(Closed_Dungeon_Door_Rect.x,
                                         Closed_Dungeon_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                         Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)

# [ < Sprite >, < Rectangle >, < Collision > ] :
Closed_Dungeon_Door = [Closed_Dungeon_Door, Closed_Dungeon_Door_Rect, True]  # Need to be mutable
Sixth_World_Objects.append(Closed_Dungeon_Door)

# [ < Previous Object >, < Open Door Sprite >, < Interaction Rectangle >,
# < Interaction ( tells if the interaction happened ) >, < Function of Interaction > ] :
Sixth_World_Interactions.append([Closed_Dungeon_Door, World.World.tiles_dict.__getitem__(42),
                                 Interaction_Door_Rect, False, MyFunctions_2.open_door])

"""Door_Rect = pygame.rect.Rect(Game_Constants.grid_spacing * 19, Game_Constants.grid_spacing * 21 + 8,
                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing * 2)
Door_Rect = (None, Door_Rect, True)
Sixth_World_Objects.append(Door_Rect)"""

# ------------------------------------------------------------------------------------------------- #

# --------------------------------------- SEVENTH WORLD OBJECTS ----------------------------------- #

Seventh_World_Objects = []
Seventh_World_Interactions = []

Wall_Rect_1 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing * 40, Game_Constants.grid_spacing - 16)
Wall_Rect_1 = (None, Wall_Rect_1, True)
Seventh_World_Objects.append(Wall_Rect_1)

Wall_Rect_2 = pygame.rect.Rect(0, 0, Game_Constants.grid_spacing - 8, Game_Constants.grid_spacing * 22)
Wall_Rect_2 = (None, Wall_Rect_2, True)
Seventh_World_Objects.append(Wall_Rect_2)

Wall_Rect_3 = pygame.rect.Rect(Game_Constants.grid_spacing * 40 - 24, 0,
                               Game_Constants.grid_spacing, Game_Constants.grid_spacing * 22)
Wall_Rect_3 = (None, Wall_Rect_3, True)
Seventh_World_Objects.append(Wall_Rect_3)

Wall_Rect_4 = pygame.rect.Rect(0, Game_Constants.grid_spacing * 22 - 16, Game_Constants.grid_spacing * 40,
                               Game_Constants.grid_spacing)
Wall_Rect_4 = (None, Wall_Rect_4, True)
Seventh_World_Objects.append(Wall_Rect_4)

# ------------------------------------------------- SEVENTH WORLD ENEMIES ------------------------------------------- #

Seventh_World_Enemies = []

Demon_Boss = Monster.Monster(Game_Constants.Window_width / 2, Game_Constants.Window_height / 2 - 200, "demon")
Seventh_World_Enemies.append(Demon_Boss)

# ------------------------------------------------------------------------------------------------------------------ #

Level_Objects = {1: First_World_Objects, 2: Second_World_Objects, 3: Third_World_Objects, 4: Fourth_World_Objects,
                 5: Fifth_World_Objects, 6: Sixth_World_Objects, 7: Seventh_World_Objects}

Level_Interactions = {1: First_World_Rect_Interactions, 2: Second_World_Rect_Interactions,
                      3: Third_World_Rect_Interactions, 4: Fourth_World_Interactions,
                      5: Fifth_World_Interactions, 6: Sixth_World_Interactions,
                      7: Seventh_World_Interactions}

# Square to get to the next level :
Next_Level_Location = {1: ((pygame.rect.Rect(Game_Constants.grid_spacing * 19, 0,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing), 2), None),

                       2: ((pygame.rect.Rect(Game_Constants.grid_spacing * 19, 0,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing), 3),
                           (
                               pygame.rect.Rect(Game_Constants.grid_spacing * 19 + 16,
                                                Game_Constants.grid_spacing * 22 - 8,
                                                Game_Constants.grid_spacing, Game_Constants.grid_spacing), 1),
                           None),

                       3: ((pygame.rect.Rect(Game_Constants.grid_spacing * (-1), Game_Constants.grid_spacing * 10,
                                             Game_Constants.grid_spacing, Game_Constants.grid_spacing * 2), 4),
                           (pygame.rect.Rect(Game_Constants.grid_spacing * 40, Game_Constants.grid_spacing * 10,
                                             Game_Constants.grid_spacing, Game_Constants.grid_spacing * 2), 5),
                           (pygame.rect.Rect(Game_Constants.grid_spacing * 19, 0,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing), 6),
                           None),

                       4: ((pygame.rect.Rect(Game_Constants.grid_spacing * 40, Game_Constants.grid_spacing * 10,
                                             Game_Constants.grid_spacing, Game_Constants.grid_spacing * 2), 3),
                           None),

                       5: ((pygame.rect.Rect((-1) * Game_Constants.grid_spacing, Game_Constants.grid_spacing * 10,
                                             Game_Constants.grid_spacing, Game_Constants.grid_spacing * 2), 3),
                           None),

                       6: ((pygame.rect.Rect(Game_Constants.grid_spacing * 19, 0,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing), 7),
                           None),

                       7: ((pygame.rect.Rect(0, 0, 0, 0), 0), None)}

Level_Spawn_Location = {1: (Game_Constants.Window_width / 2 - 16 * Game_Constants.grid_spacing - 16,
                            Game_Constants.Window_height / 2 + 18),
                        2: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64),
                        3: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64),
                        4: (Game_Constants.Window_width - 64, Game_Constants.Window_height / 2),
                        5: (64, Game_Constants.Window_height / 2),
                        6: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64),
                        7: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64)}

Level_Enemies = {1: [], 2: Second_World_Enemies, 3: [], 4: [], 5: [], 6: [], 7: Seventh_World_Enemies}

Level_Items = {1: [Item.Item(Game_Constants.grid_spacing * 37 + 16, Game_Constants.grid_spacing * 17, "emerald")],
               2: [],
               3: [Item.Item(Game_Constants.grid_spacing * 19 + 16, Game_Constants.grid_spacing * 11,
                             "steel_bow")],
               4: [], 5: [],
               6: [Item.Item(Game_Constants.grid_spacing * 19 + 16, Game_Constants.grid_spacing * 11,
                             "gold_bow")],
               7: []}

World_Raids = {1: [], 2: [], 3: [],

               4: ([lambda: MyFunctions_2.raid(current_player, 5, 0, Level_Enemies.__getitem__(4), wanted_monsters_list=["imp"]),
                    lambda: MyFunctions_2.raid(current_player, 6, 0, Level_Enemies.__getitem__(4), wanted_monsters_list=["zombie", "skeleton"]),
                    lambda: MyFunctions_2.raid(current_player, 5, 0, Level_Enemies.__getitem__(4), wanted_monsters_list=["zombie", "goblin"])], [True, True, True]),

               5: ([lambda: MyFunctions_2.raid(current_player, 5, 0, Level_Enemies.__getitem__(5), wanted_monsters_list=["imp"]),
                    lambda: MyFunctions_2.raid(current_player, 6, 0, Level_Enemies.__getitem__(5), wanted_monsters_list=["zombie", "skeleton"]),
                    lambda: MyFunctions_2.raid(current_player, 5, 0, Level_Enemies.__getitem__(5), wanted_monsters_list=["skeleton", "goblin"])], [True, True, True]),

               6: ([lambda: MyFunctions_2.raid(current_player, 6, 0, Level_Enemies.__getitem__(6), wanted_monsters_list=["zombie", "skeleton"]),
                    lambda: MyFunctions_2.raid(current_player, 4, 0, Level_Enemies.__getitem__(6), wanted_monsters_list=["goblin"]),
                    lambda: MyFunctions_2.raid(current_player, 4, 0, Level_Enemies.__getitem__(6), wanted_monsters_list=["muddy", "goblin"]),
                    lambda: MyFunctions_2.raid(current_player, 5, 0, Level_Enemies.__getitem__(6), wanted_monsters_list=["muddy"])], [True, True, True, True]),

               7: []}

Level_Title = {1: ShowFloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Level_1_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 23,
                                           Titles_Images.Level_1_Title, speed=0.1, amplitude=4),

               2: ShowFloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Level_2_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 23,
                                           Titles_Images.Level_2_Title, speed=0.2, amplitude=5),

               3: ShowFloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Level_3_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 23,
                                           Titles_Images.Level_3_Title, speed=0.2, amplitude=5),

               4: ShowFloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Level_4_and_5_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 23,
                                           Titles_Images.Level_4_and_5_Title, speed=0.2, amplitude=5),

               5: ShowFloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Level_4_and_5_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 23,
                                           Titles_Images.Level_4_and_5_Title, speed=0.2, amplitude=5),

               6: ShowFloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Level_6_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 23,
                                           Titles_Images.Level_6_Title, speed=0.2, amplitude=5),

               7: ShowFloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Level_7_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 23,
                                           Titles_Images.Level_7_Title, speed=0.2, amplitude=5)}

World_Masks = {1: [Masks.First_World_Mask_1, Masks.First_World_Mask_2],
               2: [Masks.Second_World_Mask_1, Masks.Second_World_Mask_2]}
