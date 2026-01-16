from socket import*
import asyncio
serverName = "127.0.0.1"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
package_number=0
numero_de_pacotes=int(input("Quantos pacotes deseja enviar?"))
while package_number<numero_de_pacotes:
    package_number+=1
    package_number=str(package_number)
    message = input("Insira a mensagem:")
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    clientSocket.sendto(package_number.encode(),(serverName, serverPort))
    variavel=clientSocket.settimeout(2)
    print(variavel)
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    package_number=int(package_number)


#clientSocket.close()