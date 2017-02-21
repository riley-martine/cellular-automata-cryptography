#!/usr/bin/env python3
"""Server receives, client sends."""

import socket
#print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

import threading
import time

from CellAuto_Cryptography import Automaton

class clientThread(threading.Thread):

    def __init__(self, ip, message):
        threading.Thread.__init__(self)
        self.ip = ip
        self.message = bytes(message, encoding='utf-8')
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        self.server_address = (ip, 10000)  # 192.168.193.214

    def run(self):
        self.connect()
        self.send_data(self.message)

    def connect(self):
        print('connecting to %s port %s' % self.server_address)
        try:
            self.sock.connect(self.server_address)
        except ConnectionRefusedError as e:
            print(e)
            raise(e)

        except OSError as e:
            print(e)
            raise(e)

    def send_data(self, message):
        try:
            # Send data
            print('sending "%s"' % message)
            self.sock.sendall(message)

        finally:
            print('closing socket')
            self.sock.close()


class serverThread(threading.Thread):

    def __init__(self, key):
        threading.Thread.__init__(self)
        self.key = key

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 10000)
        print('starting up on %s port %s' % server_address)
        port = 10000
        sock.bind(('', port))
        sock.listen(1)
        print('waiting for a connection')

        connection, client_address = sock.accept()

        try:
            print('connection from' + str(client_address))

            # Receive the data in small chunks and retransmit it
            data_list = []
            while True:
                data = connection.recv(16)
                if data != b'':
                    data_list.append(data)
                    print('received "%s"' % data)
                if data:
                    pass
                else:
                     print('no more data from' + str(client_address))
                     break

        finally:
            # Clean up the connection
            connection.close()
            received = (b''.join(data_list)).decode('utf-8')
            print("Received: ", end='')
            print(received)
            automaton = Automaton(seed=[int(k) for k in self.key])
            print("Message: " + automaton.getPlainText(received))
