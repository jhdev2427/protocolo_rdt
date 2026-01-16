from socket import*
import hashlib
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

def gerar_checksum(entrada):
    checksum=hashlib.sha256()
    checksum.update(entrada.encode())
    checksum=checksum.hexdigest()
    return checksum

def temporizador_cliente(mensagem):
    i=0
    while i<4:
        clientSocket.settimeout(3)
        try:
            ack_server, serverAddress = clientSocket.recvfrom(2048)
            modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        
        except timeout:
            reenviar_mensagem(mensagem)
            i+=1

        else:
            print(ack_server.decode())
            print(modifiedMessage.decode())
            break
        
def reenviar_mensagem(mensagem):
    clientSocket.sendto(mensagem.encode(),(serverName, serverPort))
    #clientSocket.sendto(checksum.encode(),(serverName, serverPort))

    
def enviar_mensagem(quantidade):
    package_number=0
    while package_number<quantidade:
        package_number+=1
        package_number=str(package_number)
        message = input("Insira a mensagem:")
        checksum_cliente=gerar_checksum(message)
        message=message+" "+package_number+" "+f'{checksum_cliente}'
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        #clientSocket.sendto(checksum.encode(),(serverName, serverPort))
        temporizador_cliente(message)
        package_number=int(package_number)


def iniciar_aplicação():
    opcao=int(input("Digite o número correspondente a opção que deseja:\n1.Entrega normal\n2.Atraso intencional\n3.Corrupção de dados"))
    if(opcao==1):
        numero_de_pacotes=int(input("Quantos pacotes deseja enviar?\n"))
        enviar_mensagem(numero_de_pacotes)
    else if(opcao==2):



iniciar_aplicação()

#clientSocket.close()