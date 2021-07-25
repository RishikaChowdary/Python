import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=socket.gethostname()
port=9999
client.connect((name,port))
msg=client.recv(1024)
client.close()
print(msg.decode('ascii'))
