import pygame
from constants import *
from collision_management import handle_vertical_collision


def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    player.x_vel = 0                    # Important to move only when holding a key
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY)
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    handle_vertical_collision(player, objects, player.y_vel)


def handle_keydown_pressing(player, key):
    if key == pygame.K_SPACE and player.jump_count < 2:
        player.jump()
