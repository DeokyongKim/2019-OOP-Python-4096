# 참고 : https://snowdeer.github.io/python/2018/09/11/pygame-example/

import pygame
import sys

dir_l = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}


class color_information:
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    PURPLE = (100, 0, 100)


class GUI_box(color_information):
    global dir_l

    def __init__(self, number, size, pos_x, pos_y):
        self.number = number
        self.size = size
        self.position_x = pos_x
        self.position_y = pos_y
        self.color = 'None'
        self.direction = 'None'

    # def get_key(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             sys.exit()
    #
    #         if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
    #             self.direction = 'left'
    #
    #         if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    #             self.direction = 'right'
    #
    #         if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
    #             self.direction = 'up'
    #
    #         if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
    #             self.direction = 'down'

    def find_out_of_range(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        for i in list(dir_l):
            if self.direction == i:
                if self.position_x + dir_l[i][0]*self.size < 0:
                    self.direction = 'None'
                elif self.position_x + dir_l[i][0]*self.size > SCREEN_WIDTH-self.size:
                    self.direction = 'None'
                elif self.position_y + dir_l[i][1]*self.size < 0:
                    self.direction = 'None'
                elif self.position_y + dir_l[i][1]*self.size > SCREEN_HEIGHT-self.size:
                    self.direction = 'None'

    def edit_position(self):
        self.get_key()

        for i in list(dir_l):
            if self.direction == i:
                self.position_x += dir_l[self.direction][0] * self.RECTANGULAR_SIZE
                self.position_y += dir_l[self.direction][1] * self.RECTANGULAR_SIZE

        self.screen.fill(self.PURPLE)
        pygame.draw.rect(self.screen, self.YELLOW, (self.position_x, self.position_y, self.RECTANGULAR_SIZE, self.RECTANGULAR_SIZE))
        pygame.display.flip()


class GUI_board_information:
    def __init__(self, screen_width, screen_height, rectangular_size):
        self.SCREEN_WIDTH = screen_width
        self.SCREEN_HEIGHT = screen_height
        self.RECTANGULAR_SIZE = rectangular_size
        self.DIST = rectangular_size


class GUI_screen(GUI_board_information, color_information):
    def __init__(self, screen_width, screen_height, rectangular_size, position_x, position_y):
        super().__init__(screen_width, screen_height, rectangular_size)
        self.position_x = position_x
        self.position_y = position_y
        self.direction = 'None'

        pygame.init()
        pygame.display.set_caption("Simple PyGame Example")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def edit_position(self):
        self.get_key()

        for i in list(dir_l):
            if self.direction == i:
                self.position_x += dir_l[self.direction][0] * self.RECTANGULAR_SIZE
                self.position_y += dir_l[self.direction][1] * self.RECTANGULAR_SIZE

        self.screen.fill(self.PURPLE)
        pygame.draw.rect(self.screen, self.YELLOW, (self.position_x, self.position_y, self.RECTANGULAR_SIZE, self.RECTANGULAR_SIZE))
        pygame.display.flip()

    def screen_move(self):
        self.get_key()
        self.find_out_of_range()
        if self.direction != 'None':
            self.edit_position()

    def screen_play(self):
        while True:
            self.screen_move()


a = GUI_screen(300, 300, 60, 30, 30)
a.screen_play()

