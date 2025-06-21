from socket import * 
serverPort = 20000
ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.bind(('', serverPort))
ServerSocket.listen(1)
print( " This server is ready to receive... " )
while True:
    connectionSocket,address = ServerSocket.accept()
    message= connectionSocket.recv(1024).decode()
    connectionSocket.send(message.encode())
    connectionSocket.close()
