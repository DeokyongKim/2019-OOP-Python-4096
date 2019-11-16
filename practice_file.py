import pygame
import sys

dir_l = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
box_l = []


class color_information:
    color = {
        'BLACK': (0, 0, 0),
        'RED': (255, 0, 0),
        'GREEN': (0, 255, 0),
        'BLUE': (0, 0, 255),
        'YELLOW': (255, 255, 0),
        'PURPLE': (100, 0, 100),
    }


class GUI_box:
    def __init__(self, number=int, size=int, pos_x=int, pos_y=int, color=str):
        self.number = number
        self.size = size
        self.position_x = pos_x
        self.position_y = pos_y
        self.color = color

    def move(self):
        s = self.size
        px = self.position_x
        py = self.position_y
        direction = GUI_key.return_key(s, px, py)
        if direction != 'None':
            for i in list(dir_l):
                if direction == i:
                    self.position_x += dir_l[i][0] * self.size
                    self.position_y += dir_l[i][1] * self.size


class GUI_key:
    direction = 'None'

    def get_key(self):
        global direction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                direction = 'left'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                direction = 'right'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                direction = 'up'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                direction = 'down'

    def find_out_of_range(self, size, position_x, position_y):
        global direction
        for i in list(dir_l):
            if direction == i:
                if position_x + dir_l[i][0] * size < 0:
                    direction = 'None'
                elif position_x + dir_l[i][0] * size > GUI_screen.__init__.screen_size - size:
                    direction = 'None'
                elif position_y + dir_l[i][1] * size < 0:
                    direction = 'None'
                elif position_y + dir_l[i][1] * size > GUI_screen.__init__.screen_size - size:
                    direction = 'None'

    def return_key(self, size, position_x, position_y):
        global direction
        self.get_key()
        self.find_out_of_range(size, position_x, position_y)
        print(direction)
        return direction


class GUI_management:
    def add_box(self, number=int, size=int, pos_x=int, pos_y=int):
        global box_l
        a = GUI_box(number, size, pos_x, pos_y, 'YELLOW')
        box_l.append(a)

    def run_game(self):
        global box_l
        while True:
            a = GUI_screen(300, 'PURPLE')
            self.add_box(2, 60, 30, 30)
            a.show_screen()

            for i in box_l:
                i.move()


class GUI_screen:
    pygame.init()

    def __init__(self, screen_size=int, color=str):
        self.screen_size = screen_size
        self.color = color

    def show_screen(self):
        screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        screen.fill(color_information.color[self.color])
        for i in box_l:
            pygame.draw.rect(screen, color_information.color[i.color], (i.position_x, i.position_y, i.size, i.size))
        pygame.display.flip()


a = GUI_management()
a.run_game()
