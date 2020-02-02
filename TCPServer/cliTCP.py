"""
时间戳客户端
"""
from socket import *

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# 实例化sock对象
tcpCliSock = socket(AF_INET, SOCK_STREAM)
# 连接服务器
tcpCliSock.connect(ADDR)

while True:
    data = input('>')
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8'))
    data_recv = tcpCliSock.recv(BUFSIZ)
    print(data_recv.decode('utf-8'))
