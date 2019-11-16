import pygame
import sys

dir_l = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
box_l = []


class color_information:
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (100, 0, 100)


class GUI_box:
    def __init__(self, number, size, pos_x, pos_y):
        self.number = number
        self.size = size
        self.position_x = pos_x
        self.position_y = pos_y

    def move(self, direction):
        if direction != 'None':
            for i in list(dir_l):
                if direction == i:
                    self.position_x += dir_l[i] * self.size
                    self.position_y += dir_l[i] * self.size


class GUI_screen:
    pygame.init()

    def __init__(self, screen_size, color):
        self.screen_size = screen_size
        self.color = color
