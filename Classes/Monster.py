# Same as Character Class.
import pygame
import math
import random

from typing import Union

import Assets.Monster_Images

from Assets import Sound_Effects
from Assets import Health_Bar
from MyFunctions import MyFunctions
from Constants import Game_Constants
from Classes import Boss_Fireball
from Classes import Bone
from Classes import Weapon
from Classes import Character
from Classes import Item

pygame.init()


class Monster:
    Animation_Cooldown = Game_Constants.animation_cooldown

    # Dictionary of monsters with their respective images and health :
    # Monster = [ < Idle Animation >, < Running Animation >, < Monster Health >, < Monster Damage >, < Monster Speed >, < Shoot Cooldown (ms) > ]
    monster_dict = dict(
        imp=[Assets.Monster_Images.Imp_Idle_Animation, Assets.Monster_Images.Imp_Run_Animation, 100, 10, 1, 0],
        skeleton=[Assets.Monster_Images.Skeleton_Idle_Animation, Assets.Monster_Images.Skeleton_Run_Animation, 75, 10,
                  1.7, 2000],
        goblin=[Assets.Monster_Images.Goblin_Idle_Animation, Assets.Monster_Images.Goblin_Run_Animation, 200, 10, 3, 0],
        muddy=[Assets.Monster_Images.Muddy_Idle_Animation, Assets.Monster_Images.Muddy_Run_Animation, 300, 20, 2, 0],
        zombie=[Assets.Monster_Images.Zombie_Idle_Animation, Assets.Monster_Images.Zombie_Run_Animation, 125, 10, 1.5,
                0],
        demon=[Assets.Monster_Images.Demon_Idle_Animation, Assets.Monster_Images.Demon_Run_Animation, 3_000, 20, 2,
               3_000])

    def __init__(self, coordinate_x: Union[int, float], coordinate_y: Union[int, float], current_monster: str):

        assert (current_monster in Monster.monster_dict), f"Given monster doesn't exist. Try these: " \
                                                          f"{list(Monster.monster_dict.keys())}"

        self.alive = True
        self.can_move = True
        self.flip = False
        self.arrow_collision = True
        self.stunned = False
        self.hit = False
        self.can_act = False
        self.create_check = False

        self.frame_index = 0
        self.action = 0  # 0 : Idle // 1 : Running

        self.shoot_cooldown = Monster.monster_dict.__getitem__(current_monster)[5]

        self.current_monster = current_monster
        self.health = Monster.monster_dict.__getitem__(current_monster)[2]
        self.damage = Monster.monster_dict.__getitem__(current_monster)[3]

        # 20% Faster or 20% Slow for Normal Monsters :
        self.speed = Monster.monster_dict.__getitem__(current_monster)[4]

        self.reaction_cooldown = Game_Constants.monsters_reaction_cooldown if self.current_monster != "demon" \
            else Game_Constants.demon_reaction_cooldown
        self.time_to_react = 0
        self.update_time = pygame.time.get_ticks()
        self.last_hit = pygame.time.get_ticks()
        self.last_shot = pygame.time.get_ticks()
        self.counter_1 = pygame.time.get_ticks()  # Variable To Set Cooldown For Standard Sword Damage.
        self.counter_2 = pygame.time.get_ticks()  # Variable To Set Cooldown For Second Sword Damage.

        self.animation = Monster.monster_dict.__getitem__(self.current_monster)[0]
        self.monster_image = self.animation[self.frame_index]
        self.rect = self.monster_image.get_rect()
        self.rect.center = (coordinate_x, coordinate_y)

        if self.current_monster == "demon":
            self.health_bar_base = Health_Bar.Boss_Health_Bar_Base
            self.original_health_bar = Health_Bar.Boss_Health_Bar
            self.health_bar = self.original_health_bar
            self.health_bar_rect = self.health_bar.get_rect()
            self.health_bar_rect.center = self.health_bar_base.rect.centerx, self.health_bar_base.rect.centery + 4

    def update(self, weapon: Weapon, character: Character, item_group: object, second_sword: Weapon = None) -> tuple:
        # Reseting Variables :
        return_damage, damage_position = 0, None

        # Check if monster has died :
        if self.health <= 0:
            self.health, self.alive = 0, False

            # Drop Spaw :
            if random.randint(0, Game_Constants.drop_rate) == Game_Constants.drop_rate:
                # 70% coin, 24% silver coin, 5% red coin and 1% emerald :
                item_dropped = ["coin"] * 70 + ["silver_coin"] * 24 + ["red_coin"] * 5 + ["emerald"] * 1
                item_dropped = random.choice(item_dropped)  # Picks a random item from the list
                item_dropped = Item.Item(self.rect.centerx, self.rect.centery, item_dropped)
                item_group.add(item_dropped)

        if self.can_act:

            if self.current_monster == "zombie":
                if self.health < Monster.monster_dict.__getitem__("zombie")[2] // 2:
                    # Increase the Zombie Speed in 70% :
                    self.speed = Monster.monster_dict.__getitem__("zombie")[4] * 1.7

            if self.current_monster == "demon":
                if self.health <= Monster.monster_dict.__getitem__(self.current_monster)[2] // 2:
                    # Shoots 25% faster :
                    self.shoot_cooldown = Monster.monster_dict.__getitem__(self.current_monster)[5] * 3 // 4
                    self.speed = Monster.monster_dict.__getitem__(self.current_monster)[4] + 0.2

                if self.health <= Monster.monster_dict.__getitem__(self.current_monster)[2] // 4:
                    # Shoots 75% faster :
                    self.shoot_cooldown = Monster.monster_dict.__getitem__(self.current_monster)[5] // 4
                    self.speed = Monster.monster_dict.__getitem__(self.current_monster)[4] + 0.3

            if pygame.time.get_ticks() - self.last_hit > Game_Constants.stun_enemy_cooldown:
                self.stunned = False

            # Handle Animation and update image.
            self.monster_image = self.animation[self.frame_index]

            # Check if enough time has passed since the last update.
            if pygame.time.get_ticks() - self.update_time >= Monster.Animation_Cooldown:
                animation_length = len(self.animation)
                self.frame_index = (self.frame_index + 1) % animation_length
                self.update_time = pygame.time.get_ticks()

            # Check for Sword Damage :
            if weapon.current_weapon == "Sword" and \
                    (pygame.time.get_ticks() - self.counter_1 >= Game_Constants.sword_damage_cooldown) and \
                    self.rect.colliderect(weapon.sword_hitbox) and self.alive:
                self.counter_1 = pygame.time.get_ticks()
                return_damage = Game_Constants.sword_base_damage + \
                                random.randint((-1) * int(Game_Constants.sword_base_damage * 3 / 10),
                                               int(Game_Constants.sword_base_damage * 3 / 10))
                damage_position = self.rect
                self.health -= return_damage
                self.hit = True
                Sound_Effects.Sword_Slice.play()

            # Check for Second Sword Damage :
            if second_sword:
                if weapon.current_weapon == "Sword" and \
                        (pygame.time.get_ticks() - self.counter_2 >= Game_Constants.sword_damage_cooldown) and \
                        self.rect.colliderect(second_sword.sword_hitbox) and self.alive:
                    self.counter_2 = pygame.time.get_ticks()
                    return_damage = Game_Constants.sword_base_damage + \
                                    random.randint((-1) * int(Game_Constants.sword_base_damage * 3 / 10),
                                                   int(Game_Constants.sword_base_damage * 3 / 10))
                    damage_position = self.rect
                    self.health -= return_damage
                    self.hit = True
                    Sound_Effects.Sword_Slice.play()

            if character.teleportation:
                return_damage, damage_position = 0, None
        else:
            if self.create_check:
                if pygame.time.get_ticks() - self.time_to_react > self.reaction_cooldown:
                    self.can_act = True
            else:
                self.create_check = True
                self.time_to_react = pygame.time.get_ticks()

        return return_damage, damage_position

    def movement(self, dx: int, dy: int, obstacles: list) -> None:  # Update the monster's position.

        if dx != 0 or dy != 0:  # Movement animation.
            MyFunctions.set_animation(self, Monster.monster_dict.__getitem__(self.current_monster)[1])
        else:  # Idle animation.
            MyFunctions.set_animation(self, Monster.monster_dict.__getitem__(self.current_monster)[0])

        # Checks if animation needs to be flipped :
        if dx < 0:
            self.flip = True
        if dx > 0:
            self.flip = False

        if dx != 0 and dy != 0:  # Diagonal movement.
            dx = float('%.0f' % (dx / math.sqrt(1.78)))
            dy = float('%.0f' % (dy / math.sqrt(1.78)))

        if dx > 0:
            dx /= 1.1

        self.rect.x += dx

        for obstacle in obstacles:
            if obstacle[2]:
                if obstacle[1].colliderect(self.rect):
                    if dx > 0:
                        self.rect.right = obstacle[1].left
                    if dx < 0:
                        self.rect.left = obstacle[1].right

        self.rect.y += dy

        for obstacle in obstacles:
            if obstacle[2]:
                if obstacle[1].colliderect(self.rect):
                    if dy > 0:
                        self.rect.bottom = obstacle[1].top
                    if dy < 0:
                        self.rect.top = obstacle[1].bottom

    def ai(self, current_player: Character, current_obstacles: list, enemy_projectiles_group: object) -> None:
        if self.can_act:
            clipped_line: tuple = ()

            ai_dx = 0
            ai_dy = 0

            # Create a line of sigth from the enemy to the player :
            line_of_sight = (self.rect.center, current_player.rect.center)

            for obstacle in current_obstacles:
                if obstacle[1].clipline(line_of_sight) and obstacle[2]:
                    clipped_line = obstacle[1].clipline(line_of_sight)

            # Check distance from the player :
            distance = math.sqrt((self.rect.centerx - current_player.rect.centerx) ** 2 +
                                 (self.rect.centery - current_player.rect.centery) ** 2)

            if not clipped_line and distance > Game_Constants.distance_player_enemy_range:

                if self.rect.centerx > current_player.rect.centerx:
                    ai_dx = (-1) * self.speed
                if self.rect.centerx < current_player.rect.centerx:
                    ai_dx = self.speed

                if self.rect.centery > current_player.rect.centery:
                    ai_dy = (-1) * self.speed
                if self.rect.centery < current_player.rect.centery:
                    ai_dy = self.speed

                if abs(current_player.rect.centerx - self.rect.centerx) <= 2:  # To avoid abnormalities in enemy movement.
                    ai_dx = 0

                if abs(current_player.rect.centery - self.rect.centery) <= 2:  # To avoid abnormalities in enemy movement.
                    ai_dy = 0

            if not self.stunned and self.can_move:
                # Move towards Player :
                self.movement(ai_dx, ai_dy, current_obstacles)

                # Attack Player :
                if distance < Game_Constants.attack_range and not current_player.hit:
                    if current_player.take_damage:
                        current_player.health -= self.damage
                        random.choice(Sound_Effects.Damage_Sound_Effect).play()
                        current_player.hit = True
                        current_player.last_hit = pygame.time.get_ticks()

                if self.current_monster == "skeleton":
                    if pygame.time.get_ticks() - self.last_shot > self.shoot_cooldown + \
                            random.randint(0, 3 * self.shoot_cooldown):
                        self.last_shot = pygame.time.get_ticks()

                        auxiliary_bone = Bone.Bone(self.rect.centerx, self.rect.centery, current_player.rect.center)
                        random.choice(Sound_Effects.Bone_Sound_Effect).play()
                        enemy_projectiles_group.add(auxiliary_bone)

                if self.current_monster == "demon":
                    if pygame.time.get_ticks() - self.last_shot > self.shoot_cooldown:
                        self.last_shot = pygame.time.get_ticks()

                        fireballs = (
                        Boss_Fireball.Boss_Fireball(self.rect.centerx, self.rect.centery, current_player.rect.center),
                        Boss_Fireball.Boss_Fireball(self.rect.centerx, self.rect.centery, current_player.rect.center,
                                                    angle_increment=25),
                        Boss_Fireball.Boss_Fireball(self.rect.centerx, self.rect.centery, current_player.rect.center,
                                                    angle_increment=(-25)))

                        for fireball in fireballs:
                            enemy_projectiles_group.add(fireball)

                        Sound_Effects.Fireball_Whoosh.play()

            # Check if hit :
            if self.hit:
                self.hit = False
                self.stunned = True
                self.last_hit = pygame.time.get_ticks()
                MyFunctions.set_animation(self, Monster.monster_dict.__getitem__(self.current_monster)[0])

    def draw(self, surface: object) -> None:  # Draws the monster on the given surface.
        if self.alive:
            flipped_img = pygame.transform.flip(self.monster_image, self.flip, False)
            surface.blit(flipped_img, (self.rect.x, self.rect.y))
            # pygame.draw.rect(surface, Game_Constants.WHITE_COLOR, self.rect, 1)

            if self.current_monster == "demon":
                self.health_bar_base.rect.x, self.health_bar_base.original_y = self.rect.x - 40, self.rect.y - 54
                self.health_bar_base.update_2()
                self.health_bar_rect.center = self.health_bar_base.rect.centerx, self.health_bar_base.rect.centery + 4

                self.health_bar_base.draw(surface)

                health_bar_ratio = self.health / Monster.monster_dict.__getitem__("demon")[2]
                self.health_bar = self.original_health_bar.subsurface(0, 0, max(0, math.floor(self.original_health_bar.get_width() * health_bar_ratio)), self.original_health_bar.get_height())

                surface.blit(self.health_bar, (self.health_bar_rect.x, self.health_bar_rect.y))
