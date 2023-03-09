# Main file to launch the game
import os
import random
import math
import pygame
from player import Player
from constants import *
from keyboard_management import handle_move
from sprites_management import get_background, draw

from os import listdir


def init():
    pygame.init()  # Init PyGame

    pygame.display.set_caption("A Muggle's Story")  # Set the window title

    window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the window

    main(window)    # Call the main function


def main(win):
    clock = pygame.time.Clock()                             # Init the clock
    background, bg_image = get_background("grey_tile.png")  # Init the background

    player = Player(128, 128, 16, 32)

    run = True
    while run:
        clock.tick(FPS)  # Clock ticking to limit the FPS (so the game speed)

        for event in pygame.event.get():    # Listen to all events
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)        # Move the player
        handle_move(player)     # Get the inputs for the movement

        draw(win, background, bg_image, player)  # For each loop iteration, draw the visual aspect

    pygame.quit()   # Quit PyGame if we leave the loop
    quit()          # Quit Python too


if __name__ == "__main__":  # Only launch the main function if this is the executed file
    init()
