import socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("127.0.0.1",5000) 
sock.bind(address)
while True: 
      data,addr = sock.recvfrom(1024)
      print(data,addr) 

