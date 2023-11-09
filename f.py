import socket

# サーバーIPとポート番号
IPADDR = "127.0.0.1"
PORT = 49152

sock_sv = socket.socket(socket.AF_INET)
sock_sv.bind((IPADDR, PORT))
sock_sv.listen()

while True:
    sock_cl, addr = sock_sv.accept()
    data = sock_cl.recv(1024)
    print(data.decode("utf-8"))
    sock_cl.close()
