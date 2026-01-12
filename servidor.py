from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))
print("Servidor em execução.")
while True:
    message, clientAddress= serverSocket.recvfrom(2048)
    message=message.decode()
    if(len(message)!=0):
        message=message.split()
        package_number=message[len(message)-1]
        message.pop(len(message)-1)
        message=" ".join(message)
        print(f'Pacote recebido: {package_number}')
        print(message)
        modifiedMessage = message.upper()
        print(modifiedMessage)
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    
    else:
        print("Mensagem vazia!")
    