from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandle(SRH):
    def handle(self):
        print("...connected from:", self.client_address)
        print("开始发送数据")
        self.wfile.write("[{0}] {1}".format(ctime(), self.rfile.readline()))


tcpServ = TCP(ADDR, MyRequestHandle)
print('waiting for connection....')
tcpServ.serve_forever()
