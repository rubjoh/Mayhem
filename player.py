from pygame.math import Vector2
import pygame
import random
from object import Object


class Player(pygame.sprite.Sprite):
    GRAVITY = 1

    def __init__(self, x_pos, y_pos, width, heigth, background, image):
        self.rect = pygame.Rect(x_pos, y_pos, width, heigth)
        self.mask = None
        self.x_vel = 0
        self.y_vel = 0
        self.bg = background
        self.img = image



