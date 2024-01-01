#
# It was necessary to create a new functions file to avoid circular import when using classes, as the "MyFunctions"
#                                      module is already present in the image files.
#

import pygame
import csv
import random
import threading
import time
import math
import functools
import itertools

from typing import List, Tuple, Union

import Assets
import Assets.Player_Images

from Assets import Animations
from Assets import Background_Images
from Assets import Buttons
from Assets import UI_Icons
from Assets import Sound_Effects
from Assets import Titles_Images
from Assets import Worlds
from Constants import Game_Constants
from Classes import Animation
from Classes import Character
from Classes import Item
from Classes import DamageText
from Classes import Familiar
from Classes import Fade
from Classes import FloatingText
from Classes import Heart
from Classes import Item
from Classes import Leaf
from Classes import Monster
from Classes import ShowText
from Classes import Weapon
from Classes import World
from Assets import Player_Images

pygame.init()

interrupt_flag = False  # Flag to stop the recursion from raid function

full_heart = Heart.Heart("full_heart", 0, 0)
half_heart = Heart.Heart("half_heart", 0, 0)
empty_heart = Heart.Heart("empty_heart", 0, 0)

coin_static_image = Item.Item(85, 45, "static_coin", can_collect=False)


def draw_info(current_palyer: object, screen: object, damage_text_group) -> None:
    # pygame.draw.rect(screen, Game_Constants.BLACK_COLOR, (0, 0, Game_Constants.Window_width,
    #                                                     Game_Constants.info_bar_height))
    # pygame.draw.line(screen, Game_Constants.WHITE_COLOR, (0, Game_Constants.info_bar_height),
    #                (Game_Constants.Window_width, Game_Constants.info_bar_height))"""

    # Draw lives:
    hearts_number = Game_Constants.hearts_quantity
    total_life = Game_Constants.player_standard_health

    heart_counter = total_life / hearts_number

    half_heart_draw = False

    character_icon = Assets.Player_Images.Health_bar
    character_icon_rect = character_icon.get_rect()
    character_icon_rect.center = (10, 10)

    screen.blit(character_icon, character_icon_rect.center)

    for i in range(hearts_number):
        if current_palyer.health >= ((i + 1) * heart_counter):
            screen.blit(full_heart.image, (83 + i * 37, 12))
        elif current_palyer.health % heart_counter and not half_heart_draw:
            screen.blit(half_heart.image, (83 + i * 37, 12))
            half_heart_draw = True
        else:
            screen.blit(empty_heart.image, (83 + i * 37, 12))

    full_heart.update()
    half_heart.update()
    empty_heart.update()

    ShowText.draw_text(f"X {current_palyer.money}", "AtariClassic", Game_Constants.WHITE_COLOR, 113, 50, screen)

    screen.blit(coin_static_image.image, coin_static_image.rect.center)
    coin_static_image.update(screen, damage_text_group)

    Keys_Pressed = pygame.key.get_pressed()

    w_button = (UI_Icons.W_Button, UI_Icons.W_Button_Rect) if not Keys_Pressed[pygame.K_w] else \
        (UI_Icons.W_Button_Pressed, UI_Icons.W_Button_Pressed_Rect)

    a_button = (UI_Icons.A_Button, UI_Icons.A_Button_Rect) if not Keys_Pressed[pygame.K_a] else \
        (UI_Icons.A_Button_Pressed, UI_Icons.A_Button_Pressed_Rect)

    s_button = (UI_Icons.S_Button, UI_Icons.S_Button_Rect) if not Keys_Pressed[pygame.K_s] else \
        (UI_Icons.S_Button_Pressed, UI_Icons.S_Button_Pressed_Rect)

    d_button = (UI_Icons.D_Button, UI_Icons.D_Button_Rect) if not Keys_Pressed[pygame.K_d] else \
        (UI_Icons.D_Button_Pressed, UI_Icons.D_Button_Pressed_Rect)

    # Drawing Buttons on Screen :
    screen.blit(*w_button)
    screen.blit(*a_button)
    screen.blit(*s_button)
    screen.blit(*d_button)

    Teleport_Orb = (UI_Icons.Teleport_Orb_Active, UI_Icons.Teleport_Orb_Active_Rect) if current_palyer.can_teleport \
        else (UI_Icons.Teleport_Orb_Deactive, UI_Icons.Teleport_Orb_Deactive_Rect)
    Ultimate_Orb = (UI_Icons.Ultimate_Orb_Active, UI_Icons.Ultimate_Orb_Active_Rect) if current_palyer.can_ultimate \
        else (UI_Icons.Ultimate_Orb_Deactive, UI_Icons.Ultimate_Orb_Deactive_Rect)
    Regeneration_Orb = (UI_Icons.Regeneration_Orb_Active, UI_Icons.Regeneration_Orb_Active_Rect) if current_palyer.can_regenerate \
        else (UI_Icons.Regeneration_Orb_Deactive, UI_Icons.Regeneration_Orb_Deactive_Rect)

    screen.blit(*Teleport_Orb)
    screen.blit(*Ultimate_Orb)
    screen.blit(*Regeneration_Orb)


def distance(coordinates_1: Tuple[Union[int, float]], coordinates_2: Tuple[Union[int, float]]) -> float:
    return math.sqrt((coordinates_2[0] - coordinates_1[0]) ** 2 + (coordinates_2[1] - coordinates_1[1]) ** 2)


def draw_grid(screen: object) -> None:
    for x in range(Game_Constants.grides_number):
        # Vertical Lines :
        pygame.draw.line(screen, Game_Constants.WHITE_COLOR, (x * Game_Constants.grid_spacing, 0),
                         (x * Game_Constants.grid_spacing, Game_Constants.Window_height))

        # Horizontal Lines :
        pygame.draw.line(screen, Game_Constants.WHITE_COLOR, (0, x * Game_Constants.grid_spacing),
                         (Game_Constants.Window_width, x * Game_Constants.grid_spacing))


def change_level(screen: object, current_world: World, current_player: Character,
                 level: int, item_group: object, enemy_projectiles_group: object, leafs_group: object) -> list:

    screen.fill(Game_Constants.BLACK_COLOR)  # Reset the background

    Sound_Effects.Grass_Walking_Sound.stop()
    Sound_Effects.Walking_Sound.stop()
    Sound_Effects.Echo_Walking_Sound.stop()

    # Saving the items from current level :
    Worlds.Level_Items.__getitem__(Worlds.current_level).clear()  # To not duplicate the items

    if Worlds.current_level not in {4, 5}:
        for item in item_group:
            Worlds.Level_Items.__getitem__(Worlds.current_level).append(item)

    item_group.empty()

    Worlds.Level_Title.__getitem__(Worlds.current_level).restart()

    enemy_projectiles_group.empty()
    leafs_group.empty()

    if level in {1, 2}:
        for i in range(Game_Constants.leafs_quantity):
            leaf_image = Background_Images.Tiny_Board_Leaf
            new_leaf = Leaf.Leaf((-30) * i * leaf_image.get_width(), random.randint(0, Game_Constants.Window_height), leaf_image)
            new_leaf.oscilation_position = random.randint(0, 100)
            leafs_group.add(new_leaf)

    if level == 2:
        Worlds.Level_Spawn_Location[1] = (Game_Constants.grid_spacing * 20, Game_Constants.grid_spacing * 3)

    if (level == 3 and Worlds.current_level == 2) or (level == 6 and Worlds.current_level == 3) or \
            (level == 7 and Worlds.current_level == 6):
        Sound_Effects.Close_Door.play()

    if level == 3 and Worlds.current_level in {4, 5}:
        Worlds.Level_Enemies.__getitem__(Worlds.current_level).clear()

    if level == 4 and Worlds.current_level == 3:
        Worlds.Level_Spawn_Location[3] = (Game_Constants.grid_spacing, Game_Constants.grid_spacing * 11)
        checker = [element for element in Worlds.World_Raids.__getitem__(level)[1] if element]

        if bool(checker):  # If player has not defeated all raids :
            Worlds.World_Raids.__getitem__(level)[0][0]()

    if level == 5 and Worlds.current_level == 3:
        Worlds.Level_Spawn_Location[3] = (Game_Constants.grid_spacing * 39, Game_Constants.grid_spacing * 11)
        checker = [element for element in Worlds.World_Raids.__getitem__(level)[1] if element]

        if bool(checker):  # If player has not defeated all raids :
            Worlds.World_Raids.__getitem__(level)[0][0]()

    if level == 1 and Worlds.current_level == 7:
        restart(screen)
        Game_Constants.fade_animation_cooldown = 12

    # Changing the World's Mask :
    try:
        if Worlds.Level_Interactions.__getitem__(level)[0][0][-1]:
            Worlds.current_mask = Worlds.World_Masks.__getitem__(level)[0]
        else:
            Worlds.current_mask = Worlds.World_Masks.__getitem__(level)[1]
    except (KeyError, IndexError):
        Worlds.current_mask = None

    with open(f"Levels/Level_{level}.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")

        for x, row in enumerate(reader):
            for y, tile in enumerate(row):
                Worlds.World_Data[x][y] = int(tile)

    current_world.map_tiles = []
    current_world.process_data(Worlds.World_Data)

    current_player.rect.center = Worlds.Level_Spawn_Location.__getitem__(level)

    Worlds.familiar.rect.centerx, Worlds.familiar.rect.centery = (current_player.rect.centerx - 40,
                                                                  current_player.rect.centery) if \
        ((Worlds.current_level == level == 1) or (Worlds.current_level == 7 and level == 1)) else \
        (current_player.rect.centerx, current_player.rect.centery)

    for item in Worlds.Level_Items.__getitem__(level):
        item_group.add(item)

    Assets.Worlds.current_level = level

    return Worlds.Level_Enemies.__getitem__(level)


def open_door(interaction_info: list) -> None:

    if Worlds.current_level == 1:
        if interaction_info[0][2]:  # If Door still Closed
            # No Restrictions
            interaction_info[0][0] = interaction_info[1]  # Change the sprite to opened door
            interaction_info[0][2] = False  # Disable the door collision
            if Worlds.draw_mask:  # Changing the Mask :
                Worlds.current_mask = Worlds.World_Masks[Worlds.current_level][1]
            Sound_Effects.Open_Door.play_loop()

    if Worlds.current_level == 2:
        if not bool(Worlds.Level_Enemies.__getitem__(2)) and interaction_info[0][2]:
            # If it has no enemies in level 2 and Door still CLosed:
            interaction_info[0][0] = interaction_info[1]  # Change the sprite to opened door
            interaction_info[0][2] = False  # Disable the door collision
            if Worlds.draw_mask:  # Changing the Mask :
                Worlds.current_mask = Worlds.World_Masks[Worlds.current_level][1]
            Sound_Effects.Open_Door.play_loop()
        else:
            if interaction_info[0][2]:
                Sound_Effects.Closed_Door.play_loop()

    elif Worlds.current_level == 3:
        if not ((functools.reduce(lambda aux_1, aux_2: aux_1 or aux_2, Worlds.World_Raids.__getitem__(4)[1])) or
                (functools.reduce(lambda aux_1, aux_2: aux_1 or aux_2, Worlds.World_Raids.__getitem__(5)[1]))) and \
                ("Steel_bow" in Worlds.current_player.weapons_inventory) and interaction_info[0][2]:

            # If it has no enemies in level 4 and 5 :
            interaction_info[0][0] = interaction_info[1]  # Change the sprite to opened door
            interaction_info[0][2] = False  # Disable the door collision
            Sound_Effects.Open_Door.play_loop()
        else:
            if interaction_info[0][2]:
                Sound_Effects.Closed_Door.play_loop()

    elif Worlds.current_level == 6:
        if not (functools.reduce(lambda aux_1, aux_2: aux_1 or aux_2, Worlds.World_Raids.__getitem__(6)[1])) and\
                ("Gold_bow" in Worlds.current_player.weapons_inventory) and interaction_info[0][2]:
            # If it has no enemies in level 6 :
            interaction_info[0][0] = interaction_info[1]  # Change the sprite to opened door
            interaction_info[0][2] = False  # Disable the door collision
            Sound_Effects.Open_Door.play_loop()
        else:
            if interaction_info[0][2]:
                Sound_Effects.Closed_Door.play_loop()


def menu(screen: object, is_fullscreen: bool = False) -> None:
    global interrupt_flag

    Screen = screen
    FullScreen = is_fullscreen

    Worlds.Start_Fade = True
    Worlds.Current_Fade_Animation = Worlds.Fade_Animation[1]
    Worlds.Do_Fade = 1

    for fade in Worlds.Fade_Animation:
        fade.change_rate = Game_Constants.second_fade_transition_rate

    pygame.mouse.get_pressed()

    game_clock = pygame.time.Clock()

    # Getting the custom pointer :
    custom_pointer = Background_Images.Pointer
    pointer_rect = custom_pointer.get_rect()
    pointer_rect.center = pygame.mouse.get_pos()

    Button_Sound = Sound_Effects.Button
    Press_Button_Sound = Sound_Effects.Button_Pressed

    Menu_Background = Animation.Animation(Animations.Menu_Animation,
                                          Game_Constants.fade_death_cooldown, coordinate_x=70)

    Game_Title = FloatingText.FloatingText((Game_Constants.Window_width - Titles_Images.Game_Title.get_width()) / 2,
                                           Game_Constants.Window_height / 20,
                                           Titles_Images.Game_Title)

    Play_Button = (Buttons.Play_Button, Buttons.Play_Button_Rect)
    Play_Button[1].x, Play_Button[1].y = (Game_Constants.Window_width - Play_Button[0].get_width()) / 2, \
                                         9 * Game_Constants.Window_height / 20
    Play_Button = FloatingText.FloatingText(Play_Button[1].x, Play_Button[1].y, Play_Button[0], speed=0.08, amplitude=2)

    Play_Button_Pressed = (Buttons.Play_Button_Pressed, Buttons.Menu_Button_Pressed_Rect)
    Play_Button_Pressed[1].x, Play_Button_Pressed[1].y = (Game_Constants.Window_width - Play_Button_Pressed[
        0].get_width()) / 2, \
                                                         9 * Game_Constants.Window_height / 20
    Play_Button_Pressed = FloatingText.FloatingText(Play_Button_Pressed[1].x, Play_Button_Pressed[1].y,
                                                    Play_Button_Pressed[0], speed=0.08, amplitude=2)

    Quit_Button = (Buttons.Quit_Button, Buttons.Quit_Button_Rect)
    Quit_Button[1].x, Quit_Button[1].y = (Game_Constants.Window_width - Quit_Button[0].get_width()) / 2, \
                                         13 * Game_Constants.Window_height / 20
    Quit_Button = FloatingText.FloatingText(Quit_Button[1].x, Quit_Button[1].y, Quit_Button[0], speed=0.08, amplitude=2)

    Quit_Button_Pressed = (Buttons.Quit_Button_Pressed, Buttons.Quit_Button_Pressed_Rect)
    Quit_Button_Pressed[1].center = Quit_Button.rect.center
    Quit_Button_Pressed = FloatingText.FloatingText(Quit_Button_Pressed[1].x, Quit_Button_Pressed[1].y,
                                                    Quit_Button_Pressed[0], speed=0.08, amplitude=2)

    go_play = False
    go_quit = False

    Game_Loop = True
    while Game_Loop:

        Screen.fill(Game_Constants.BLACK_COLOR)

        game_clock.tick(Game_Constants.FPS)

        Menu_Background.draw(Screen)

        Menu_Background.update_loop()

        Game_Title.draw(Screen)

        Game_Title.update()

        Sound_Effects.Menu_Music.play_loop()

        left_mouse_click = pygame.mouse.get_pressed()[0]

        if not pointer_rect.colliderect(Play_Button.rect):
            Play_Button.draw(Screen)
            Play_Button.update()
            Play_Button_Pressed.rect.center = Play_Button.rect.center

        else:

            Play_Button_Pressed.draw(Screen)

            if left_mouse_click and not Worlds.Do_Fade:
                Press_Button_Sound.play()
                Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]
                Worlds.Current_Fade_Animation.restart()
                Worlds.Do_Fade = 1
                go_play = True

        if not pointer_rect.colliderect(Quit_Button.rect):
            Quit_Button.draw(Screen)
            Quit_Button.update()
            Quit_Button_Pressed.rect.center = Quit_Button.rect.center
        else:
            Quit_Button_Pressed.draw(Screen)

            if left_mouse_click and not Worlds.Do_Fade:
                Press_Button_Sound.play()
                Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]
                Worlds.Current_Fade_Animation.restart()
                Worlds.Do_Fade = 1
                go_quit = True

        if pointer_rect.colliderect(Quit_Button.rect) or pointer_rect.colliderect(Play_Button.rect):
            Button_Sound.play_once()
        else:
            Button_Sound.just_one_time = False

        if Worlds.Do_Fade:

            Worlds.Current_Fade_Animation.draw(Screen)

            if not Worlds.Current_Fade_Animation.end_fade:
                Worlds.Current_Fade_Animation.update()

            else:

                Worlds.Current_Fade_Animation.restart()

                Worlds.Do_Fade -= 1

                if go_play:
                    go_quit = False
                if go_quit:
                    go_play = False

                if go_play:
                    Sound_Effects.Menu_Music.stop()
                    restart(Screen)
                    play(Screen, is_fullscreen)

                if go_quit:
                    Sound_Effects.Menu_Music.stop()
                    Game_Loop = False  # Close the Game.

        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:  # Event for closing the game window.
                Game_Loop = False
                interrupt_flag = True

            if Event.type == pygame.KEYDOWN:
                if Event.key == pygame.K_F11:
                    if FullScreen:
                        Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                          Game_Constants.Window_height))
                        FullScreen = not FullScreen
                    else:
                        Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                          Game_Constants.Window_height), pygame.FULLSCREEN)
                        FullScreen = not FullScreen

        # Updating the Pointer :
        pygame.mouse.set_visible(False)  # Hiding the original pointer
        Pointer_rect = pointer_rect
        Pointer_rect.center = pygame.mouse.get_pos()
        if (0 < pygame.mouse.get_pos()[0] < Game_Constants.Window_width - 1) and \
                (Game_Constants.Window_height - 1 > pygame.mouse.get_pos()[1] > 0):
            Screen.blit(custom_pointer, Pointer_rect.center)

        pygame.display.update()

    pygame.quit()


def play(screen: object, is_fullscreen: bool = False) -> None:

    global interrupt_flag

    Screen = screen

    Worlds.Start_Fade = True
    Worlds.Current_Fade_Animation = Worlds.Fade_Animation[1]
    Worlds.Do_Fade = 1

    Game_Clock = pygame.time.Clock()  # Gettinng a Game Clock.
    FullScreen = is_fullscreen  # Variable to set FullScreen

    # Loading Custom Pointer :
    Custom_Pointer = Background_Images.Pointer
    Pointer_rect = Custom_Pointer.get_rect()
    Pointer_rect.center = pygame.mouse.get_pos()

    next_level = None

    # Creating the player :
    current_player = Worlds.current_player
    # Creating an weapon :
    weapon = Weapon.Weapon()  # Starts with no weapon.
    second_sword = Weapon.Weapon("Sword", True)

    # Creating Enemy List :
    enemy_list = Worlds.Level_Enemies.__getitem__(Worlds.current_level)

    # Creating the First World Test:
    current_world = World.World()
    current_world.process_data(Worlds.World_Data)

    # Objects from the Map Current :
    current_objects = Worlds.Level_Objects.get(Worlds.current_level, [])

    # ----------------------------------------- GROUPS --------------------------------- #

    # Creating Arrows Sprite Group :
    arrow_group = pygame.sprite.Group()

    # Creating Damage Text Group :
    damage_text_group = pygame.sprite.Group()

    # Creating Text Group :
    text_group = pygame.sprite.Group()

    # Creating Items Group :
    item_group = pygame.sprite.Group()

    # Creating Enemies Projectiles Group :
    enemy_projectiles_group = pygame.sprite.Group()

    # Creating Leafs Group :
    leafs_group = pygame.sprite.Group()

    for i in range(Game_Constants.leafs_quantity):
        leaf_image = Background_Images.Tiny_Board_Leaf
        new_leaf = Leaf.Leaf((-30) * i * leaf_image.get_width(), random.randint(0, Game_Constants.Window_height), leaf_image)
        new_leaf.oscilation_position = random.randint(0, 100)
        leafs_group.add(new_leaf)

    for item in Worlds.Level_Items.__getitem__(Worlds.current_level):
        item_group.add(item)

    # Items Test :
    """potion = Item.Item(480, 200, "red_potion")
    item_group.add(potion)
    coin = Item.Item(780, 640, "coin")
    item_group.add(coin)
    silver_coin = Item.Item(810, 640, "silver_coin")
    item_group.add(silver_coin)
    red_coin = Item.Item(840, 640, "red_coin")
    item_group.add(red_coin)
    emerald = Item.Item(870, 640, "emerald")
    item_group.add(emerald)"""

    Game_LOOP = True  # Setting Game Loop.
    while Game_LOOP:

        Game_Clock.tick(Game_Constants.FPS)  # Setting FPS to 60.
        Screen.fill(Game_Constants.BLACK_COLOR)

        if not enemy_list and Worlds.current_level == 7 and not Worlds.end_game:
            next_level = (None, 1)
            Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]
            Worlds.end_game = True
            Worlds.Current_Fade_Animation.change_rate = Game_Constants.second_fade_transition_rate
            Worlds.Do_Fade = 2

        if current_player.alive:  # if Player still alive :

            if Worlds.current_level in {1, 2}:
                Sound_Effects.Wind_Sound.play_loop()

                if len(leafs_group) < Game_Constants.leafs_quantity:
                    leaf_image = Background_Images.Tiny_Board_Leaf
                    new_leaf = Leaf.Leaf((-1) * leaf_image.get_width(), random.randint(0, Game_Constants.Window_height),
                                         leaf_image)
                    new_leaf.angle = random.randint(0, 360)
                    leafs_group.add(new_leaf)
            else:
                Sound_Effects.Wind_Sound.stop()
                Sound_Effects.Dungeon_Air.play_loop()

            if Worlds.current_level == 1:

                for music in Sound_Effects.Second_Level_Music:
                    music.stop()
                for music in Sound_Effects.Dungeon_Music:
                    music.stop()
                for music in Sound_Effects.Boss_Fight_Music:
                    music.stop()

                if not enemy_list:
                    Sound_Effects.First_Level_Music[1].stop()
                    Sound_Effects.First_Level_Music[0].play_loop()
                else:
                    Sound_Effects.First_Level_Music[0].stop()
                    Sound_Effects.First_Level_Music[1].play_loop()

            elif Worlds.current_level == 2:

                for music in Sound_Effects.First_Level_Music:
                    music.stop()
                for music in Sound_Effects.Dungeon_Music:
                    music.stop()
                for music in Sound_Effects.Boss_Fight_Music:
                    music.stop()

                if not enemy_list:
                    Sound_Effects.Second_Level_Music[1].stop()
                    Sound_Effects.Second_Level_Music[0].play_loop()
                else:
                    Sound_Effects.Second_Level_Music[0].stop()
                    Sound_Effects.Second_Level_Music[1].play_loop()

            elif Worlds.current_level == 3:

                for music in Sound_Effects.Second_Level_Music:
                    music.stop()
                for music in Sound_Effects.First_Level_Music:
                    music.stop()
                for music in Sound_Effects.Boss_Fight_Music:
                    music.stop()

                Sound_Effects.Dungeon_Music[1].stop()
                Sound_Effects.Dungeon_Music[0].play_loop()

            elif Worlds.current_level in {4, 5}:

                for music in Sound_Effects.Second_Level_Music:
                    music.stop()
                for music in Sound_Effects.First_Level_Music:
                    music.stop()
                for music in Sound_Effects.Boss_Fight_Music:
                    music.stop()

                if not (functools.reduce(lambda aux_1, aux_2: aux_1 or aux_2,
                                         Worlds.World_Raids.__getitem__(Worlds.current_level)[1])):

                    Sound_Effects.Dungeon_Music[1].stop()
                    Sound_Effects.Dungeon_Music[0].play_loop()
                else:
                    Sound_Effects.Dungeon_Music[0].stop()
                    Sound_Effects.Dungeon_Music[1].play_loop()

            elif Worlds.current_level == 6:

                for music in Sound_Effects.Second_Level_Music:
                    music.stop()
                for music in Sound_Effects.First_Level_Music:
                    music.stop()
                for music in Sound_Effects.Boss_Fight_Music:
                    music.stop()

                if (functools.reduce(lambda aux_1, aux_2: aux_1 or aux_2,
                                     Worlds.World_Raids.__getitem__(Worlds.current_level)[1])) and \
                        "Gold_bow" in current_player.weapons_inventory:

                    Sound_Effects.Dungeon_Music[0].stop()
                    Sound_Effects.Dungeon_Music[1].play_loop()
                else:
                    Sound_Effects.Dungeon_Music[1].stop()
                    Sound_Effects.Dungeon_Music[0].play_loop()

            elif Worlds.current_level == 7:

                for music in Sound_Effects.Second_Level_Music:
                    music.stop()
                for music in Sound_Effects.First_Level_Music:
                    music.stop()
                for music in Sound_Effects.Dungeon_Music:
                    music.stop()

                if not enemy_list:
                    Sound_Effects.Boss_Fight_Music[1].stop()
                    Sound_Effects.Boss_Fight_Music[0].play_loop()
                else:
                    Sound_Effects.Boss_Fight_Music[0].stop()
                    Sound_Effects.Boss_Fight_Music[1].play_loop()

            # Defining initial speed :
            dx = 0
            dy = 0

            Keys_pressed = pygame.key.get_pressed()  # Getting a dict with all pressed buttons in keyboard

            # Checking for Player's interactions :
            for Event in pygame.event.get():

                if Event.type == pygame.QUIT:  # Event for closing the game window.
                    Game_LOOP = False
                    interrupt_flag = True

                right_mouse_pressed = pygame.mouse.get_pressed()[2]

                if right_mouse_pressed:  # Interaction between objects in map :
                    for interaction in Worlds.Level_Interactions.__getitem__(Worlds.current_level):

                        # if interaction has not occured yet :
                        if not interaction[3]:

                            if current_player.hitbox.colliderect(interaction[2]) and current_player.can_interact:
                                interaction[4](interaction)

                if Event.type == pygame.KEYDOWN:

                    if Event.key == pygame.K_F11:
                        if FullScreen:
                            Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                              Game_Constants.Window_height))
                            FullScreen = not FullScreen

                        else:

                            Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                              Game_Constants.Window_height), pygame.FULLSCREEN)
                            FullScreen = not FullScreen

                    if Event.key == pygame.K_0 and current_player.can_change_weapon:

                        current_player.can_change_weapon = False

                        weapon.current_weapon = "none_wp"

                    if Event.key == pygame.K_1 and current_player.can_change_weapon:

                        if "Sword" in current_player.weapons_inventory:

                            if not weapon.current_weapon == "Sword":
                                current_player.can_change_weapon = False
                                Sound_Effects.Sword_Pull.play_loop()
                                weapon.current_weapon = "Sword"
                                weapon.weapon_change_time = pygame.time.get_ticks()

                    if Event.key == pygame.K_2 and current_player.can_change_weapon:

                        if "Bow" in current_player.weapons_inventory:
                            if not weapon.current_weapon == "Bow":
                                current_player.can_change_weapon = False
                                Sound_Effects.Bow_Pull.play_loop()
                                weapon.current_weapon = "Bow"
                                weapon.weapon_change_time = pygame.time.get_ticks()

                    if Event.key == pygame.K_3 and current_player.can_change_weapon:

                        if "Steel_bow" in current_player.weapons_inventory:
                            if not weapon.current_weapon == "Steel_bow":
                                current_player.can_change_weapon = False
                                Sound_Effects.Steel_Bow_Pull.play_loop()
                                weapon.current_weapon = "Steel_bow"
                                weapon.weapon_change_time = pygame.time.get_ticks()

                    if Event.key == pygame.K_4 and current_player.can_change_weapon:

                        if "Gold_bow" in current_player.weapons_inventory:
                            if not weapon.current_weapon == "Gold_bow":
                                current_player.can_change_weapon = False
                                Sound_Effects.Gold_Bow_Pull.play_loop()
                                weapon.current_weapon = "Gold_bow"
                                weapon.weapon_change_time = pygame.time.get_ticks()

                    if Event.key in {pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_SPACE}:  # Dash Button :
                        if current_player.can_dash:
                            if not current_player.teleportation and not current_player.end_teleportation:
                                current_player.dash()

                    if Event.key == pygame.K_e:  # Teleport button :
                        no_collision = True  # Boolean variable to check if player is not teleporting inside objects

                        new_position = pygame.mouse.get_pos()

                        temporary_rectangle = current_player.rect.copy()
                        mouse_position = pygame.mouse.get_pos()

                        for obstacle in current_objects:
                            temporary_rectangle.center = mouse_position
                            if obstacle[1].colliderect(temporary_rectangle) and obstacle[
                                2]:  # if object has collision enabled
                                no_collision = False

                        if current_player.can_teleport and no_collision:
                            if not current_player.dashing and not current_player.end_dashing:
                                if (0 < new_position[0] < Game_Constants.Window_width - 1) and \
                                        (Game_Constants.Window_height - 1 > new_position[1] > 0):
                                    current_player.teleport(new_position)

                    if Event.key == pygame.K_r:
                        if not current_player.dashing and not current_player.end_dashing and \
                                not current_player.teleportation and not current_player.end_teleportation:
                            current_player.ultimate_cast()

                    if Event.key == pygame.K_g:
                        current_player.regenerate()

            if Keys_pressed[pygame.K_d] or Keys_pressed[pygame.K_RIGHT]:
                Moving_right = True
            else:
                Moving_right = False

            if Keys_pressed[pygame.K_a] or Keys_pressed[pygame.K_LEFT]:
                Moving_left = True
            else:
                Moving_left = False

            if Keys_pressed[pygame.K_s] or Keys_pressed[pygame.K_DOWN]:
                Moving_down = True
            else:
                Moving_down = False

            if Keys_pressed[pygame.K_w] or Keys_pressed[pygame.K_UP]:
                Moving_up = True
            else:
                Moving_up = False

            if Moving_right and Moving_left:
                Moving_right = False
                Moving_left = False

            if Moving_up and Moving_down:
                Moving_down = False
                Moving_up = False

            if Moving_up:
                dy = (-1) * (Game_Constants.Player_Speed if not current_player.ultimate else
                             Game_Constants.Player_Ultimate_Speed)

            if Moving_down:
                dy = Game_Constants.Player_Speed if not current_player.ultimate else Game_Constants.Player_Ultimate_Speed

            if Moving_left:
                dx = (-1) * (Game_Constants.Player_Speed if not current_player.ultimate else
                             Game_Constants.Player_Ultimate_Speed)

            if Moving_right:
                dx = Game_Constants.Player_Speed if not current_player.ultimate else Game_Constants.Player_Ultimate_Speed

            # Moving Player :
            current_player.movement(dx, dy, current_objects, Worlds.World_Data)
            # if current level > 2 ===> 0 == False

            # Moving Enemies :
            for enemy in enemy_list:
                enemy.ai(current_player, current_objects, enemy_projectiles_group)

        else:  # if player is Dead :

            for music in itertools.chain(Sound_Effects.First_Level_Music, Sound_Effects.Second_Level_Music,
                                         Sound_Effects.Dungeon_Music, Sound_Effects.Boss_Fight_Music):
                music.stop()

            Sound_Effects.Grass_Walking_Sound.stop()
            Sound_Effects.Walking_Sound.stop()
            Sound_Effects.Echo_Walking_Sound.stop()

            for Event in pygame.event.get():
                if Event.type == pygame.WINDOWCLOSE or Event.type == pygame.QUIT:  # Event for closing the game window.
                    Game_LOOP = False

                if Event.type == pygame.KEYDOWN:
                    if Event.key == pygame.K_ESCAPE:
                        if not FullScreen:
                            Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                              Game_Constants.Window_height))
                            FullScreen = not FullScreen
                        else:
                            Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                              Game_Constants.Window_height), pygame.FULLSCREEN)
                            FullScreen = not FullScreen

            current_player.update(weapon)

            if current_player.frame_index == 9:  # End of the death animation :
                for fade in Worlds.Fade_Animation:
                    fade.change_rate = Game_Constants.second_fade_transition_rate

                Worlds.Do_Fade = 1
                Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]

        # ------------------------------------- UPDATING SECTION ------------------------------------- #

        Worlds.Level_Title.__getitem__(Worlds.current_level).update()

        if current_player.alive:
            current_player.update(weapon)
            Worlds.familiar.update()
            Worlds.familiar.ai(current_player)
            current_arrow = weapon.update(current_player)

            second_sword.update(current_player)

            if current_player.ultimate and weapon.current_weapon == "Sword":
                Sound_Effects.Double_Sword_Pull.play_once()
            else:
                Sound_Effects.Double_Sword_Pull.just_one_time = False

            if current_arrow and current_player.can_attack:
                if weapon.current_weapon == "Gold_bow":  # Gold Bow shoots 3 arrows.
                    for arw in current_arrow:
                        arrow_group.add(arw)
                else:
                    arrow_group.add(current_arrow)
                    Sound_Effects.Normal_Arrow_Sound.play()

            # Updating Arrows :
            for current_arrow in arrow_group:
                damage, damage_position = current_arrow.update(enemy_list, current_player, weapon, current_objects)
                if damage:  # if "damage" != 0
                    damage_text = DamageText.DamageText(damage_position.centerx, damage_position.y,
                                                        str(damage), Game_Constants.RED_COLOR, "AtariClassic")
                    damage_text_group.add(damage_text)

            for enemy in enemy_list:
                if not enemy.alive:
                    enemy_list.remove(enemy)

            # Updating Enemies :
            for enemies in enemy_list:
                if current_player.ultimate and weapon.current_weapon == "Sword":
                    damage, damage_position = enemies.update(weapon, current_player, item_group, second_sword)
                else:
                    damage, damage_position = enemies.update(weapon, current_player, item_group)

                if damage:  # if "damage" != 0
                    damage_text = DamageText.DamageText(damage_position.centerx, damage_position.y,
                                                        str(damage), Game_Constants.RED_COLOR, "AtariClassic")
                    damage_text_group.add(damage_text)

            # Updating All Leafs :
            for leaf in leafs_group:
                leaf.update()

            # Updating All Damage Texts :
            damage_text_group.update()

            # Updating All Texts :
            text_group.update()

            # Updating All Items :
            item_group.update(current_player, text_group)

            # Updating All Enemy Projectiles :
            for projectile in enemy_projectiles_group:
                projectile.update(current_player, current_objects)

        # ---------------------------------------------------------------------------------------- #

        # ------------------------------------- DRAW SECTION ------------------------------------- #

        # Drawing the Current World :
        current_world.draw(Screen)

        # Drawing the Current World Objects :
        for objects in current_objects:
            if objects[0]:  # check if Object has image
                Screen.blit(objects[0], objects[1])

        # Drawind the Mask of the World :
        if Worlds.current_mask:
            Screen.blit(Worlds.current_mask, (0, 0))

        # Drawing Player :
        current_player.draw(Screen)  # The player needs to be under the enemies and over the weapons

        # Drawing Enemies :
        for enemy in enemy_list:
            enemy.draw(Screen)

        # Drawing Weapons :
        weapon.draw(Screen, current_player)

        if current_player.ultimate and weapon.current_weapon == "Sword":
            second_sword.draw(Screen, current_player)

        # Drawing Arrows Group :
        for arrow in arrow_group:
            arrow.draw(Screen)

        # Drawing Items Group :
        item_group.draw(Screen)

        # Tree's from the current map :
        if Worlds.current_level == 1:
            for tree in Worlds.First_World_Trees:
                Screen.blit(tree[0], tree[1])
        elif Worlds.current_level == 2:
            for tree in Worlds.Second_World_Trees:
                Screen.blit(tree[0], tree[1])

        # Drawing Tutorial Sign :
        if Worlds.current_level == 1:
            Worlds.Tutorial_Sign.draw(Screen, current_player)

        # Drawind the Familiar :
        Worlds.familiar.draw(Screen)

        # Drawing Leafs from the Current Map :
        for leaf in leafs_group:
            leaf.draw(Screen)

        # Drawing All Damage Texts :
        damage_text_group.draw(Screen)

        # Drawing All Texts :
        text_group.draw(Screen)

        # Drawing All Enemy Projectiles :
        for projectile in enemy_projectiles_group:
            projectile.draw(Screen)

        # Drawing the Floating Buttons from Picking Weapons :
        if "Steel_bow" in current_player.weapons_inventory:
            Worlds.button_3.rect.centerx, Worlds.button_3.original_y = current_player.rect.centerx, current_player.rect.centery - 60
            Worlds.button_3.draw(Screen)
            Worlds.button_3.update()
        if "Gold_bow" in current_player.weapons_inventory:
            Worlds.button_4.rect.centerx, Worlds.button_4.original_y = current_player.rect.centerx, current_player.rect.centery - 60
            Worlds.button_4.draw(Screen)
            Worlds.button_4.update()

        # Drawing the Title from Current Level :
        Worlds.Level_Title.__getitem__(Worlds.current_level).draw(Screen)

        # Display Player Info :
        draw_info(current_player, Screen, damage_text_group)

        # Display of the Game Grid :
        # MyFunctions_2.draw_grid(Screen)

        if Worlds.Start_Fade:  # Fade from the start of the game
            if not Worlds.Current_Fade_Animation.end_fade:
                Worlds.Current_Fade_Animation.update()
            else:
                Worlds.Start_Fade = False

        # Locations to change the level :
        for level_locations in Worlds.Next_Level_Location.__getitem__(Worlds.current_level):
            if level_locations:  # if != 'None'
                # Checks if the player has progressed to the next level :
                if current_player.rect.colliderect(level_locations[0]):
                    current_player.can_interact = False
                    next_level = level_locations
                    Worlds.Do_Fade = 2  # Times to do the fade.
                    Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]

                    for fade in Worlds.Fade_Animation:
                        fade.change_rate = Game_Constants.fade_transition_rate

                    current_player.can_move = False
                    for enemy in enemy_list:
                        enemy.can_move = False

        if Worlds.Do_Fade:

            Worlds.Current_Fade_Animation.draw(Screen)

            if not Worlds.Current_Fade_Animation.end_fade:
                Worlds.Current_Fade_Animation.update()

            else:

                Worlds.Current_Fade_Animation.restart()

                Worlds.Do_Fade -= 1

                if Worlds.Do_Fade == 1:

                    if Worlds.end_game:
                        Worlds.end_game = False
                        restart(Screen)
                        play(Screen, is_fullscreen)

                    Worlds.Current_Fade_Animation = Worlds.Fade_Animation[1]

                    enemy_list = change_level(Screen, current_world, current_player,
                                              next_level[1], item_group, enemy_projectiles_group, leafs_group)

                    for enemy in enemy_list:
                        enemy.can_move = False

                    # Objects from the Current Map :
                    current_objects = Worlds.Level_Objects.get(Worlds.current_level, [])
                    arrow_group.empty()
                    damage_text_group.empty()

        else:
            current_player.can_move = True
            current_player.can_interact = True

            for enemy in enemy_list:
                enemy.can_move = True

        if not current_player.alive and Worlds.Current_Fade_Animation.end_fade:
            death_screen(Screen, FullScreen)

        # ---------------------------------------------------------------------------------------- #

        # Updating the Pointer :
        pygame.mouse.set_visible(False)  # Hiding the original pointer
        Pointer_rect.center = pygame.mouse.get_pos()
        if (0 < pygame.mouse.get_pos()[0] < Game_Constants.Window_width - 1) and \
                (Game_Constants.Window_height - 1 > pygame.mouse.get_pos()[1] > 0):
            Screen.blit(Custom_Pointer, Pointer_rect.center)

        # Updating the game window :
        pygame.display.update()

    pygame.quit()  # Closing Pygame.


def restart(screen: object) -> None:

    Worlds.current_level = 1
    Worlds.raid_index = 0

    Worlds.button_3.restart()
    Worlds.button_4.restart()

    for fade in Worlds.Fade_Animation:
        fade.change_rate = Game_Constants.second_fade_transition_rate

    Sound_Effects.Death_Sound_Effect.just_one_time = False

    # --------------------------------------- FIRST WORLD RESTART ------------------------------------ #

    Closed_Door = World.World.tiles_dict.__getitem__(16)
    Closed_Door_Rect = Closed_Door.get_rect()
    Closed_Door_Rect.height -= 20
    Closed_Door_Rect.x, Closed_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
    Interaction_Door_Rect = pygame.rect.Rect(Closed_Door_Rect.x, Closed_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)

    # [ < Sprite >, < Rectangle >, < Collision > ] :
    Closed_Door = [Closed_Door, Closed_Door_Rect, True]  # Need to be mutable

    Worlds.Level_Objects.__getitem__(1).pop()
    Worlds.Level_Objects.__getitem__(1).append(Closed_Door)

    Worlds.Level_Interactions.__getitem__(1).pop()
    Worlds.Level_Interactions.__getitem__(1).append(
        [Closed_Door, World.World.tiles_dict.__getitem__(17), Interaction_Door_Rect, False,
         open_door])

    # --------------------------------------- SECOND WORLD RESTART ------------------------------------ #

    Second_World_Enemies = []

    Imp_1 = Monster.Monster(Game_Constants.grid_spacing * 10, Game_Constants.grid_spacing * 7, "imp")
    Second_World_Enemies.append(Imp_1)

    Imp_2 = Monster.Monster(Game_Constants.grid_spacing * 36 + 16, Game_Constants.grid_spacing * 4, "imp")
    Second_World_Enemies.append(Imp_2)

    Imp_3 = Monster.Monster(Game_Constants.grid_spacing * 8, Game_Constants.grid_spacing * 17, "imp")
    Second_World_Enemies.append(Imp_3)

    Worlds.Level_Enemies[2] = Second_World_Enemies

    Closed_Dungeon_Door = World.World.tiles_dict.__getitem__(40)
    Closed_Dungeon_Door_Rect = Closed_Dungeon_Door.get_rect()
    Closed_Dungeon_Door_Rect.height -= 20
    Closed_Dungeon_Door_Rect.x, Closed_Dungeon_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
    Interaction_Door_Rect = pygame.rect.Rect(Closed_Dungeon_Door_Rect.x,
                                             Closed_Dungeon_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)

    # [ < Sprite >, < Rectangle >, < Collision > ] :
    Closed_Dungeon_Door = [Closed_Dungeon_Door, Closed_Dungeon_Door_Rect, True]  # Need to be mutable
    Worlds.Level_Objects.__getitem__(2).pop()
    Worlds.Level_Objects.__getitem__(2).append(Closed_Dungeon_Door)

    Worlds.Level_Interactions.__getitem__(2).pop()
    Worlds.Level_Interactions.__getitem__(2).append(
        [Closed_Dungeon_Door, World.World.tiles_dict.__getitem__(42), Interaction_Door_Rect, False,
         open_door])

    # ----------------------------------------- THIRD WORLD RESTART -------------------------------------- #

    Closed_Dungeon_Door = World.World.tiles_dict.__getitem__(40)
    Closed_Dungeon_Door_Rect = Closed_Dungeon_Door.get_rect()
    Closed_Dungeon_Door_Rect.height -= 20
    Closed_Dungeon_Door_Rect.x, Closed_Dungeon_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
    Interaction_Door_Rect = pygame.rect.Rect(Closed_Dungeon_Door_Rect.x,
                                             Closed_Dungeon_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)

    # [ < Sprite >, < Rectangle >, < Collision > ] :
    Closed_Dungeon_Door = [Closed_Dungeon_Door, Closed_Dungeon_Door_Rect, True]  # Need to be mutable
    Worlds.Third_World_Objects.pop()
    Worlds.Third_World_Objects.pop()
    Worlds.Third_World_Objects.append(Closed_Dungeon_Door)

    # [ < Previous Object >, < Open Door Sprite >, < Interaction Rectangle >,
    # < Interaction ( tells if the interaction happened ) >, < Function of Interaction > ] :
    Worlds.Third_World_Rect_Interactions.pop()
    Worlds.Third_World_Rect_Interactions.append([Closed_Dungeon_Door, World.World.tiles_dict.__getitem__(42),
                                          Interaction_Door_Rect, False, open_door])

    Door_Rect = pygame.rect.Rect(Game_Constants.grid_spacing * 19, Game_Constants.grid_spacing * 21 + 8,
                                 Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing * 2)
    Door_Rect = (None, Door_Rect, True)
    Worlds.Third_World_Objects.append(Door_Rect)

    # ----------------------------------------- SIXTH WORLD RESTART -------------------------------------- #

    Closed_Dungeon_Door = World.World.tiles_dict.__getitem__(40)
    Closed_Dungeon_Door_Rect = Closed_Dungeon_Door.get_rect()
    Closed_Dungeon_Door_Rect.height -= 20
    Closed_Dungeon_Door_Rect.x, Closed_Dungeon_Door_Rect.y = Game_Constants.grid_spacing * 19, 0
    Interaction_Door_Rect = pygame.rect.Rect(Closed_Dungeon_Door_Rect.x,
                                             Closed_Dungeon_Door_Rect.y + Game_Constants.grid_spacing * 2,
                                             Game_Constants.grid_spacing * 2, Game_Constants.grid_spacing)

    # [ < Sprite >, < Rectangle >, < Collision > ] :
    Closed_Dungeon_Door = [Closed_Dungeon_Door, Closed_Dungeon_Door_Rect, True]  # Need to be mutable
    Worlds.Sixth_World_Objects.pop()
    Worlds.Sixth_World_Objects.append(Closed_Dungeon_Door)

    # [ < Previous Object >, < Open Door Sprite >, < Interaction Rectangle >,
    # < Interaction ( tells if the interaction happened ) >, < Function of Interaction > ] :
    Worlds.Sixth_World_Interactions.pop()
    Worlds.Sixth_World_Interactions.append([Closed_Dungeon_Door, World.World.tiles_dict.__getitem__(42),
                                     Interaction_Door_Rect, False, open_door])

    # --------------------------------------- SEVENTH WORLD RESTART ------------------------------------ #

    Seventh_World_Enemies = []

    Demon_Boss = Monster.Monster(Game_Constants.Window_width / 2, Game_Constants.Window_height / 2 - 200, "demon")
    Seventh_World_Enemies.append(Demon_Boss)

    Worlds.Level_Enemies[7] = Seventh_World_Enemies

    # ---------------------------------------------------------------------------------------------------- #

    Worlds.Level_Enemies[4] = Worlds.Level_Enemies[5] = Worlds.Level_Enemies[6] = []

    # ---------------------------------------------------------------------------------------------------- #

    Worlds.Level_Spawn_Location = {1: (Game_Constants.Window_width / 2 - 16 * Game_Constants.grid_spacing - 16,
                                       Game_Constants.Window_height / 2 + 18),
                                   2: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64),
                                   3: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64),
                                   4: (Game_Constants.Window_width - 64, Game_Constants.Window_height / 2),
                                   5: (64, Game_Constants.Window_height / 2),
                                   6: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64),
                                   7: (Game_Constants.Window_width / 2, Game_Constants.Window_height - 64)}

    Worlds.World_Raids = {1: [], 2: [], 3: [],

               4: ([lambda: raid(Worlds.current_player, 5, 0, Worlds.Level_Enemies.__getitem__(4), wanted_monsters_list=["imp"]),
                    lambda: raid(Worlds.current_player, 6, 0, Worlds.Level_Enemies.__getitem__(4), wanted_monsters_list=["zombie", "skeleton"]),
                    lambda: raid(Worlds.current_player, 5, 0, Worlds.Level_Enemies.__getitem__(4), wanted_monsters_list=["zombie", "goblin"])], [True, True, True]),

               5: ([lambda: raid(Worlds.current_player, 5, 0, Worlds.Level_Enemies.__getitem__(5), wanted_monsters_list=["imp"]),
                    lambda: raid(Worlds.current_player, 6, 0, Worlds.Level_Enemies.__getitem__(5), wanted_monsters_list=["zombie", "skeleton"]),
                    lambda: raid(Worlds.current_player, 5, 0, Worlds.Level_Enemies.__getitem__(5), wanted_monsters_list=["skeleton", "goblin"])], [True, True, True]),

               6: ([lambda: raid(Worlds.current_player, 6, 0, Worlds.Level_Enemies.__getitem__(6), wanted_monsters_list=["zombie", "skeleton"]),
                    lambda: raid(Worlds.current_player, 4, 0, Worlds.Level_Enemies.__getitem__(6), wanted_monsters_list=["goblin"]),
                    lambda: raid(Worlds.current_player, 4, 0, Worlds.Level_Enemies.__getitem__(6), wanted_monsters_list=["muddy", "goblin"]),
                    lambda: raid(Worlds.current_player, 5, 0, Worlds.Level_Enemies.__getitem__(6), wanted_monsters_list=["muddy"])], [True, True, True, True]),

               7: []}

    Worlds.Level_Items = {
        1: [Item.Item(Game_Constants.grid_spacing * 37 + 16, Game_Constants.grid_spacing * 17, "emerald")],
        2: [],
        3: [Item.Item(Game_Constants.grid_spacing * 19 + 16, Game_Constants.grid_spacing * 11,
                      "steel_bow")],
        4: [], 5: [],
        6: [Item.Item(Game_Constants.grid_spacing * 19 + 16, Game_Constants.grid_spacing * 11,
                      "gold_bow")],
        7: []}

    Worlds.current_player = Character.Character(Game_Constants.Window_width / 2 - 16 * Game_Constants.grid_spacing - 16,
                                                Game_Constants.Window_height / 2 + 18, Game_Constants.player_standard_health)

    aux_group = pygame.sprite.Group()
    aux_group.add(Item.Item(Game_Constants.grid_spacing * 37 + 16, Game_Constants.grid_spacing * 17, "emerald"))

    change_level(screen, World.World(), Worlds.current_player, 1, aux_group, pygame.sprite.Group(), pygame.sprite.Group())


def death_screen(screen: object, is_fullscreen: bool = False) -> None:
    global interrupt_flag

    Screen = screen
    FullScreen = is_fullscreen

    Worlds.Start_Fade = True
    Worlds.Current_Fade_Animation = Worlds.Fade_Animation[1]
    Worlds.Do_Fade = 1

    for fade in Worlds.Fade_Animation:
        fade.change_rate = Game_Constants.second_fade_transition_rate

    game_clock = pygame.time.Clock()

    # Getting the custom pointer :
    custom_pointer = Background_Images.Pointer
    pointer_rect = custom_pointer.get_rect()
    pointer_rect.center = pygame.mouse.get_pos()

    go_restart = False
    go_menu = False

    Death_Title = (Titles_Images.Death_Title, Titles_Images.Death_Title_Rect)
    Death_Title[1].x, Death_Title[1].y = (Game_Constants.Window_width - Titles_Images.Death_Title.get_width()) / 2, \
                                         Game_Constants.Window_height / 15
    Death_Title = FloatingText.FloatingText(Death_Title[1].x, Death_Title[1].y, Death_Title[0])

    Restart_Button = (Buttons.Restart_Button, Buttons.Restart_Button_Rect)
    Restart_Button[1].center = (Game_Constants.Window_width / 2, 9 * Game_Constants.Window_height / 18)
    Restart_Button = FloatingText.FloatingText(Restart_Button[1].x, Restart_Button[1].y, Restart_Button[0],
                                               speed=0.08, amplitude=2)

    Restart_Button_Pressed = (Buttons.Restart_Button_Pressed, Buttons.Restart_Button_Pressed_Rect)
    Restart_Button_Pressed[1].center = Restart_Button.rect.center
    Restart_Button_Pressed = FloatingText.FloatingText(Restart_Button_Pressed[1].x, Restart_Button_Pressed[1].y,
                                                       Restart_Button_Pressed[0], speed=0.08, amplitude=2)

    Menu_Button = (Buttons.Menu_Button, Buttons.Menu_Button_Rect)
    Menu_Button[1].center = (Game_Constants.Window_width / 2, 13 * Game_Constants.Window_height / 18)
    Menu_Button = FloatingText.FloatingText(Menu_Button[1].x, Menu_Button[1].y, Menu_Button[0],
                                            speed=0.08, amplitude=2)

    Menu_Button_Pressed = (Buttons.Menu_Button_Pressed, Buttons.Menu_Button_Pressed_Rect)
    Menu_Button_Pressed[1].center = Menu_Button.rect.center
    Menu_Button_Pressed = FloatingText.FloatingText(Menu_Button_Pressed[1].x, Menu_Button_Pressed[1].y,
                                                    Menu_Button_Pressed[0], speed=0.08, amplitude=2)

    Game_Loop = True
    while Game_Loop:
        Screen.fill(Game_Constants.BLACK_COLOR)
        game_clock.tick(Game_Constants.FPS)

        Sound_Effects.Menu_Music.play_loop()

        # Death Title :
        Death_Title.draw(Screen)
        Death_Title.update()

        if not pointer_rect.colliderect(Restart_Button.rect):
            Restart_Button.draw(Screen)
            Restart_Button.update()
            Restart_Button_Pressed.rect.center = Restart_Button.rect.center
        else:
            Restart_Button_Pressed.draw(Screen)

            left_mouse_pressed = pygame.mouse.get_pressed()[0]

            if left_mouse_pressed and not Worlds.Do_Fade:
                Sound_Effects.Button_Pressed.play()
                Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]
                Worlds.Current_Fade_Animation.restart()
                Worlds.Do_Fade = 1
                go_restart = True

        if not pointer_rect.colliderect(Menu_Button.rect):
            Menu_Button.draw(Screen)
            Menu_Button.update()
            Menu_Button_Pressed.rect.center = Menu_Button.rect.center

        else:
            Menu_Button_Pressed.draw(Screen)
            left_mouse_pressed = pygame.mouse.get_pressed()[0]

            if left_mouse_pressed and not Worlds.Do_Fade:
                Sound_Effects.Button_Pressed.play()
                Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]
                Worlds.Current_Fade_Animation.restart()
                Worlds.Do_Fade = 1
                go_menu = True

        if pointer_rect.colliderect(Restart_Button.rect) or pointer_rect.colliderect(Menu_Button.rect):
            Sound_Effects.Button.play_once()
            Sound_Effects.Button.just_one_time = True
        else:
            Sound_Effects.Button.just_one_time = False

        if Worlds.Do_Fade:

            Worlds.Current_Fade_Animation.draw(Screen)

            if not Worlds.Current_Fade_Animation.end_fade:
                Worlds.Current_Fade_Animation.update()

            else:

                Worlds.Current_Fade_Animation.restart()

                Worlds.Do_Fade -= 1

                if go_menu:
                    go_restart = False
                if go_restart:
                    go_menu = False

                if go_menu:
                    Sound_Effects.Menu_Music.stop()
                    restart(Screen)
                    menu(Screen, is_fullscreen)

                if go_restart:
                    Sound_Effects.Menu_Music.stop()
                    restart(Screen)
                    play(Screen, is_fullscreen)

        for Event in pygame.event.get():
            if Event.type == pygame.QUIT:  # Event for closing the game window.
                Game_Loop = False
                interrupt_flag = True

            if Event.type == pygame.KEYDOWN:
                if Event.key == pygame.K_F11:
                    if FullScreen:
                        Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                          Game_Constants.Window_height))
                        FullScreen = not FullScreen
                    else:
                        Screen = pygame.display.set_mode((Game_Constants.Window_width,
                                                          Game_Constants.Window_height), pygame.FULLSCREEN)
                        FullScreen = not FullScreen

                if Event.key == pygame.K_RETURN and not (go_restart or go_menu):
                    Sound_Effects.Button_Pressed.play()
                    Worlds.Current_Fade_Animation = Worlds.Fade_Animation[0]
                    Worlds.Current_Fade_Animation.restart()
                    Worlds.Do_Fade = 1
                    go_restart = True

        # Updating the Pointer :
        pygame.mouse.set_visible(False)  # Hiding the original pointer
        Pointer_rect = pointer_rect
        Pointer_rect.center = pygame.mouse.get_pos()
        if (0 < pygame.mouse.get_pos()[0] < Game_Constants.Window_width - 1) and \
                (Game_Constants.Window_height - 1 > pygame.mouse.get_pos()[1] > 0):
            Screen.blit(custom_pointer, Pointer_rect.center)

        pygame.display.update()

    pygame.quit()


def raid(current_player: Character, quantity: int, frequency: Union[int, float], world_enemy_list: list,
         coordinate_x: Union[int, float] = None, coordinate_y: Union[int, float] = None,
         wanted_monsters_list: list = list(Monster.Monster.monster_dict.keys()),
         __counter__: int = 0, __interval_time__: Union[int, float] = pygame.time.get_ticks()) -> None:
    global interrupt_flag

    def run_raid() -> bool:

        nonlocal coordinate_x, coordinate_y, __counter__, __interval_time__

        # Don't change the variables "__counter__" and "__interval_time__". It is a parameter used to generate the
        # desired amount of monsters using recursion.

        if __counter__ < quantity:

            if pygame.time.get_ticks() - __interval_time__ > frequency:

                __interval_time__ = pygame.time.get_ticks()
                __counter__ += 1

                # coordinate_x = coordinate_x if coordinate_x else random.randint()

                if not coordinate_x:
                    aux_coordinate_x = random.randint(64, Game_Constants.Window_width - 64)

                if not coordinate_y:
                    aux_coordinate_y = random.randint(64, Game_Constants.Window_height - 64)

                if not coordinate_x or not coordinate_y:  # If at least one of the coordinates is random

                    if not coordinate_x and not coordinate_y:  # If both coordinates is random

                        while distance((aux_coordinate_x, aux_coordinate_y), current_player.rect.center) \
                                <= Game_Constants.minimum_enemy_spawn_distance:
                            # Generating a new coordinate with minimum distance from the player :

                            aux_coordinate_x = random.randint(64, Game_Constants.Window_width - 64)
                            aux_coordinate_y = random.randint(64, Game_Constants.Window_height - 64)

                    else:

                        if not coordinate_x:

                            while distance((aux_coordinate_x, aux_coordinate_y), current_player.rect.center) \
                                    <= Game_Constants.minimum_enemy_spawn_distance:
                                # Generating a new coordinate with minimum distance from the player :

                                aux_coordinate_x = random.randint(64, Game_Constants.Window_width - 64)
                        else:

                            while distance((aux_coordinate_x, aux_coordinate_y), current_player.rect.center) \
                                    <= Game_Constants.minimum_enemy_spawn_distance:
                                # Generating a new coordinate with minimum distance from the player :

                                aux_coordinate_y = random.randint(64, Game_Constants.Window_height - 64)

                # Generation is random based on the given monster list :
                current_monster = Monster.Monster(aux_coordinate_x, aux_coordinate_y,
                                                  random.choice(wanted_monsters_list))
                world_enemy_list.append(current_monster)

            # Recursion Call :
            raid(current_player, quantity, frequency, world_enemy_list, coordinate_x=coordinate_x,
                 coordinate_y=coordinate_y,
                 wanted_monsters_list=wanted_monsters_list, __counter__=__counter__,
                 __interval_time__=__interval_time__)

        else:  # End of the current raid :

            while Worlds.Level_Enemies.__getitem__(Worlds.current_level):  # If Player not killed all enemies
                time.sleep(0.05)

                if interrupt_flag:
                    return True

            if Worlds.current_level not in {4, 5, 6}:
                Worlds.raid_index = 0
                return True

            # If player has defeated the Raid :
            Worlds.World_Raids.__getitem__(Worlds.current_level)[1][Worlds.raid_index] = False

            Worlds.raid_index += 1

            # Calling the next raid :
            try:
                Worlds.World_Raids.__getitem__(Worlds.current_level)[0][Worlds.raid_index]()
            except IndexError:
                Worlds.raid_index = 0
                return True  # End of the raid.

    thread = threading.Thread(target=run_raid)
    thread.start()
