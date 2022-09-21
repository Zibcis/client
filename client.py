import socket

port=1024
ip = ''
s = socket.socket()
s.connect ((ip,port))
print(s.recv(1024).decode())
s.close