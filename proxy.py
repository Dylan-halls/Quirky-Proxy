import socket, threading

class Main_Proxy(object):

    def __init__(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", 8080))
        s.listen(5)
        s.accept()
    
    def client_handler(self):
        while True:
            sock, addr = s.accept()
            data = sock.recv(1024)
            return data

    def server_handler(self, data):
        so = socket.socket()
        so.connect(("127.0.0.1", 9090))
        so.send(data)

if __name__ == '__main__':
    mp = Main_Proxy()
    while True:
        data = mp.client_handler()
        mp.server_handler(data)
