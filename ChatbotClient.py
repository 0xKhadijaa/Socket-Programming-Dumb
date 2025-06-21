import socket
ServerName = '10.75.47.215'
ServerPort = 20000
clientsocket = socket.socket()
print(clientsocket)
clientsocket.connect((ServerName, ServerPort))
message = input( "Enter any message: ")
clientsocket.send(message.encode())
Reply = clientsocket.recv(1024)
print(Reply.decode())
clientsocket.close()