# 참고 : https://snowdeer.github.io/python/2018/09/11/pygame-example/

import pygame
import sys

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
SIZE_RECT = 50
DIST = 50

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (100, 0, 100)

pygame.init()
pygame.display.set_caption("Simple PyGame Example")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pos_x = 200
pos_y = 200

clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    key_event = pygame.key.get_pressed()
    if key_event[pygame.K_LEFT]:
        pos_x -= DIST

    if key_event[pygame.K_RIGHT]:
        pos_x += DIST

    if key_event[pygame.K_UP]:
        pos_y -= DIST

    if key_event[pygame.K_DOWN]:
        pos_y += DIST

    screen.fill(PURPLE)
    pygame.draw.rect(screen, YELLOW, (pos_x, pos_y, SIZE_RECT, SIZE_RECT))
    pygame.display.update()
