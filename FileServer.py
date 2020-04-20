import socket
s=socket.socket()
s.connect(('localhost',6465))
filename1="python.png"
s.send(filename1.encode())
ms=s.recv(1024)
print(ms.decode())
s.close()