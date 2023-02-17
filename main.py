import pygame, sys
from pygame.locals import *

pygame.init()

WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
BLUE = pygame.Color(0, 0, 255)

SCREEN = pygame.display.set_mode((800, 600))
SCREEN.fill(WHITE)
pygame.display.set_caption("Breakout")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
