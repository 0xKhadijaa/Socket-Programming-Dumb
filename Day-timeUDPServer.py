from socket import *
serverPort = 13000
ServerSocket = socket(AF_INET, SOCK_DGRAM)
ServerSocket.bind(('', serverPort))
print("This server is ready to receive...")
while True:
    message, ClientAddress = ServerSocket.recvfrom(2048)
    modifiedmessage = message.decode()
    ServerSocket.sendto(modifiedmessage.encode(), ClientAddress)
