import random
from GUI import GUI_management
from GUI import GUI_key
from GUI import GUI_screen

class box:#박스 객체 선언

    def __init__(self, num, locate, color):
        self.num = num
        self.locate = locate
        self.color = color
        self.y = (locate-1)//s
        self.x = (locate-1)%s
        board[self.y][self.x] = self.num

    def move_up(self):#위로 이동
        while True:#이동 못할 때 까지 반복
            if board[self.y-1][self.x]==board[self.y][self.x] and self.y>0:#위에 칸이 있고 값이 같으면 병합
                board[self.y][self.x]=0
                board[self.y-1][self.x] = 2 * self.num
                for l in boxes:#기존의 박스 제거
                    if l.locate == self.locate-s:
                        boxes.remove(l)
                        break
                self.y = self.y - 1
                self.locate = self.locate - s
                self.num = 2 * self.num

            elif board[self.y-1][self.x]==0 and self.y>0: #위에 칸이 있고 비어있으면 위로 이동
                board[self.y][self.x]=0
                board[self.y-1][self.x]=self.num
                self.y = self.y - 1
                self.locate = self.locate - s
            else:
                break

    def move_down(self):#아래로 이동
        while True:#이동 못할 때 까지 반복
            if self.y < s-1 and board[self.y+1][self.x]==board[self.y][self.x]:#위에 칸이 있고 값이 같으면 병합
                board[self.y][self.x]=0
                board[self.y+1][self.x] = 2 * self.num
                for l in boxes:
                    if l.locate == self.locate+s:#기존의 박스 제거
                        boxes.remove(l)
                        break
                self.y = self.y + 1
                self.locate = self.locate + s
                self.num = 2 * self.num

            elif self.y < s-1 and board[self.y+1][self.x]==0:#아래에 칸이 있고 비어있으면 아래로 이동
                board[self.y][self.x]=0
                board[self.y+1][self.x]=self.num
                self.y = self.y + 1
                self.locate = self.locate + s
            else:
                break

    def move_right(self):#오른쪽으로 이동
        while True:#이동 못할 때 까지 반복
            if self.x < s-1 and board[self.y][self.x+1]==board[self.y][self.x]:#오른쪽에 칸이 있고 값이 같으면 병합
                board[self.y][self.x]=0
                board[self.y][self.x+1] = 2 * self.num
                for l in boxes:#기존의 박스 제거
                    if l.locate == self.locate+1:
                        boxes.remove(l)
                        break
                self.x = self.x + 1
                self.locate = self.locate + 1
                self.num = 2 * self.num

            elif self.x < s-1 and board[self.y][self.x+1]==0:#오른쪽에 칸이 있고 비어있으면 오른쪽으로 이동
                board[self.y][self.x]=0
                board[self.y][self.x+1]=self.num
                self.x = self.x + 1
                self.locate = self.locate + 1
            else:
                break

    def move_left(self):#왼쪽으로 이동
        while True:#이동 못할 때 까지 반복
            if board[self.y][self.x-1]==board[self.y][self.x] and self.x > 0:#왼쪽에 칸이 있고 비어있으면 왼쪽으로 이동
                board[self.y][self.x]=0
                board[self.y][self.x-1]= 2 * self.num
                for l in boxes:#기존의 박스 제거
                    if l.locate == self.locate-1:
                        boxes.remove(l)
                        break
                self.x = self.x - 1
                self.locate = self.locate - 1
                self.num = 2 * self.num

            elif board[self.y][self.x-1]==0 and self.x > 0:#왼쪽에 칸이 있고 비어있으면 왼쪽으로 이동
                board[self.y][self.x]=0
                board[self.y][self.x-1]=self.num
                self.x = self.x - 1
                self.locate = self.locate - 1
            else:
                break

def is_range_in(player_s):#변의 길이가 2~8까지의 숫자인지를 판별
    for i in ['2', '3', '4', '5', '6', '7', '8']:
        if player_s == i:
            return True
    return False

def gen_box_locate(): #비어있는 곳을 찾고 그 곳중 랜덤한 위치 선정함
    location = []
    for i in range(s):
        for j in range(s):
            if board[i][j]==0:
                location.append(s*i+j+1)
    return location

def player_move():
    # 플레이어의 상자 움직이기
    while True:
        # 플레이어의 상자 움직이는 방향 입력받음
        print('direction?')
        player_move = GUI_key.get_key()

        if player_move == 'up':
            # 위로 움직이는 경우
            for i in range(s):
                for j in range(s):
                    if board[i][j] is not 0:
                        # 박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:
                                # 모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_up()
                                # 박스를 위로 이동

        if player_move == 'down':
            # 아래로 움직이는 경우
            for i in range(s-1, -1, -1):
                for j in range(s):
                    if board[i][j] is not 0:
                        # 박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:
                                # 모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_down()
                                # 박스를 아래로 이동

        if player_move == 'right':#오른쪽으로 움직이는 경우
            for i in range(s):
                for j in range(s-1, -1, -1):
                    if board[i][j]!=0:#박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:#모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_right()#박스를 오른쪽으로 이동

        if player_move == 'left':#왼쪽으로 움직이는 경우
            for i in range(s):
                for j in range(s):
                    if board[i][j]!=0:#박스가 있는 칸 조사
                        for k in boxes:
                            if k.locate == s*i+j+1:#모든 박스 중에서 위치가 동일한 박스 조사
                                k.move_left()#박스를 왼쪽으로 이동

        if player_move in ['up', 'down', 'right', 'left']:#방향을 틀리게 입력하면 재입력
            break


while True:
    tmp = GUI_management()
    while True:
        # 변 길이 입력받기
        print("한 변의 크기를 입력해 주세요 (2~8):")
        s = tmp.show_start_page()
        if s != 0:
            break

    board = []

    for _ in range(s):
        # 게임보드 형성
        board.append([0] * s)
        # board의 모든 수 0으로 선언(0이 비고 1이 참)

    boxes = []

    screen = GUI_screen(s)
    while True:
        # 상자 생성 - 상자 움직이기 실행
        boxes.append(box(random.choice([2, 4]), random.choice(gen_box_locate()), 'White'))  # 상자 랜덤한 위치에 생성
        for i in range(s):
            for j in range(s):
                print("%d " % board[i][j], end='')
            print()
        screen.show_screen(boxes)
        player_move()
        # 방향 입력 받아 움직이기


