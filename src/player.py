import pygame
from constants import *
from sprites_management import load_sprite_sheets


class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
        self.fall_count = 0
        self.SPRITES = load_sprite_sheets("character", "test_character", 64, 64, True)
        self.sprite = None

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        # Amount of falling ticks divided by the amount of tick in one second
        # 1 is the minimum to avoid a very slow falling start
        # self.y_vel += min(1, (self.fall_count / fps) * GRAVITY)
        self.move(self.x_vel, self.y_vel)   # Move

        self.fall_count += 1                # Increment the falling ticks each tick
        self.update_sprite()

    def update_sprite(self):
        sprite_sheet = "idle"
        if self.x_vel != 0:
            sprite_sheet = "run"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.animation_count // ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.animation_count += 1
        self.update()

    def update(self):
        # Adapt the rect to the sprite size
        self.rect = self.sprite.get_rect(toplef=(self.rect.x, self.rect.y))

        # Mapping the "hit-box" to the sprite to have pixel perfect collision
        self.mask = pygame.mask.from_surface(self.sprite)

    def draw(self, window):
        window.blit(self.sprite, (self.rect.x, self.rect.y))
