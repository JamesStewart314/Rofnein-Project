import pygame

from MyFunctions import MyFunctions
from Constants import Game_Constants

pygame.init()


# --------------------------------------------- WEAPONS -------------------------------------------------- #

# Standard Bow Weapon :
Bow_Img = pygame.image.load("Assets/Weapon/Bow.png")
Bow_Img_Width = Bow_Img.get_width()
Bow_Img_Height = Bow_Img.get_height()
Bow_Img = MyFunctions.pygame_scale_img(Bow_Img, (int(Bow_Img_Width * Game_Constants.Bow_scale),
                                                 int(Bow_Img_Height * Game_Constants.Bow_scale)))

# Steel Bow Weapon :
Steel_Bow_Img = pygame.image.load("Assets/Weapon/Steel_Bow.png")
Steel_Bow_Img_Width = Steel_Bow_Img.get_width()
Steel_Bow_Img_Height = Steel_Bow_Img.get_height()
Steel_Bow_Img = MyFunctions.pygame_scale_img(Steel_Bow_Img,
                (int(Steel_Bow_Img_Width * Game_Constants.Bow_scale * Game_Constants.Custom_bows_constant),
                int(Steel_Bow_Img_Height * Game_Constants.Bow_scale * Game_Constants.Custom_bows_constant)))

# Gold Bow Weapon :
Gold_Bow_Img = pygame.image.load("Assets/Weapon/Gold_Bow.png")
Gold_Bow_Img_Width = Gold_Bow_Img.get_width()
Gold_Bow_Img_Height = Gold_Bow_Img.get_height()
Gold_Bow_Img = MyFunctions.pygame_scale_img(Gold_Bow_Img,
                (int(Gold_Bow_Img_Width * Game_Constants.Bow_scale * Game_Constants.Custom_bows_constant),
                int(Gold_Bow_Img_Height * Game_Constants.Bow_scale * Game_Constants.Custom_bows_constant)))

# Sword Weapon :
Sword_Img = pygame.image.load("Assets/Weapon/Sword.png")
Sword_Img_Width = Sword_Img.get_width()
Sword_Img_Height = Sword_Img.get_height()
Sword_Img = MyFunctions.pygame_scale_img(Sword_Img, int(Game_Constants.Sword_scale))

# None Weapon :
None_Weapon = pygame.image.load("Assets/Weapon/Blank.png")


# --------------------------------------------- ARROWS -------------------------------------------------- #

# Standard Arrow :
Standard_Arrow = pygame.image.load("Assets/Arrows/Arrow.png")
Standard_Arrow = MyFunctions.pygame_scale_img(Standard_Arrow, Game_Constants.Arrow_scale)

# Spirit Arrow :
Spirit_Arrow = pygame.image.load("Assets/Arrows/Spirit_arrow.png")
Spirit_Arrow = MyFunctions.pygame_scale_img(Spirit_Arrow, Game_Constants.Arrow_scale)

# Phantom Arrow :
Phantom_Arrow = pygame.image.load("Assets/Arrows/Phantom_arrow.png")
Phantom_Arrow = MyFunctions.pygame_scale_img(Phantom_Arrow, Game_Constants.Arrow_scale)

# -------------------------------------------- SPELLS & PROJECTILES ------------------------------------------------- #

Fireball = pygame.image.load("Assets/Enemy_Projectiles/Fireball.png")
Fireball = MyFunctions.pygame_scale_img(Fireball, Game_Constants.Fireball_Scale)

Bone = pygame.image.load("Assets/Enemy_Projectiles/Bone.png")
Bone = MyFunctions.pygame_scale_img(Bone, Game_Constants.Bone_Scale)
