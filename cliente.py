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

def reenviar_mensagem(mensagem):
    clientSocket.sendto(mensagem.encode(),(serverName, serverPort))


def temporizador_cliente(mensagem):
    i=0
    while i<5:
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

def enviar_mensagem_corrompida(quantidade):
    package_number=0
    while package_number<quantidade:
        package_number+=1
        package_number=str(package_number)
        message = input("Insira a mensagem:")
        message_corrompida= message + "Texto_externo_adicionado"
        checksum_cliente=gerar_checksum(message_corrompida)
        message=message+" "+package_number+" "+f'{checksum_cliente}'
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        #clientSocket.sendto(checksum.encode(),(serverName, serverPort))
        temporizador_cliente(message)
        package_number=int(package_number)


def iniciar_aplicação():
    while True:
        opcao=int(input("Reliable Data Transfer (RDT) \n\nDigite o número correspondente a opção que deseja:\n1.Entrega normal\n2.Corrupção de dados\n"))
        numero_de_pacotes=int(input("Quantos pacotes deseja enviar?\n"))
        if opcao==1:
            enviar_mensagem(numero_de_pacotes)
            break
        elif opcao==2:
            enviar_mensagem_corrompida(numero_de_pacotes)
            break
        elif type(opcao)!=int and opcao>2:
            print("Entrada inválida!")
            continue


iniciar_aplicação()

#clientSocket.close()