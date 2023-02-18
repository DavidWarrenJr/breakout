import pygame
import sys
import time
from pygame.locals import *
from globals import *
from player import Player
from block import Block
from ball import Ball

# TODO create blocks with random length
# TODO learn trigonometry for ball physics

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
frames_per_second = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

ball = Ball()
all_sprites.add(ball)

wall = pygame.sprite.Group()


def create_wall():
    block_start = -10
    row_height = 75
    for row in range(5):
        # create row
        while block_start < WIDTH:
            block = Block(block_start, row_height)
            block_start = block.rect.right + 5

            all_sprites.add(block)
            wall.add(block)

        row_height += block.rect.height + 5
        block_start = -10


create_wall()

WIN = pygame.USEREVENT + 1
won = False
LOSE = pygame.USEREVENT + 0
running = True
while running:
    frames_per_second.tick(FPS)

    # input / events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == LOSE:
            running = False
        if event.type == WIN:
            won = True
            running = False

    # UPDATE
    player.update()
    ball.update(player, wall)

    # DRAW
    screen.fill(WHITE)  # CLEAR SCREEN
    if running:
        all_sprites.draw(screen)
    else:
        if not won:
            screen.fill(RED)
        else:
            screen.fill(GREEN)
        pygame.display.update()
        time.sleep(2)

    pygame.display.update()
