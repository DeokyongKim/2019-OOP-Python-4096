
# 참고 : https://snowdeer.github.io/python/2018/09/11/pygame-example/

import pygame
import sys

dir_l = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
box_l = []


class color_information:
    """
    about: color information in RGB
    """
    color = {
        'BLACK': (0, 0, 0),
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255),
        'YELLOW': (255, 255, 0),
        'PURPLE': (100, 0, 100),
    }


class GUI_box:
    """
    about: make box object and save their information
    """
    def __init__(self, number=int, size=int, pos_x=int, pos_y=int, color=str):
        """
        save box's information such as...
        :param number: int
        :param size: int
        :param pos_x: int
        :param pos_y: int
        :param color: str
        """
        self.number = number
        self.size = size
        self.position_x = pos_x
        self.position_y = pos_y
        self.color = color

    def move(self, direction):
        """
        change box's position by keyboard input information
        :param direction: str
        :return: None
        """
        s = self.size
        px = self.position_x
        py = self.position_y
        if direction != 'None':
            for i in list(dir_l):
                if direction == i:
                    self.position_x += dir_l[i][0] * self.size
                    self.position_y += dir_l[i][1] * self.size


class GUI_key:
    """
    about: get keyboard input and manage them
    """
    def __init__(self):
        self.direction = 'None'

    def get_key(self):
        """
        get keyboard input and turn them into str object
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                self.direction = 'left'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                self.direction = 'right'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                self.direction = 'up'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                self.direction = 'down'

    def find_out_of_range(self, size, position_x, position_y):
        """
        get box's size and position and judge the 'direction' command is able to act
        근데 이건 box 객체가 하는 게 맞다. 여기서 이럴 문제가 아님.
        :param size: int
        :param position_x: int
        :param position_y: int
        :return: None
        """
        self.get_key()
        a = GUI_screen(300, 300)
        for i in list(dir_l):
            if self.direction == i:
                if position_x + dir_l[i][0] * size < 0:
                    self.direction = 'None'
                elif position_x + dir_l[i][0] * size > a.screen_size - size:
                    self.direction = 'None'
                elif position_y + dir_l[i][1] * size < 0:
                    self.direction = 'None'
                elif position_y + dir_l[i][1] * size > a.screen_size - size:
                    self.direction = 'None'

    def return_key(self, size, position_x, position_y):
        """

        :param size: int
        :param position_x:
        :param position_y:
        :return: None
        """
        self.get_key()
        # self.find_out_of_range(size, position_x, position_y)
        if self.direction != 'None':
            print(self.direction)
        return self.direction


class GUI_management:
    """
    about: manage objects ( boxes ) and screen, all game
    """
    def add_box(self, number=int, size=int, pos_x=int, pos_y=int):
        global box_l
        a = GUI_box(number, size, pos_x, pos_y, 'YELLOW')
        box_l.append(a)

    def run_game(self):
        global box_l
        self.add_box(2, 60, 30, 30)
        while True:
            a = GUI_screen(300, 'PURPLE')
            # self.add_box(2, 60, 30, 30)
            a.show_screen()


class GUI_screen:
    """
    about: display screen.
    """
    pygame.init()

    def __init__(self, screen_size=int, color=str):
        self.screen_size = screen_size
        self.color = color

    def show_screen(self):
        screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        screen.fill(color_information.color[self.color])
        a = GUI_key()
        b = GUI_box(2, 60, 30, 30)
        direction = a.return_key(b.size, b.position_x, b.position_y)
        for i in box_l:
            pygame.draw.rect(screen, color_information.color[i.color], (i.position_x, i.position_y, i.size, i.size))
            i.move(direction)
        pygame.display.flip()


a = GUI_management()
a.run_game()
