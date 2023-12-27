import pygame

pygame.init()


class MySound:

    # All Sounds Avaible :
    sound_dict = dict(wind="Assets/Sounds/Ambient_Sounds/Wind_Sound.wav",
                      dungeon_air="Assets/Sounds/Ambient_Sounds/Dungeon_Air.wav",
                      open_door="Assets/Sounds/Ambient_Sounds/Open_Door_Sound_Effect.wav",
                      close_door="Assets/Sounds/Ambient_Sounds/Door_Slam.wav",
                      closed_door="Assets/Sounds/Ambient_Sounds/Closed_Door.wav",

                      coin_collect="Assets/Sounds/Item_Sounds/Coin_Collect.wav",
                      silver_coin_collect="Assets/Sounds/Item_Sounds/Silver_Coin_Collect.wav",
                      red_coin_collect="Assets/Sounds/Item_Sounds/Red_Coin_Collect.wav",
                      emerald_collect="Assets/Sounds/Item_Sounds/Emerald_Collect(1).wav",
                      red_potion="Assets/Sounds/Item_Sounds/Red_Potion_Collect(2).wav",
                      weapon_collect="Assets/Sounds/Item_Sounds/Weapon_Collect.wav",

                      walking="Assets/Sounds/Player_Sounds/Walking.wav",
                      echo_walking="Assets/Sounds/Player_Sounds/Echo_Walking.wav",
                      grass_walk="Assets/Sounds/Player_Sounds/Grass_Walk.wav",
                      dash="Assets/Sounds/Player_Sounds/Dash_Sound.wav",
                      teleport="Assets/Sounds/Player_Sounds/Teleport_Sound.wav",
                      player_death="Assets/Sounds/Player_Sounds/Death_Sound_Effect.wav",
                      damage_sound_1="Assets/Sounds/Player_Sounds/Damage_Sound_Effect(1).wav",
                      damage_sound_2="Assets/Sounds/Player_Sounds/Damage_Sound_Effect(2).wav",
                      regeneration="Assets/Sounds/Player_Sounds/Regeneration_Sound.wav",
                      ultimate="Assets/Sounds/Player_Sounds/Ultimate_Sound.wav",

                      sword="Assets/Sounds/Weapon_Sounds/Sword_Pull.wav",
                      double_sword="Assets/Sounds/Weapon_Sounds/Double_Sword_Pull_Sound.wav",
                      sword_slice="Assets/Sounds/Weapon_Sounds/Sword_Slice.wav",
                      bow="Assets/Sounds/Weapon_Sounds/Bow_Pull.wav",
                      steel_bow="Assets/Sounds/Weapon_Sounds/Steel_Bow_Pull.wav",
                      gold_bow="Assets/Sounds/Weapon_Sounds/Gold_Bow_Pull.wav",
                      arrow="Assets/Sounds/Weapon_Sounds/Normal_Arrow_Sound.wav",
                      arrow_impact="Assets/Sounds/Weapon_Sounds/Arrow_Impact.wav",
                      arrow_recoil="Assets/Sounds/Weapon_Sounds/Arrow_Recoil.wav",

                      fireball_whoosh="Assets/Sounds/Enemy_Sounds/Fireball_Whoosh.wav",
                      fireball_recoil="Assets/Sounds/Enemy_Sounds/Fireball_Wall_Recoil.wav",
                      fireball_impact="Assets/Sounds/Enemy_Sounds/Fireball_Impact.wav",
                      bone_sound_1="Assets/Sounds/Enemy_Sounds/Bone_Sound(1).wav",
                      bone_sound_2="Assets/Sounds/Enemy_Sounds/Bone_Sound(2).wav",
                      bone_impact="Assets/Sounds/Enemy_Sounds/Bone_Impact.wav",

                      menu_music="Assets/Sounds/Menu_Sounds/Main_Menu_Music.wav",
                      button="Assets/Sounds/Menu_Sounds/Button_Sound.wav",
                      button_pressed="Assets/Sounds/Menu_Sounds/Button_Pressed_Sound.wav",

                      dungeon_combat_music="Assets/Sounds/Musics/Dungeon_Combat_Music.wav",
                      second_level_stand_music="Assets/Sounds/Musics/Second_Level_Stand_Music.wav",
                      second_level_combat_music="Assets/Sounds/Musics/Second_Level_Combat_Music.wav",
                      dungeon_stand_music="Assets/Sounds/Musics/Dungeon_Stand_Music.wav",
                      boss_fight_music="Assets/Sounds/Musics/Boss_Fight_Music.wav",
                      first_level_stand_music="Assets/Sounds/Musics/First_Level_Stand_Music.wav")

    def __init__(self, sound_name: str, volume: float = 1.0, just_one_time: bool = False):

        assert (sound_name in MySound.sound_dict), f"Given sound name doesn't exist. Try these: " \
                                                   f"{list(MySound.sound_dict.keys())}"

        self.is_playing = False

        self.sound = pygame.mixer.Sound(MySound.sound_dict.__getitem__(sound_name))
        self.volume = volume
        self.sound.set_volume(self.volume)
        self.update_time = pygame.time.get_ticks()
        self.audio_length = self.sound.get_length()
        self.just_one_time = just_one_time

    def play(self) -> None:
        # To Just Play the Audio w/ no Restrictions :

        self.sound.play()

    def update(self) -> None:
        # Updating the Audio :

        self.sound.set_volume(self.volume)

        if self.is_playing:
            if pygame.time.get_ticks() - self.audio_length * 1000 > self.update_time:
                self.update_time = pygame.time.get_ticks()
                self.is_playing = False

    def play_once(self) -> None:
        # To Just Play the Audio Once :

        if not self.just_one_time:
            self.play()
            self.just_one_time = True

    def play_loop(self) -> None:
        # To Play the Audio in Loop :

        self.sound.set_volume(self.volume)

        self.update()

        if not self.is_playing:
            self.is_playing = True
            self.play()
            self.update_time = pygame.time.get_ticks()

    def stop(self) -> None:
        # Stop the audio :

        self.is_playing = False
        self.sound.stop()
