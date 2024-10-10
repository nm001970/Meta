import  socket
import  numpy as np
from  sklearn.linear_model import LinearRegression


class socketServer:
    def __init__(self, address ='', port = ''):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = address
        self.port = port
        self.sock.bind((self.address, self.port))

    def listen(self):
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()
        print('connection from', self.addr)
        self.cummdata = ''

        while True:
            data = self.conn.recv(10000)
            self.cummdata += data.decode('utf-8')
            print(data)
            if not data:
                print('no data')
                break
            self.conn.send(bytes(calcregr(self.cummdata), 'utf-8'))
            return self.cummdata

    def  __del__(self):
        self.conn.close()