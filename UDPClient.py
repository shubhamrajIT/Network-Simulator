from socket import socket, AF_INET, SOCK_DGRAM
s = socket(AF_INET, SOCK_DGRAM)
s.bind(('127.0.0.1', 0))
print("using", s.getsockname())
server = ('127.0.0.1', 11111)
message="Hello World"
message=str.encode(message)
s.sendto(message, server)
data, addr = s.recvfrom(1024)
print("received", data, "from", addr)
s.close()
