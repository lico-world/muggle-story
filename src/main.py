# Main file to launch the game
import os
import random
import math
import pygame
from player import Player

from os import listdir
from os.path import isfile, join

pygame.init()  # Init PyGame

pygame.display.set_caption("A Muggle's Story")  # Set the window title

# Utility constants
WIDTH, HEIGHT = 800, 550
FPS = 60

# Game constants
PLAYER_VELOCITY = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the window


def get_background(name):  # Return the background
    image = pygame.image.load(join("..\\assets", "terrain", name))  # Retrieve the image file
    _, _, width, height = image.get_rect()                          # Retrieve the image size

    # Temp : to reduce the background tiles size (but this is temp background)  #
                                                                                #
    ratio = 4                                                                   #
    image = pygame.transform.scale(image, (width/ratio, height/ratio))          #
    _, _, width, height = image.get_rect()                                      #
                                                                                #
    # End of temp bloc ------------------------------------------------------   #

    tiles = []  # The background (list of tiles positions)

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i*width, j*height)   # Get the top left corner of the tile
            tiles.append(pos)           # Add the position to the list of tiles positions

    return tiles, image


def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0                    # Important to move only when holding a key
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VELOCITY)


def draw(window, background, bg_image, player):  # Draw the visual aspect on the window
    for tile in background:
        window.blit(bg_image, tile)  # Draw each tile for the background

    player.draw(window)

    pygame.display.update()  # Update the screen


def main(window):
    clock = pygame.time.Clock()                             # Init the clock
    backgroung, bg_image = get_background("grey_tile.png")  # Init the background

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

        draw(window, backgroung, bg_image, player)  # For each loop iteration, draw the visual aspect

    pygame.quit()   # Quit PyGame if we leave the loop
    quit()          # Quit Python too


if __name__ == "__main__":  # Only launch the main function if this is the executed file
    main(window)
