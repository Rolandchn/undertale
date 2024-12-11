

from pygame.locals import *

from map import *
from player_sprite import Player
from enemie_sprite import Enemy

import pygame


def get_collision():
    if pygame.sprite.spritecollide(player_sprite.sprite, enemy_sprites, False): player.hp -= 1


# sprite class
player = Player()
player.get_screen(screen)
player_sprite = pygame.sprite.GroupSingle()
player_sprite.add(player)

enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(Enemy("spike"))

## main
game_active = True
running = True
while running:
    set_map()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False

        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            player.change_state()

    if game_active:
        player_sprite.draw(screen)
        player_sprite.update()

        enemy_sprites.draw(screen)

        get_collision()

    clock.tick(60)
    pygame.display.update()

pygame.quit()
