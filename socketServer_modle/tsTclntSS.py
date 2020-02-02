from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)
try:
    while True:
        tcpCliSock = socket(AF_INET, SOCK_STREAM)
        tcpCliSock.connect(ADDR)
        # 接收数据
        data = input(">")
        if not data:
            break
        tcpCliSock.send(data.encode("utf-8"))
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.strip())
        tcpCliSock.close()
except EOFError and KeyboardInterrupt as ex:
    raise ex
