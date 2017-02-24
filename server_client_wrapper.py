#!/usr/bin/env python3
"""Server receives, client sends."""

import socket
import threading
from CellAuto_Cryptography import Automaton


class ClientThread(threading.Thread):
    """Thread that sends message to client over sockets."""
    def __init__(self, ip, message):
        threading.Thread.__init__(self)
        self.server_ip = ip
        self.message = bytes(message, encoding='utf-8')
        # Create a TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect the socket to the port where the server is listening
        self.server_address = (ip, 10000)  # 192.168.193.214

    def run(self):
        self.connect()
        self.send_data(self.message)

    def connect(self):
        """Connect to server."""
        print('connecting to %s port %s' % self.server_address)
        try:
            self.sock.connect(self.server_address)
        except ConnectionRefusedError as error:
            print(error)
            raise error

        except OSError as error:
            print(error)
            raise error

    def send_data(self, message):
        """Send data to server."""
        try:
            # Send data
            print('sending "%s"' % message)
            self.sock.sendall(message)

        finally:
            print('closing socket')
            self.sock.close()


class ServerThread(threading.Thread):
    """Thread that listens for data being sent."""
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
            print(b''.join(data_list))
            automaton = Automaton(key=[int(k) for k in self.key])
            print("Message: " + automaton.getPlainText(received))
