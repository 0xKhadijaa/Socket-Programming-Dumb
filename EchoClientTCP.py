from socket import *
ServerName = 'localhost'
ServerPort = 15000
clientsocket = socket(AF_INET,  SOCK_STREAM)
clientsocket.connect((ServerName, ServerPort))
message = input("Enter any data:")
clientsocket.send(message.encode())
modifiedMessage = clientsocket.recv(1024)
print(modifiedMessage.decode())
clientsocket.close()