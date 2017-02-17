#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
host = socket.gethostname()
port = 10000

sock.bind(('', port))

sock.listen(1)
while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from' + str(client_address))

        # Receive the data in small chunks and retransmit it
        data_list = []
        while True:
            data = connection.recv(16)
            data_list.append(data)
            print('received "%s"' % data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from' + str(client_address))
                break

    finally:
        # Clean up the connection
        connection.close()
        print((b''.join(data_list)).decode('ascii'))
