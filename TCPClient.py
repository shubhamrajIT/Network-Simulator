from socket import *
serverName ="localhost"
serverPort = 80
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence =input("Input lowercase sentence:")
sentence=str.encode(sentence)
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print("From Server:", modifiedSentence)
clientSocket.close()