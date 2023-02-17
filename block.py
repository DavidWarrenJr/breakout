import pygame.sprite

from globals import *


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((55, 25))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()

        self.rect.topleft = (x, y)
