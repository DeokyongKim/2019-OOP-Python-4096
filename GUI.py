
# 참고 : https://snowdeer.github.io/python/2018/09/11/pygame-example/
# 참고 : https://bluese05.tistory.com/5
# 참고 : https://nightshadow.tistory.com/entry/pygame-에서-텍스트-출력

import pygame
import sys

dir_l = {'left': (-1, 0), 'right': (1, 0), 'up': (0, -1), 'down': (0, 1)}


class color_information:
    """
    about: color information in RGB
    """
    color = {
        'BLACK': (0, 0, 0),
        'WHITE': (255, 255, 255),
        'BACKGROUND COLOR': (185, 173, 162),
        'BACKGROUND BOX COLOR': (203, 193, 181),
        '2COLOR': (236, 228, 219),
        '4COLOR': (235, 224, 203),
        '8COLOR': (233, 179, 219),
        '16COLOR': (232, 153, 108),
        '32COLOR': (231, 130, 103),
        '64COLOR': (229, 104, 71),
        '128COLOR': (233, 207, 127),
        '256COLOR': (232, 204, 114),
        '512COLOR': (232, 200, 101),
        '1024COLOR': (231, 197, 89),
        '2048COLOR': (231, 195, 79)
    }

    def return_color(self, number):
        if number == 0:
            return self.color['BACKGROUND BOX COLOR']
        else:
            for i in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
                c = str(i) + 'COLOR'
                if number == i:
                    return self.color[c]
        return self.color['BACKGROUND COLOR']


class GUI_key:
    """
    about: get keyboard input and manage them
    """

    def get_key(self):
        """
        get keyboard input about direction and turn them into str object
        :return: None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                return 'left'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                return 'right'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                return 'up'

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                return 'down'

    def get_number_key(self):
        """
        get keyboard input about numbers
        :return: int, number chosen by keyboard
        """
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

    def get_restart_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                    return True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                    return False

    def get_alphabet_key(self):
        alphabet_l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        alphabet_key_l = [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f,
                          pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l,
                          pygame.K_m, pygame.K_n, pygame.K_o, pygame.K_p, pygame.K_q, pygame.K_r,
                          pygame.K_s, pygame.K_t, pygame.K_u, pygame.K_v, pygame.K_w, pygame.K_x,
                          pygame.K_y, pygame.K_z]
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    for i in alphabet_key_l:
                         if event.key == i:
                            index = alphabet_key_l.index(i)
                            return alphabet_l[index]
                    if event.key == pygame.K_KP_ENTER:
                        return 'ENTER'


class GUI_management(GUI_key):
    """
    about: manage objects ( boxes ) and screen, all game
    """
    def __init__(self):
        super().__init__()
        self.screen = GUI_screen(5)

    def show_ID_page(self):
        ID = []
        ID_string = ''
        x_position = int(self.screen.screen_size * 100 / 4)
        self.screen.show_text('Type your ID', 40, 'WHITE', int(self.screen.screen_size * 100 / 4),
                              int(self.screen.screen_size * 200 / 5))
        while True:
            b = self.get_alphabet_key()
            if b != 'ENTER':
                ID.append(b)
                ID_string = ''.join(ID)
                self.screen.show_text(ID_string, 40, 'WHITE', x_position,
                                      int(self.screen.screen_size * 300 / 5))
                x_position += 10
            else:
                return ID_string

    def show_start_page(self):
        self.screen.show_text('Hello This is 2048', 40, 'WHITE', int(self.screen.screen_size * 100 / 4),
                              int(self.screen.screen_size * 200 / 5))
        self.screen.show_text('Choose number 2~8', 40, 'WHITE', int(self.screen.screen_size * 100 / 4),
                              int(self.screen.screen_size * 300 / 5))
        while True:
            b = self.get_number_key()
            print(b)
            if b != 0:
                return b

    def show_end_page(self):
        self.screen.show_text('Game ended...', 40, 'BLACK', int(self.screen.screen_size * 200 / 5),
                              int(self.screen.screen_size * 200 / 5))
        self.screen.show_text('Good luck Next time', 40, 'BLACK', int(self.screen.screen_size * 100 / 4),
                              int(self.screen.screen_size * 300 / 5))
        while True:
            b = self.get_restart_key()
            return b


class GUI_screen:
    """
    about: display screen.
    """
    pygame.init()

    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.color = 'BACKGROUND COLOR'
        self.screen = pygame.display.set_mode((self.screen_size*100, self.screen_size*100))

    def show_text(self, word, font_size, color, position_x, position_y):
        """
        show text on screen
        원하는 문장을 원하는 위치에 표시함
        :param word: any type.
        :param position_x: int
        :param position_y: int
        :return:
        """
        font = pygame.font.SysFont("notosanscjkkr", font_size)
        textSurfaceObj = font.render(str(word), True, color_information.color[color ])
        self.screen.blit(textSurfaceObj, (position_x, position_y))
        pygame.display.flip()

    def show_screen(self, board):
        self.screen.fill(color_information.color[self.color])

        for i in range(self.screen_size):
            for j in range(self.screen_size):
                c_i = color_information()
                box_color = c_i.return_color(board[i][j])
                pygame.draw.rect(self.screen, box_color, (i * 100 + 10, j * 100 + 10, 80, 80))
                if board[i][j] != 0:
                    if board[i][j] < 10:
                        self.show_text(board[i][j], 40, 'WHITE', i * 100 + 40, j * 100 + 40)
                    elif board[i][j] < 100:
                        self.show_text(board[i][j], 40, 'WHITE', i * 100 + 35, j * 100 + 40)
                    else:
                        self.show_text(board[i][j], 35, 'WHITE', i * 100 + 25, j * 100 + 40)
        pygame.display.flip()


if __name__ == '__main__':
    # a = GUI_management()
    # a.show_start_page()
    # a.run_game()
    b = str(2) + 'COLOR'
    print(b)
