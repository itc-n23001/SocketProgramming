import socket

IPADDR = "127.0.0.1"
PORT = 49152

sock = socket.socket(socket.AF_INET)
sock.connect((IPADDR, PORT))

sock.send("hello".encode("utf-8"))
