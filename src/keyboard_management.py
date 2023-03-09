import pygame
from constants import *


def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0                    # Important to move only when holding a key
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY)