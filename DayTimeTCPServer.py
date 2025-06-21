from socket import *
from datetime import datetime
serverPort = 13000
ServerSocket = socket(AF_INET, SOCK_STREAM)
ServerSocket.bind(('', serverPort))
ServerSocket.listen(1)
print("This server is ready to receive...")
message = str(datetime.now())
while True:
    connectionSocket,Clientaddress = ServerSocket.accept()
    connectionSocket.send(message.encode())
    connectionSocket.close()
