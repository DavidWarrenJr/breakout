import pygame
import sys
from pygame.locals import *
from globals import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
frames_per_second = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


while True:
    frames_per_second.tick(FPS)

    # input / events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # UPDATE
    all_sprites.update()

    # DRAW
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.update()

