import pygame
from constants import *
from os.path import join, isfile
from os import listdir


def get_background(name):  # Return the background
    image = pygame.image.load(join(ASSETS, "terrain", name))  # Retrieve the image file
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


def draw(window, background, bg_image, player, objects):  # Draw the visual aspect on the window
    for tile in background:
        window.blit(bg_image, tile)  # Draw each tile for the background

    for obj in objects:
        obj.draw(window)

    player.draw(window)

    pygame.display.update()  # Update the screen


def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(path, width, height, direction=False):
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}

    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:   # If you want multi-directional animation
            all_sprites[image.replace(".png", "") + "_right"] = sprites         # Then both are saved
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)    # in the dictionary
        else:
            all_sprites[image.replace(".png", "")] = sprites

    return all_sprites


def load_block(size):
    path = join(ASSETS, "terrain", "crate.png")
    image = pygame.image.load(path).convert_alpha()
    surface = pygame.Surface((size, size), pygame.SRCALPHA, 32)
    rect = pygame.Rect(0, 0, size, size)
    surface.blit(image, (0, 0), rect)
    return surface
