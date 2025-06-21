from socket import *
from datetime import datetime
ServerName = 'localhost'
ServerPort = 13000
clientsocket = socket(AF_INET, SOCK_DGRAM)
message = str(datetime.now())
clientsocket.sendto(message.encode(), (ServerName , ServerPort))
modifiedMessage, ServerAddress= clientsocket.recvfrom(2048)
print(modifiedMessage.decode())
clientsocket.close()
