# 참고 : https://pydole.tistory.com/entry/Python-%EC%9E%90%EC%8B%A0%EC%9D%98-%EB%A1%9C%EC%BB%AC-IP-%EC%95%8C%EC%95%84%EB%82%B4%EA%B8%B0

import socket


def check(self):
    return socket.gethostbyname(socket.getfqdn())
