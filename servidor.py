from socket import *
import hashlib
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))
print("Servidor em execução.")

def gerar_checksum(entrada):
    checksum=hashlib.sha256()
    checksum.update(entrada.encode())
    checksum=checksum.hexdigest()
    return checksum

def temporizador_cliente(ack_cliente):
    i=0
    while i<4:
        serverSocketSocket.settimeout(3)
        try:
            ack_cliente, clientAddress = clientSocket.recvfrom(2048)
        
        except timeout:
            reenviar_mensagem(mensagem)
            i+=1

        else:
            print(ack_cliente.decode())
            break
        
while True:
    message, clientAddress= serverSocket.recvfrom(2048)
    #checksum, clientAddress= serverSocket.recvfrom(2048)
    message=message.decode()
    message=message.split()
    checksum, package_number=message[len(message)-1],message[len(message)-2]
    message.pop(len(message)-1)
    message.pop(len(message)-1)
    message=" ".join(message)
    checksum_server=gerar_checksum(message)
    print(checksum,checksum_server)
    if(checksum==checksum_server):
        print("Mensagem íntegra!")
        print(f'Pacote recebido: {package_number}')
        ack=f'Pacote recebido {package_number}'
        serverSocket.sendto(ack.encode(), clientAddress)
        modifiedMessage = message.upper()
        print(modifiedMessage)
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)

    #package_number,clientAddress2= serverSocket.recvfrom(2048)
    
    else:
        print("Mensagem corrompida!")
    