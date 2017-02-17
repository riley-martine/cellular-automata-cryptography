#!/usr/bin/env python3

import client
import server
import socket


print(socket.gethostbyname(socket.gethostname()))


client.send_data(b'message is here and will only be sent once')
