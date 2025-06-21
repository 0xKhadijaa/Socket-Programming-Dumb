from socket import *
ServerName = 'localhost'
ServerPort = 13000
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((ServerName, ServerPort))
modifiedMessage = clientsocket.recv(1024)
print('From Server:', modifiedMessage.decode())
clientsocket.close()
