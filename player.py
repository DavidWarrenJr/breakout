import pygame.sprite
from globals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([120, 15])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2 + 10
        self.rect.y = HEIGHT / 2 + 100

    def update(self):
        self.move()

    def move(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LEFT]:
            if not self.rect.left < 0:
                self.rect.x -= 5

        if keys_pressed[pygame.K_RIGHT]:
            if not self.rect.right > WIDTH:
                self.rect.x += 5
