from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)
try:
    while True:
        data = input(">")
        if not data:
            break
        udpCliSock.sendto(data.encode('utf-8'), ADDR)
        data, ADDR = udpCliSock.recvfrom(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
    udpCliSock.close()
except EOFError and KeyboardInterrupt as ex:
    raise ex
