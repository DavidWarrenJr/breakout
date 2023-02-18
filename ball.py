import pygame.sprite
from pygame.math import Vector2
from globals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((20, 20))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()

        # starting position
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2

        self.velocity = 1
        self.y_speed = 2
        self.x_speed = 2
        self.block_hit_count = 0

    def update(self, player, wall):
        if len(wall) == 0:
            win = pygame.USEREVENT + 1
            win_event = pygame.event.Event(win)
            pygame.event.post(win_event)

        # MOVE
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed

        self.handle_collision(player, wall)

    def handle_collision(self, player, wall):
        # COLLISION WITH PLAYER
        if self.rect.colliderect(player):
            self.y_speed *= -1

            # moving right
            if self.x_speed > 0:
                # if ball lands on left side of paddle reverse x direction
                if self.rect.center[0] < player.rect.center[0]:
                    self.x_speed *= -1
            else:  # moving left
                # if ball lands on right side of paddle reverse x direction
                if self.rect.center[0] > player.rect.center[0]:
                    self.x_speed *= -1

        # COLLISION WITH BLOCK
        for block in wall:
            # TOP / BOTTOM
            if block.rect.collidepoint(self.rect.midtop) or block.rect.collidepoint(self.rect.midbottom):
                self.y_speed *= -1
                block.kill()
                self.block_hit_count += 1

            # LEFT / RIGHT
            if block.rect.collidepoint(self.rect.midleft) or \
                    block.rect.collidepoint(self.rect.midright):
                self.x_speed *= -1
                block.kill()
                self.block_hit_count += 1

        # COLLISION WITH SCREEN EDGE
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_speed *= -1

        if self.rect.top < 0:
            self.y_speed *= -1

        if self.rect.bottom > HEIGHT:
            lose = pygame.USEREVENT + 0
            loss_event = pygame.event.Event(lose)
            pygame.event.post(loss_event)

        if self.block_hit_count > 6:
            if self.y_speed > 0:
                self.y_speed += 1
            else:
                self.y_speed -= 1
            self.block_hit_count = 0
