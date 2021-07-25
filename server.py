import socket
networkSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientName=socket.gethostname()
port=9999
networkSocket.bind((clientName,port))
networkSocket.listen(3)
while True:
    clientsocket,add=networkSocket.accept()
    print('Connected to, ',clientName)
    msg="Don't sleep...."
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
    
