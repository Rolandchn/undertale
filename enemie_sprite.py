
from enum import Enum
import pygame

from map import *


class Enemy_icon(Enum):
    SPIKE = 0


class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemy_name):
        super().__init__()
        self.enemy = enemy_name

        self.load_enemie_texture()


    def load_enemie_texture(self):
        self.image = pygame.image.load(f"img/{self.enemy}.png").convert_alpha()
        self.rect = self.image.get_rect(bottomleft = (700, box_rect.bottom - 4))