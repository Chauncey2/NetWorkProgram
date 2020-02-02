from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSocket = socket(AF_INET, SOCK_DGRAM)
udpSerSocket.bind(ADDR)

try:
    while True:
        print("waiting for connection ...")
        data, addr = udpSerSocket.recvfrom(BUFSIZ)
        message = '[{0}]{1}'.format(ctime(), data.decode('utf-8')).encode('utf-8')
        udpSerSocket.sendto(message, addr)
        print("connected from and returned to", addr)
    udpSerSocket.close()
except EOFError and KeyboardInterrupt as ex:
    raise ex
