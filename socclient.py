#-*-coding: UTF-8-*-

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(("10.0.2.15",52001))

tcp_socket.send('Hello!'.encode("utf-8"))
response = tcp_socket.recv(1024)
print(f'Data : {response.decode("utf-8")}')
