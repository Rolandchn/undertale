

import pygame

from map import *
from texture import Texture, HeartColor



class HeathBar:
    def __init__(self, max_hp):
        self.x = 20
        self.y = 20
        self.w = 200
        self.h = 18
        self.hp = max_hp
        self.max_hp = max_hp


    def update(self):
        self.bar_rect = Rect(self.x, self.y, self.w, self.h)
        self.ratio = self.hp / self.max_hp
        
        hp_font = pygame.font.Font(None, 30)
        self.hp_surface = hp_font.render(f"{self.hp}/{self.max_hp}", False, "white")
        self.hp_rect = self.hp_surface.get_rect(topleft = self.bar_rect.topright)
        

    def get_hp(self, hp):
        self.hp = hp


    def draw(self, screen):
        self.update()

        screen.blit(self.hp_surface, self.hp_rect)

        pygame.draw.rect(screen, "red", self.bar_rect)
        pygame.draw.rect(screen, "green", (self.bar_rect.x, self.bar_rect.
        x, self.bar_rect.w * self.ratio, self.bar_rect.x))
        


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.TEXTURE = Texture()
        self.State = HeartColor.BLUE

        # texture 
        self.image = self.TEXTURE.heart_textures[self.State.value]
        self.rect = self.TEXTURE.heart_rect[self.State.value]
        self.rect.center = spawn_point

        self.max_hp = 100
        self.hp = self.max_hp

        # blue heart
        self.gravity = 0
        self.falling = True
        self.min_fall_acceleration = 0.5
        self.max_acceleration = 5.5
        self.jump_acceleration = self.max_acceleration
        self.falling_acceleration = self.max_acceleration - 1

        self.list_pos = []


    def get_screen(self, screen):
        self.screen = screen


    def set_heartbar(self):
        heart_bar = HeathBar(self.max_hp)
        heart_bar.get_hp(self.hp)
        heart_bar.draw(self.screen)


    def change_state(self):
        if self.State == HeartColor.BLUE: 
            self.State = HeartColor.RED

        elif self.State == HeartColor.RED: 
            self.State = HeartColor.BLUE
            self.reset_gravity(); self.falling = True
        
        self.image = self.TEXTURE.heart_textures[self.State.value]


    def blue_heart(self):
        self.blue_heart_mouvement()
        self.apply_gravity()

    def red_heart(self):
        self.red_heart_mouvement()

    # blue
    def blue_heart_mouvement(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.rect.x -= 3
        
        if keys[K_RIGHT]:
            self.rect.x += 3
        
        if keys[K_UP] and not self.falling:
            self.falling_acceleration = self.min_fall_acceleration

            if 0 <= self.jump_acceleration:
                self.jump_acceleration -= 0.15
                self.rect.y -= self.jump_acceleration

            else:
                self.falling = True

        else:
            self.falling = True
                
    # blue
    def reset_gravity(self):
        self.falling = False
        self.jump_acceleration = self.max_acceleration
        self.falling_acceleration = self.max_acceleration - 1

    # blue
    def apply_gravity(self):
        if self.falling:
            if self.jump_acceleration < self.max_acceleration:
                self.falling_acceleration += 0.15
                self.rect.y += self.falling_acceleration

            else:
                self.falling_acceleration = self.max_acceleration - 1
                self.rect.y += self.falling_acceleration

        if self.rect.bottom >= box_rect.bottom - 4:
            self.reset_gravity()

    # red
    def red_heart_mouvement(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            self.rect.x -= 3
        
        if keys[K_RIGHT]:
            self.rect.x += 3
        
        if keys[K_UP]:
            self.rect.y -= 3

        if keys[K_DOWN]:
            self.rect.y += 3


    def collision_map(self):
        if self.rect.bottom >= box_rect.bottom - 4:
            self.rect.bottom = box_rect.bottom - 5

        if self.rect.left <= box_rect.left + 4:
            self.rect.left = box_rect.left + 4

        if self.rect.right >= box_rect.right - 4:
            self.rect.right = box_rect.right - 4

        if self.rect.top <= box_rect.top + 4:
            self.rect.top = box_rect.top + 4
    

    def MouvementTracking(self):
        pointx, pointy = self.rect.centerx, self.rect.centery
        self.list_pos.append((pointx, pointy))

        pressed = pygame.key.get_pressed()

        if pressed[K_ESCAPE]:
            self.list_pos = []

        if len(self.list_pos) >= 2:
            pygame.draw.lines(self.screen, "white", False, self.list_pos)
        pygame.draw.rect(self.screen, "green", self.rect, 1)


    def respawn(self):  
        self.hp = self.max_hp
        self.rect.center = spawn_point
        self.falling = True

    def update(self):
        self.set_heartbar()

        """ self.MouvementTracking() """
        if self.State == HeartColor.BLUE:
            self.blue_heart()

        elif self.State == HeartColor.RED:
            self.red_heart()
        
        self.collision_map()

        if self.hp <= 0:    
            self.respawn()
