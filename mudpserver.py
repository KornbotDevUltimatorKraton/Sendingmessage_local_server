import socket 
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
address = "127.0.0.1"
sock.sendto("Sending".encode('utf-8'),(address,5000)) 

