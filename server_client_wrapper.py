#!/usr/bin/env python3

import socket
print("Your IP: ", end ='')
print([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])

import subprocess
import client
import server


# server_thread = threading.Thread(target=server.start_server())
# server_thread.start()
# server_thread.run()
server_sub = subprocess.run(['python3', 'server.py'])

client.connect()

client.send_data(b'message is here and will only be sent once')
