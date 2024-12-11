

from enum import Enum
import pygame



class HeartColor(Enum):
    RED = 0
    BLUE = 1
    YELLOW = 2


class Texture:
    heart_textures = []
    heart_rect = []

    def __init__(self):
        self.load_heart_texture()
        self.load_heart_rect()


    @staticmethod
    def generate_heart_surface():
        for color in HeartColor:
            heart_surface = pygame.image.load(f"img/{color.name.lower()}_heart.png").convert_alpha()
            heart_surface = pygame.transform.rotozoom(heart_surface, 0, 0.8)

            yield heart_surface


    def load_heart_texture(self):
        self.heart_textures = []

        for color in self.generate_heart_surface():
            self.heart_textures.append(color) 


    def load_heart_rect(self):
        self.heart_rect = []

        for image in self.heart_textures:
            self.heart_rect.append(image.get_rect())
