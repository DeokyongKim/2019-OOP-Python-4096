import socket


class Client:
    def __init__(self):
        ######## 여기를 수정하세요!############
        self.HOST = '127.0.0.1'
        ##################################
        self.PORT = 9998

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.connect((self.HOST, self.PORT))

    # 키보드로 입력한 문자열을 서버로 전송하고

    # 서버에서 에코되어 돌아오는 메시지를 받으면 화면에 출력합니다.

    # quit를 입력할 때 까지 반복합니다.

    def client_message(self, message):
        self.client_socket.send(message.encode())
        data = self.client_socket.recv(1024)

        print('Received from the server :', repr(data.decode()))
        data = data.decode()
        self.client_socket.close()

        data = data.split(',')
        return data

