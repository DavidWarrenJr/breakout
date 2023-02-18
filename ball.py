import pygame.sprite

from globals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        # starting position
        self.rect.x = WIDTH / 2
        self.rect.y = 25

        self.velocity = 1
        self.y_speed = 1 * self.velocity
        self.x_speed = 1 * self.velocity

    def update(self, player, wall):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        # if collision with player
        if self.rect.colliderect(player):
            self.y_speed *= -1

        # if collision with block
        for block in wall:
            # top / bottom collisions
            if block.rect.collidepoint(self.rect.midtop) or block.rect.collidepoint(self.rect.midbottom):
                self.y_speed *= -1
                block.kill()

            # left / right collision
            if block.rect.collidepoint(self.rect.midleft) or \
                    block.rect.collidepoint(self.rect.midright):
                self.x_speed *= -1
                block.kill()

        # if collision with edge of screen
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_speed *= -1

        if self.rect.top < 0:
            self.y_speed *= -1
