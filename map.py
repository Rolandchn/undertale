

from pygame.locals import *



import pygame

pygame.init()

# screen
screen_size = (1080, 1000)
screen_weight, screen_height = screen_size
spawn_point = screen_weight / 2, 700 

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("My Training Camp")

# box and life
box_rect = Rect(20, 20, 500, 200)
box_rect.centerx = screen_weight / 2
box_rect.centery = 700

# texts
text_font = pygame.font.Font(None, 50)
text_surface = text_font.render("Undertale", False, "white")
text_rect = text_surface.get_rect(center = (screen_weight / 2, 200))

# FPS
clock = pygame.time.Clock()

def set_map():    
    screen.fill("black")
    pygame.draw.rect(screen, "white", box_rect, 4)
    screen.blit(text_surface, text_rect)
        