from socket import *
import hashlib
import time
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))


def gerar_checksum(entrada):
    checksum=hashlib.sha256()
    checksum.update(entrada.encode())
    checksum=checksum.hexdigest()
    return checksum

def execucao_normal():
    print("Servidor em execução.")
    while True:
        message, clientAddress= serverSocket.recvfrom(2048)
        message=message.decode()
        message=message.split()
        checksum, package_number=message[len(message)-1],message[len(message)-2]
        message.pop(len(message)-1)
        message.pop(len(message)-1)
        message=" ".join(message)
        print(f'Mensagem do cliente: {message}')
        checksum_server=gerar_checksum(message)
        if(checksum==checksum_server):
            print("Mensagem íntegra!")
            print(f'Pacote recebido: {package_number}')
            ack=f'Pacote recebido no servidor:{package_number}'
            serverSocket.sendto(ack.encode(), clientAddress)
            modifiedMessage = message.upper()
            print(f'Mensagem modificada:{modifiedMessage}')
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    
        else:
            print("Mensagem corrompida!")

def execucao_com_atraso():
    print("Servidor em execução.")
    while True:
        message, clientAddress= serverSocket.recvfrom(2048)
        message=message.decode()
        message=message.split()
        checksum, package_number=message[len(message)-1],message[len(message)-2]
        message.pop(len(message)-1)
        message.pop(len(message)-1)
        message=" ".join(message)
        print(f'Mensagem do cliente: {message}')
        checksum_server=gerar_checksum(message)
        if(checksum==checksum_server):
            print("Mensagem íntegra!")
            print(f'Pacote recebido: {package_number}')
            for k in range(0,5):
                print(k)
                time.sleep(1)
            ack=f'Pacote recebido no servidor: {package_number}'
            serverSocket.sendto(ack.encode(), clientAddress)
            modifiedMessage = message.upper()
            print(f'Mensagem modificada:{modifiedMessage}')
            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    
        else:
            print("Mensagem corrompida!")


def iniciar_servidor():
    opcao=int(input("Reliable Data Transfer(RDT)\nServidor\nDigite o número correspondente à opção que deseja:\n1.Execução normal;\n2.Atraso intencional.\n "))
    if opcao==1:
        execucao_normal()
    elif opcao==2:
        execucao_com_atraso()

iniciar_servidor()


    