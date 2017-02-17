import socket
import handshake

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip = input("sever ip address: ")
server_address = (ip, 10000) #192.168.193.214
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

def send_data(message):
    try:
        # Send data
        # message = b'line four is very very long and stuff and ling anad lng'
        print('sending "%s"' % message)
        sock.sendall(message)
        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received "%s"' % data)

    finally:
        print('closing socket')
        sock.close()
