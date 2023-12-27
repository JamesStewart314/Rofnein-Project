import pygame

from typing import Union

pygame.init()

Window_width: int = 1_280
Window_height: int = 704
info_bar_height: int = 40
grid_spacing: int = 32
grides_number: int = 40

FPS: int = 60

OFFSET: Union[int, float] = 8
Arrow_Offset: Union[int, float] = 10
distance_player_enemy_range: Union[int, float] = 30
attack_range: Union[int, float] = 40
Sword_radius: Union[int, float] = 35
WEAPON_OFFSET: Union[int, float] = 6

Player_Speed: Union[int, float] = 3
text_oscilation_amplitude: Union[int, float] = 20
floating_text_oscilation_speed: Union[int, float] = 0.05
Fireball_standard_speed: Union[int, float] = 3
enemy_speed: Union[int, float] = 2
Bone_standard_speed: Union[int, float] = 4
Player_Ultimate_Speed: Union[int, float] = Player_Speed * 1.5
damage_text_speed: Union[int, float] = 1
dash_velocity: Union[int, float] = Player_Speed
horizontal_leaf_speed: Union[int, float] = 3
Arrow_standard_speed: Union[int, float] = 8
spirit_arrow_change_velocity: Union[int, float] = 50

player_standard_health: Union[int, float] = 100
hearts_quantity: int = 5
potion_heal: Union[int, float] = player_standard_health / hearts_quantity

drop_rate: int = 2  # 1 = 50% -> (0, 1)   |||   2 = -> 33,3% -> (0, 0, 1) etc...

dash_horizontal_distance: Union[int, float] = 0
dash_vertical_distance: Union[int, float] = 0

animation_cooldown: Union[int, float] = 100
animation_death_cooldown: Union[int, float] = 200
animation_teleport_cooldown: Union[int, float] = 40
animation_hearts_cooldown: Union[int, float] = 250
animation_items_cooldown: Union[int, float] = 80
Board_Leaf_Cooldown: Union[int, float] = 30
dash_animation_cooldown: Union[int, float] = 30
dash_cooldown: Union[int, float] = 2_000  # 2,000 ms = 2 sec
damage_text_cooldown: Union[int, float] = 460
floating_text_oscilation_cooldown: Union[int, float] = 100
fade_animation_cooldown: Union[int, float] = 12
fade_death_cooldown: Union[int, float] = 100
monsters_reaction_cooldown: Union[int, float] = 500
demon_reaction_cooldown: Union[int, float] = 1_000  # 1,000 ms = 1 sec
hit_cooldown: Union[int, float] = 1_000  # 1,000 ms = 1 sec
regenerate_cooldown: Union[int, float] = 40_000  # 40,000 ms = 40 sec
stun_enemy_cooldown: Union[int, float] = 100
sword_damage_cooldown: Union[int, float] = 750
teleport_cooldown: Union[int, float] = 30_000  # 30,000 ms = 30 sec
ultimate_cooldown: Union[int, float] = 60_000  # 60,000 ms = 60 sec = 1 min
ultimate_using_time: Union[int, float] = 7_000  # 7,000 ms = 7 sec
transition_ultimate_cooldown: Union[int, float] = 3_000  # 3,000 ms = 3 sec
weapon_change_cooldown: Union[int, float] = 2_000  # 2,000 ms = 2 sec

SCALE: int = 2
Custom_bows_constant: Union[int, float] = 1.2
damage_text_size: int = 15
Fireball_Scale: int = 1
Bone_Scale: int = 1
item_scale: int = 1
static_coin_scale: Union[int, float] = 1.5
hearts_scale: Union[int, float] = 1.4
Bow_scale: Union[int, float] = 2 / 3
Arrow_scale: int = 1
Sword_scale: int = 1
UI_Icons_Scale: Union[int, float] = 1 / 3

sword_base_damage: Union[int, float] = 15
bone_base_damage: Union[int, float] = 10
standard_arrow_damage: Union[int, float] = 10
fireball_base_damage: Union[int, float] = 20
spirit_arrow_damage: Union[int, float] = 15
phantom_arrow_damage: Union[int, float] = 17
side_arrow_damage_reduction: Union[int, float] = 7 / 10  # 30% damage reduction
side_arrow_damage_reduction_ultimate: Union[int, float] = 2 / 5  # 60% damage reduction

minimum_enemy_spawn_distance: Union[int, float] = 100
opacity_change_rate: Union[int, float] = 5
fade_transition_rate: Union[int, float] = 30
second_fade_transition_rate: Union[int, float] = 3

level_text_time: Union[int, float] = 3000

leafs_quantity: int = 3

# ------------------------------- COLORS SECTION ------------------------------- #

BLACK_COLOR: Union[tuple, list] = (0, 0, 0)
WHITE_COLOR: Union[tuple, list] = (255, 255, 255)
RED_COLOR: Union[tuple, list] = (255, 0, 0)
PURPLE_COLOR: Union[tuple, list] = (128, 0, 128)
YELLOW_COLOR: Union[tuple, list] = (255, 255, 0)
GREEN_COLOR: Union[tuple, list] = (80, 220, 100)
SILVER_COLOR: Union[tuple, list] = (197, 206, 212)
CRIMSON_RED_COLOR: Union[tuple, list] = (153, 0, 0)

# -------------------------------- WORLD SECTION -------------------------------- #

Map_Rows: int = Window_height // 32
Map_Columns: int = Window_width // 32
