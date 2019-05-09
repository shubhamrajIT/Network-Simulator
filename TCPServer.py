from socket import *
import datetime as dt


serverPort =13
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('0.0.0.0',serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
reply=str(dt.datetime.now())
reply=str.encode(reply)
print(reply)
while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(2000)
    if serverPort==80:
        capitalizedSentence = sentence.upper()
        connectionSocket.send(capitalizedSentence)
    if serverPort==13:
        connectionSocket.send(reply)
    connectionSocket.close()