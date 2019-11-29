"""
import socket
import random
import threading

# 서버의 정보 설정
myip = '127.0.0.1'
myport = 50001
address = (myip, myport)

# 소켓을 활용하여 서버 열기
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen()

print("===== 클라이언트 접속을 대기하는 중입니다.")
client_sock, client_addr = server_sock.accept()
print("===== 클라이언트가 접속하였습니다.")


# 클라이언트가 보내온 메시지를 받아 출력해주는 함수 | Thread로 돌릴 예정
def receive():
    global client_sock
    while True:
        try:
            data = client_sock.recv(1024)
            if data == '':
                break
        except OSError:
            print('연결이 종료되었습니다.')
            break

        print(data.decode('UTF-8'), " *from Client")
    client_sock.close()


# Thread 생성 및 실행
thread_recv = threading.Thread(target=receive, args=())
thread_recv.start()

# 메시지 전송 및 판단 client_sock 처리
while True:
    try:
        data = input('>')
    except KeyboardInterrupt:
        break
    if data == '!quit' or '':
        client_sock.close()
        break
    client_sock.send(bytes(data, 'UTF-8'))

# 서버 종료
server_sock.close()
"""
import socket


# 접속할 서버 주소입니다. 여기에서는 루프백(loopback) 인터페이스 주소 즉 localhost를 사용합니다.
HOST = '127.0.0.1'

# 클라이언트 접속을 대기하는 포트 번호입니다.
PORT = 9999



# 소켓 객체를 생성합니다.
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# 포트 사용중이라 연결할 수 없다는
# WinError 10048 에러 해결를 위해 필요합니다.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


# bind 함수는 소켓을 특정 네트워크 인터페이스와 포트 번호에 연결하는데 사용됩니다.
# HOST는 hostname, ip address, 빈 문자열 ""이 될 수 있습니다.
# 빈 문자열이면 모든 네트워크 인터페이스로부터의 접속을 허용합니다.
# PORT는 1-65535 사이의 숫자를 사용할 수 있습니다.
server_socket.bind((HOST, PORT))

# 서버가 클라이언트의 접속을 허용하도록 합니다.
server_socket.listen()

# accept 함수에서 대기하다가 클라이언트가 접속하면 새로운 소켓을 리턴합니다.
client_socket, addr = server_socket.accept()

# 접속한 클라이언트의 주소입니다.
print('Connected by', addr)

#클라이언트들이 기록한 점수를 나타낼 공간

#점수판 딕셔너리를 리스트로 바꾼 값을 value기준으로 정렬하는 함수
def sortSecond(val):
   return val[1]

#클라이언트의 점수를 저장할 점수판 딕셔너리
socre_dict = {}


# 무한루프를 돌면서
while True:

    # 클라이언트가 보낸 메시지를 수신하기 위해 대기합니다.
    data = client_socket.recv(1024)

    # 빈 문자열을 수신하면 루프를 중지합니다.
    if not data:
        break


    # 수신받은 문자열을 출력합니다.
    print('Received from', addr, data.decode())

    #수신 받은 클라이언트의 주소와 점수를 기록
    socre_dict[addr] = data

    #정렬하기 위해 딕셔너리를 리스트로 변환, 그리고 value기준으로 정렬
    items = list(score_dict.items())
    items.sort(key=sortSecond, reverse=True)


    # 리스트를 다시 클라이언트로 전송해줍니다.
    client_socket.sendall(items)


# 소켓을 닫습니다.
client_socket.close()
server_socket.close()