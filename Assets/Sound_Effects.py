from Classes import MySound

#
# The first argument is the name of the sound and the second is the volume of the sound ;
#
# Volume: 0.000 -> 1.000  ( Example: 0.65 )
#

Wind_Sound = MySound.MySound("wind")
Dungeon_Air = MySound.MySound("dungeon_air")
Open_Door = MySound.MySound("open_door")
Close_Door = MySound.MySound("close_door")
Closed_Door = MySound.MySound("closed_door", 0.3)

Coin_Collect = MySound.MySound("coin_collect")
Silver_Coin_Collect = MySound.MySound("silver_coin_collect")
Red_Coin_Collect = MySound.MySound("red_coin_collect")
Emerald_Collect = MySound.MySound("emerald_collect")
Red_Potion_Collect = MySound.MySound("red_potion")
Weapon_Collect = MySound.MySound("weapon_collect", 0.5)

Walking_Sound = MySound.MySound("walking")
Echo_Walking_Sound = MySound.MySound("echo_walking")
Grass_Walking_Sound = MySound.MySound("grass_walk")
Dash_Sound = MySound.MySound("dash")
Teleport_Sound = MySound.MySound("teleport")
Death_Sound_Effect = MySound.MySound("player_death", 0.5)
Damage_Sound_Effect = [MySound.MySound("damage_sound_1"), MySound.MySound("damage_sound_2")]
Regeneration_Sound = MySound.MySound("regeneration")
Ultimate_Sound = MySound.MySound("ultimate")

Sword_Pull = MySound.MySound("sword")
Double_Sword_Pull = MySound.MySound("double_sword")
Sword_Slice = MySound.MySound("sword_slice", 0.5)
Bow_Pull = MySound.MySound("bow")
Steel_Bow_Pull = MySound.MySound("steel_bow")
Gold_Bow_Pull = MySound.MySound("gold_bow")
Normal_Arrow_Sound = MySound.MySound("arrow")
Arrow_Impact = MySound.MySound("arrow_impact", 0.25)
Arrow_Recoil = MySound.MySound("arrow_recoil")

Fireball_Whoosh = MySound.MySound("fireball_whoosh")
Fireball_Recoil = MySound.MySound("fireball_recoil", 0.3)
Fireball_Impact = MySound.MySound("fireball_impact", 0.2)
Bone_Sound_Effect = [MySound.MySound("bone_sound_1"), MySound.MySound("bone_sound_2")]
Bone_Impact = MySound.MySound("bone_impact")

Button = MySound.MySound("button", 0.5)
Button_Pressed = MySound.MySound("button_pressed", 0.5)

Menu_Music = MySound.MySound("menu_music", 0.5)
First_Level_Music = (MySound.MySound("first_level_stand_music", 0.5), MySound.MySound("first_level_stand_music", 0.5))
Second_Level_Music = (MySound.MySound("second_level_stand_music", 0.3), MySound.MySound("second_level_combat_music", 0.3))
Dungeon_Music = (MySound.MySound("dungeon_stand_music", 0.5), MySound.MySound("dungeon_combat_music", 0.3))
Boss_Fight_Music = (MySound.MySound("first_level_stand_music", 0.5), MySound.MySound("boss_fight_music", 0.3))
