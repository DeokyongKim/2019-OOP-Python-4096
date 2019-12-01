# 참고 : https://snowdeer.github.io/python/2018/09/11/pygame-example/
# 참고 : https://bluese05.tistory.com/5
# 참고 : https://nightshadow.tistory.com/entry/pygame-에서-텍스트-출력
# 참고 : https://stackoverflow.com/questions/27664957/pygame-catching-enter-button
# 참고 : https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
# 참고 : https://m.blog.naver.com/PostView.nhn?blogId=lee95292&logNo=221201880034&proxyReferer=https%3A%2F%2Fwww.google.co.kr%2F


import pygame
import sys


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
        '2048COLOR': (231, 195, 79),
        '4096COLOR': (0, 0, 0)
    }

    def get_color(self, number):
        """
        입력된 숫자에 맞는 색의 RGB 값을 return 하는 함수
        :param number: int
        :return: tuple
        """
        if number == 0:
            return self.color['BACKGROUND BOX COLOR']
        else:
            for i in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
                c = str(i) + 'COLOR'
                if number == i:
                    return self.color[c]
        return self.color['BACKGROUND COLOR']


class GUI_key:
    """
    about: get keyboard input and manage them
    """

    def __init__(self):
        self.alphabet = {pygame.K_a: 'a', pygame.K_b: 'b', pygame.K_c: 'c', pygame.K_d: 'd', pygame.K_e: 'e',
                         pygame.K_f: 'f', pygame.K_g: 'g', pygame.K_h: 'h', pygame.K_i: 'i', pygame.K_j: 'j',
                         pygame.K_k: 'k', pygame.K_l: 'l', pygame.K_m: 'm', pygame.K_n: 'n', pygame.K_o: 'o',
                         pygame.K_p: 'p', pygame.K_q: 'q', pygame.K_r: 'r', pygame.K_s: 's', pygame.K_t: 't',
                         pygame.K_u: 'u', pygame.K_v: 'v', pygame.K_w: 'w', pygame.K_x: 'x', pygame.K_y: 'y',
                         pygame.K_z: 'z'}

        self.number = {pygame.K_0: '0', pygame.K_1: '1', pygame.K_2: '2', pygame.K_3: '3', pygame.K_4: '4',
                       pygame.K_5: '5', pygame.K_6: '6', pygame.K_7: '7', pygame.K_8: '8', pygame.K_9: '9'}
        self.command = {pygame.K_BACKSPACE: 'backspace', pygame.K_RETURN: 'return', pygame.K_SPACE: 'space'}
        self.direction = {pygame.K_UP: 'up', pygame.K_DOWN: 'down', pygame.K_LEFT: 'left', pygame.K_RIGHT: 'right'}
        self.key_l = [self.alphabet, self.number, self.command, self.direction]

    def get_key(self):
        """
        key 를 받는 기본이 되는 함수
        :return: str
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                for l in self.key_l:
                    if event.type == pygame.KEYDOWN:
                        for i in list(l):
                            if event.key == i:
                                return l[i]

    def get_direction_key(self):
        """
        direction 을 판별하는 함수
        :return: str
        """
        while True:
            a = self.get_key()
            if a in ['up', 'down', 'left', 'right']:
                return a

    def get_number_key(self, start, end):
        """
        from start to end
        start ~ end-1 이내의 범위의 수가 들어오면 입력을 넣어주는 함수
        :param start: int
        :param end: int
        :return: int
        """
        while True:
            a = self.get_key()
            if a.isdecimal():
                if start <= int(a) < end:
                    return int(a)

    def get_restart_key(self):
        """
        y 와 n 로 재시작 여부를 받아 bool 로 전달하는 함수
        재시작을 원하면 True, 원하지 않으면 False 가 전달됨
        :return: bool
        """
        while True:
            a = self.get_key()
            if a == 'y':
                return True
            elif a == 'n':
                return False

    def get_alphabet_key(self):
        """
        alphabet 을 받으면 그에 맞는 문자를 return 하는 함수
        :return: str
        """
        while True:
            a = self.get_key()
            if a.isalpha():
                return a


class GUI_management(GUI_key):
    """
    about: manage objects ( boxes ) and screen, all game
    """

    def __init__(self):
        super().__init__()
        self.screen = GUI_screen(5)

    def show_ID_page(self):
        """
        ID 입력을 받는 함수
        13글자 초과의 ID는 입력 도중 입력을 완료함
        backspace 입력시 삭제 가능
        enter 입력시 입력 종료
        :return: str
        """
        ID = []
        x_position = int(self.screen.screen_size * 100 / 5)
        self.screen.screen.fill(color_information.color['BLACK'])
        self.screen.show_text('Type your ID (only Eng)', 40, 'WHITE', int(self.screen.screen_size * 90 / 5),
                              int(self.screen.screen_size * 180 / 5))
        while True:
            b = self.get_key()
            if b != 'return' and len(ID) <= 13:
                if b != 'backspace':
                    ID.append(str(b))
                elif len(ID) > 0:
                    ID.pop()
                self.screen.screen.fill(color_information.color['BLACK'])
                self.screen.show_text('Type your ID (only Eng)', 40, 'WHITE', int(self.screen.screen_size * 90 / 5),
                                      int(self.screen.screen_size * 180 / 5))
                self.screen.show_text(''.join(ID), 35, 'WHITE', x_position,
                                      int(self.screen.screen_size * 270 / 5))

            else:
                return ''.join(ID)

    def show_start_page(self):
        """
        시작 화면을 보여주는 함수. 변의 길이를 입력받음
        :return: int
        """
        self.screen.screen.fill(color_information.color['BLACK'])
        self.screen.show_text('Hello This is 2048', 40, 'WHITE', int(self.screen.screen_size * 90 / 5),
                              int(self.screen.screen_size * 180 / 5))
        self.screen.show_text('Choose number 3~8', 40, 'WHITE', int(self.screen.screen_size * 90 / 5),
                              int(self.screen.screen_size * 270 / 5))
        return self.get_number_key(3, 9)

    def show_end_page(self):
        """
        게임이 끝났을 때의 화면을 보여주는 함수
        또한 게임이 끝나면 재실행 여부를 물어 입력을 받음
        :return: bool
        """
        self.screen.screen.fill(color_information.color['BLACK'])
        self.screen.show_text('Retry?', 40, 'WHITE', 10, 10)
        self.screen.show_text('Press y or n', 40, 'WHITE', 10, 50)
        return self.get_restart_key()

    def show_rank_page(self, player_id, score, game_time):
        """
        server 와의 통신을 통해 자신의 점수를 서버에 올리고 서버의 최고점수를 받아 화면에 출력하는 함수
        server 와 통신이 불가능할 땐 'No internet' 을 표시하고 넘어감
        server 와 연결이 되지 않았을 때는 최고점수가 등록되지 않음
        :param player_id: str
        :param score: int
        :return: None
        """
        self.screen.screen.fill(color_information.color['BLACK'])
        self.screen.show_text('Game ended...', 50, 'WHITE', 10, 10)
        self.screen.show_text('ID: {}'.format(player_id), 40, 'WHITE', 10, 50)
        self.screen.show_text('Score: {}'.format(score), 50, 'WHITE', 10, 90)
        try:
            raise ConnectionError
            # server 통신, 최고점수 받아옴 
            self.screen.show_text('Best Score is', 40, 'WHITE', 10, 130)
            self.screen.show_text('{}'.format("""여기에 최고점수 넣기"""), 50, 'WHITE', 10, 170)
            self.screen.show_text('Press any key', 50, 'WHITE', 10, 210)
            pass

        except ConnectionError:
            self.screen.show_text('No internet', 40, 'WHITE', 10, 130)
            self.screen.show_text('Press any key', 40, 'WHITE', 10, 170)
        finally:
            self.get_key()


class GUI_screen:
    """
    about: display screen.
    """
    pygame.init()

    def __init__(self, screen_size):
        self.screen_size = screen_size
        self.color = 'BACKGROUND COLOR'
        self.screen = pygame.display.set_mode((self.screen_size * 90, self.screen_size * 90 + 100))

    def show_text(self, word, font_size, color, position_x, position_y):
        """
        show text on screen
        원하는 문장을 원하는 위치에 표시함
        :param color: str
        :param font_size: int
        :param word: any type
        :param position_x: int
        :param position_y: int
        :return:
        """
        font = pygame.font.SysFont("notosanscjkkr", font_size)
        textSurfaceObj = font.render(str(word), True, color_information.color[color])
        self.screen.blit(textSurfaceObj, (position_x, position_y))
        pygame.display.flip()

    def show_box(self, board):
        """
        GUI 에 박스를 표현하는 함수
        여기서 박스는 보드 위의 판에 있는 네모 박스를 지칭한다
        :param board: list
        :return: None
        """
        for i in range(self.screen_size):
            for j in range(self.screen_size):
                c_i = color_information()
                box_color = c_i.get_color(board[i][j])
                pygame.draw.rect(self.screen, box_color, (i * 90 + 9, j * 90 + 9, 72, 72))
                if board[i][j] != 0:
                    if board[i][j] < 10:
                        self.show_text(board[i][j], 36, 'WHITE', i * 90 + 36, j * 90 + 36)
                    elif board[i][j] < 100:
                        self.show_text(board[i][j], 36, 'WHITE', i * 90 + 31.5, j * 90 + 36)
                    else:
                        self.show_text(board[i][j], 31, 'WHITE', i * 90 + 22.5, j * 90 + 36)

    def show_score(self, score):
        """
        게임 도중 scree 에 점수를 표시하는 함수
        :param score: int
        :return: None
        """
        self.show_text('Score', 50, 'BLACK', 10, self.screen_size * 90)
        self.show_text(score, 50, 'BLACK', 10, self.screen_size * 90 + 50)

    def show_screen(self, board, score):
        """
        게임 화면을 보여주는 함수
        board 는 이차원 배열이어야 함
        :param board: list
        :param score: int
        :return: None
        """
        self.screen.fill(color_information.color[self.color])
        self.show_box(board)
        self.show_score(score)

        pygame.display.flip()


if __name__ == '__main__':
    # a = GUI_screen(4)
    # a.show_score(5403)

    b = GUI_key()
    print(b.get_key())
