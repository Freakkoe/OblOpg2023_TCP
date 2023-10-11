from socket import *
import threading

# Funktion til at håndtere en tilsluttet klient
def handleClient(connectionSocket, address):
    while True:
        data = connectionSocket.recv(1024)        # Modtag data fra klienten (op til 1024 bytes)
        msg = data.decode()  # Decode den modtaget data til en string
        msg = msg.strip().lower()  # Fjern førende/efterfølgende mellemrum og konverter til små bogstaver

        # Tjek om klienten ønsker at afslutte
        if msg == 'Exit':
            print("Connection terminated")
            connectionSocket.close()  # Luk forbindelsen med klienten
            break

        print("Received message from client:", msg)

        # Udfør en beregning baseret på den modtagne besked
        result = 0
        operation_list = msg.split()  # Del beskeden op i dele (operand og operator)
        oprnd1 = operation_list[0]  # Udtræk den første operand
        operation = operation_list[1]  # Udtræk operatoren
        oprnd2 = operation_list[2]  # Udtræk den anden operand

        num1 = int(oprnd1)  # Konverter den første operand til et heltal
        num2 = int(oprnd2)  # Konverter den anden operand til et heltal

        # Udfør den passende beregning baseret på operatoren
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2

        # Send resultatet tilbage til klienten
        output = str(result)
        connectionSocket.send(output.encode())  # Kode og send resultatet til klienten

    connectionSocket.close()  # Luk forbindelsen med klienten når færdig

# Serverkonfiguration
serverName = "127.0.0.1"  # Serverens IP-adresse
serverPort = 12000  # Port at lytte på
serverSocket = socket(AF_INET, SOCK_STREAM)  # Opret en TCP-socket
serverSocket.bind((serverName, serverPort))  # Bind socket til serverens adresse og port
serverSocket.listen(5)  # Lyt efter indkommende forbindelser med en kø på 5
print('Server is ready to listen')

# Accepter og håndter indkommende forbindelser kontinuerligt
while True:
    connectionSocket, addr = serverSocket.accept()  # Accepter en indkommende forbindelse
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()  # Start en ny tråd til at håndtere klienten
