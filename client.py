import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

msg = s.recv(3)
print(msg.decode("utf-8"))
