# Main file to launch the game
import os
import random
import math
import pygame
from player import Player
from block import Block
from constants import *
from keyboard_management import handle_move, handle_keydown_pressing
from sprites_management import get_background, draw, flip


def init():
    pygame.init()  # Init PyGame

    pygame.display.set_caption("A Muggle's Story")  # Set the window title

    window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the window

    main(window)    # Call the main function


def main(win):
    clock = pygame.time.Clock()                             # Init the clock
    background, bg_image = get_background("grey_tile.png")  # Init the background

    block_size = 64

    player = Player(128, 128, 16, 32)

    floor = [Block(i * block_size, HEIGHT - block_size, block_size)
             for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]

    run = True
    while run:
        clock.tick(FPS)  # Clock ticking to limit the FPS (so the game speed)

        for event in pygame.event.get():    # Listen to all events
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                handle_keydown_pressing(player, event.key)

        player.loop(FPS)        # Move the player
        handle_move(player, floor)     # Get the inputs for the movement

        draw(win, background, bg_image, player, floor)  # For each loop iteration, draw the visual aspect

    pygame.quit()   # Quit PyGame if we leave the loop
    quit()          # Quit Python too


if __name__ == "__main__":  # Only launch the main function if this is the executed file
    init()
