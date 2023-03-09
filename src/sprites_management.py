import pygame
from constants import *
from os.path import join


def get_background(name):  # Return the background
    image = pygame.image.load(join("..\\assets", "terrain", name))  # Retrieve the image file
    _, _, width, height = image.get_rect()                          # Retrieve the image size

    # Temp : to reduce the background tiles size (but this is temp background)  #

    ratio = 4                                                                   #
    image = pygame.transform.scale(image, (width/ratio, height/ratio))          #
    _, _, width, height = image.get_rect()                                      #

    # End of temp bloc ------------------------------------------------------   #

    tiles = []  # The background (list of tiles positions)

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i*width, j*height)   # Get the top left corner of the tile
            tiles.append(pos)           # Add the position to the list of tiles positions

    return tiles, image


def draw(window, background, bg_image, player):  # Draw the visual aspect on the window
    for tile in background:
        window.blit(bg_image, tile)  # Draw each tile for the background

    player.draw(window)

    pygame.display.update()  # Update the screen
