
# 참고 : https://snowdeer.github.io/python/2018/09/11/pygame-example/


import pygame
import sys

dir_l = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}
# box_l = []


class color_information:
    """
    about: color information in RGB
    """
    color = {
        'BLACK': (0, 0, 0),
        'WHITE': (255, 255, 255),
        'BACKGROUND COLOR': (185, 173, 162),
        'BACKGROUND BOX COLOR': (203, 193, 181),
        '8COLOR': (233, 179, 219),
        '16COLOR': (232, 153, 108),
        '2COLOR': (236, 228, 219),
        '4COLOR': (235, 224, 203),
        '64COLOR': (229, 104, 71),
        '128COLOR': (233, 207, 127),
        '256COLOR': (232, 204, 114),
        '512COLOR': (232, 200, 101),
        '1024COLOR': (231, 197, 89),
        '2048COLOR': (231, 195, 79)
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

    # def move(self, direction):
    #     """
    #     change box's position by keyboard input information
    #     얘는 실험용으로 만든거고 실제로 사용되지는 않습니다. 제대로 구현되었나 보는데 썼습니다.
    #     :param direction: str
    #     :return: None
    #     """
    #     s = self.size
    #     px = self.position_x
    #     py = self.position_y
    #     if direction != 'None':
    #         for i in list(dir_l):
    #             if direction == i:
    #                 self.position_x += dir_l[i][0] * self.size
    #                 self.position_y += dir_l[i][1] * self.size


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

    def get_number_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    return 2
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
                    return 3
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
                    return 4
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_5:
                    return 5
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_6:
                    return 6
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_7:
                    return 7
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_8:
                    return 8
                elif event.type == pygame.KEYDOWN:
                    return 0

    # def find_out_of_range(self, size, position_x, position_y):
    #     """
    #     get box's size and position and judge the 'direction' command is able to act
    #     근데 이건 board에서 해결하는 것이 맞다. 여기서 이럴 문제가 아님. 영채 화이팅
    #     :param size: int
    #     :param position_x: int
    #     :param position_y: int
    #     :return: None
    #     """
    #     self.get_key()
    #     a = GUI_screen(300, 300)
    #     for i in list(dir_l):
    #         if self.direction == i:
    #             if position_x + dir_l[i][0] * size < 0:
    #                 self.direction = 'None'
    #             elif position_x + dir_l[i][0] * size > a.screen_size - size:
    #                 self.direction = 'None'
    #             elif position_y + dir_l[i][1] * size < 0:
    #                 self.direction = 'None'
    #             elif position_y + dir_l[i][1] * size > a.screen_size - size:
    #                 self.direction = 'None'

    # def return_key(self, size, position_x, position_y):
    #     """
    #
    #     :param size: int
    #     :param position_x:
    #     :param position_y:
    #     :return: None
    #     """
    #     self.get_key()
    #     # self.find_out_of_range(size, position_x, position_y)
    #     if self.direction != 'None':
    #         print(self.direction)
    #     return self.direction


class GUI_management:
    """
    about: manage objects ( boxes ) and screen, all game
    """
    def __init__(self):
        self.screen = GUI_screen(5)

    # def add_box(self, number=int, size=int, pos_x=int, pos_y=int):
    #     """
    #     이건 board에서 구현할 내용
    #     여기는 실험을 위해 넣어놓았다
    #     :param number: int
    #     :param size: int
    #     :param pos_x: int
    #     :param pos_y: int
    #     :return: None
    #     """
    #     global box_l
    #     a = GUI_box(number, size, pos_x, pos_y, '128COLOR')
    #     box_l.append(a)

    def show_start_page(self):
        tmp = GUI_key()
        while True:
            self.screen.show_text('Choose number 2~8', int(self.screen.screen_size / 3),
                                  int(self.screen.screen_size / 2))
            b = tmp.get_number_key()
            print(b)
            if b != 0:
                return b

    # def run_game(self):
    #     # global box_l
    #     # self.add_box(2, 140, 20, 20)
    #
    #     while True:
    #         # self.add_box(2, 60, 30, 30)
    #         self.screen.show_screen(140, 20, 20)


class GUI_screen:
    """
    about: display screen.
    """
    pygame.init()

    def __init__(self, screen_size=int):
        self.screen_size = screen_size
        self.color = 'BACKGROUND COLOR'
        self.screen = pygame.display.set_mode((self.screen_size*40, self.screen_size*40))

    # 참고 : https://nightshadow.tistory.com/entry/pygame-에서-텍스트-출력
    def show_text(self, word, position_x, position_y):
        """
        show text on screen
        원하는 문장을 원하는 위치에 표시함
        :param word: any type.
        :param position_x: int
        :param position_y: int
        :return:
        """
        font = pygame.font.SysFont("notosanscjkkr", 30)
        textSurfaceObj = font.render(str(word), True, color_information.color['WHITE'])
        self.screen.blit(textSurfaceObj, (position_x, position_y))
        pygame.display.flip()

    def show_screen(self, board):
        self.screen.fill(color_information.color[self.color])

        for i in range(self.screen_size):
            for j in range(self.screen_size):
                box_color = str(board[i][j]) + 'COLOR'
                pygame.draw.rect(self.screen, color_information.color[box_color], (i, j, 20, 20))
                self.show_text(board[i][j], i, j)
        pygame.display.flip()


if __name__ == '__main__':
    a = GUI_management()
    a.show_start_page()
    # a.run_game()
