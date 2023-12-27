import pygame

from MyFunctions import MyFunctions
from Constants import Game_Constants

pygame.init()

Imp_Idle_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/imp_mob/idle/idle_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]

Imp_Run_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/imp_mob/run/run_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]


Skeleton_Idle_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/skeleton_mob/idle/idle_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]

Skeleton_Run_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/skeleton_mob/run/run_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]


Muddy_Idle_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/muddy_mob/idle/idle_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]

Muddy_Run_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/muddy_mob/run/run_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]


Zombie_Idle_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/zombie_mob/idle/idle_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]

Zombie_Run_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/zombie_mob/run/run_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]


Goblin_Idle_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/goblin_mob/idle/idle_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]

Goblin_Run_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/goblin_mob/run/run_{i}.png"),
                                                   Game_Constants.SCALE) for i in range(4)]


Demon_Idle_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/demon_mob/idle/idle_{i}.png"),
                                                   Game_Constants.SCALE + 1) for i in range(4)]

Demon_Run_Animation = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Mobs/demon_mob/run/run_{i}.png"),
                                                   Game_Constants.SCALE + 1) for i in range(4)]


