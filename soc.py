#-*-coding:UTF-8-*-

import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcp_server.bind(("10.0.2.15", 52001))

tcp_server.listen(1)
print('Wait tcp accepting...')
client, address = tcp_server.accept()
print(f'Connected client ip : {address}')

rcv_data = client.recv(1024)
print(f'Data : {rcv_data.decode("utf-8")}')

client.send('Hi!'.encode("utf-8"))
client.close()
