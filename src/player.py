import pygame
from constants import *


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
        self.y_vel += min(1, (self.fall_count / FPS) * GRAVITY)
        self.move(self.x_vel, self.y_vel)   # Move

        self.fall_count += 1                # Increment the falling ticks each tick

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)
