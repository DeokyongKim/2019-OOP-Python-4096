import socket
from _thread import *


#클라이언트의 점수를 저장할 점수판 딕셔너리
score_dict = {}

# 쓰레드에서 실행되는 코드입니다.

# 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다.
def threaded(client_socket, addr):
    print('Connected by :', addr[0], ':', addr[1])

    # 클라이언트가 접속을 끊을 때 까지 반복합니다.
    while True:

        try:

            # 데이터가 수신되면 클라이언트에 다시 전송합니다.(에코)
            data = client_socket.recv(1024)

            data_a = data.decode()
            data_a = data_a.split(',')
            # 수신 받은 클라이언트의 주소와 점수를 기록
            score_dict[data_a[0]] = int(data_a[1])

            # 정렬하기 위해 딕셔너리를 리스트로 변환, 그리고 value기준으로 정렬
            items = list(score_dict.items())
            items.sort(key = lambda element : element[1],reverse=True)
            print(items[0])
            a=items.index(('{}'.format(data_a[0]), score_dict[data_a[0]]))
            if not data:
                print('Disconnected by ' + addr[0], ':', addr[1])
                break

            print('Received from ' + addr[0], ':', addr[1], data_a)
            winner = items[0][0]+','+str(items[0][1])+','+str(a)
            #winner=' '.join(['%d@%d' % (items[0][0], items[0][1])])
            print(winner)
            client_socket.send(winner.encode())

        except ConnectionResetError as e:

            print('Disconnected by ' + addr[0], ':', addr[1])
            break

    client_socket.close()


HOST = '127.0.0.1'
PORT = 9998

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('server start')

# 클라이언트가 접속하면 accept 함수에서 새로운 소켓을 리턴합니다.

# 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다.
while True:
    print('wait')

    client_socket, addr = server_socket.accept()
    start_new_thread(threaded, (client_socket, addr))

server_socket.close()