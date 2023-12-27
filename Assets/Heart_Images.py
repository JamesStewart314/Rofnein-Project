import pygame

from MyFunctions import MyFunctions
from Constants import Game_Constants

pygame.init()

heart_width = pygame.image.load(f"Assets/Hearts_Assets/full_heart-0.png").get_width()
heart_height = pygame.image.load(f"Assets/Hearts_Assets/full_heart-0.png").get_height()

Full_Heart_Anim = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Hearts_Assets/full_heart-{i}.png"),
                                                (int(heart_width * Game_Constants.hearts_scale),
                                                 int(heart_height * Game_Constants.hearts_scale)))
                                                for i in range(8)]

Half_Heart_Anim = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Hearts_Assets/half_heart-{i}.png"),
                                                (int(heart_width * Game_Constants.hearts_scale),
                                                 int(heart_height * Game_Constants.hearts_scale)))
                                                for i in range(8)]

Empty_Heart_Anim = [MyFunctions.pygame_scale_img(pygame.image.load(f"Assets/Hearts_Assets/empty_heart-{i}.png"),
                                                 (int(heart_width * Game_Constants.hearts_scale),
                                                  int(heart_height * Game_Constants.hearts_scale)))
                                                for i in range(8)]
