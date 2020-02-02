"""
时间戳服务器
"""
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

# 实例化sock对象
tcpServerSock = socket(AF_INET, SOCK_STREAM)
# 绑定地址
tcpServerSock.bind(ADDR)
# 设置最大监听数
tcpServerSock.listen(5)

while True:
    print("waiting for connection.....")
    # 接收连接信息
    tcpCliSock, addr = tcpServerSock.accept()
    print("...connected from:", addr)

    while True:
        # 接收TCP消息
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        # 编码信息
        message = '[{0}]{1}'.format(ctime(), data.decode('utf-8')).encode('utf-8')
        tcpCliSock.send(message)
    tcpCliSock.close()
tcpServerSock.close()
