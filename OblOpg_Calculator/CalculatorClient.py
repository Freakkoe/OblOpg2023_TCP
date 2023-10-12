from socket import *

# Serverkonfiguration
serverName = "127.0.0.1"  # Serverens IP-adresse
serverPort = 12000  # Port at forbinde til
client = socket(AF_INET, SOCK_STREAM)  # Opret en TCP-socket
client.connect((serverName, serverPort))  # Opret forbindelse til serveren

# Velkomstbesked
print("Welcome to my calculator")
print(" ")

while True:
    oprnd1 = input("Enter the first operand: ")
    operation = input("Enter operationen (+, -, *, /): ")
    oprnd2 = input("Enter the second operand: ")

    # Kombiner brugerens input til en samlet string
    inp = f"{oprnd1} {operation} {oprnd2}"

    # Send brugerens input til serveren
    client.send(inp.encode())  # Send input som bytes til serveren

    # Modtag og vis resultatet fra serveren
    answer = client.recv(1024)  # Modtag op til 1024 bytes fra serveren
    print("Answer is " + answer.decode())  # Decode og udskriv resultatet som en string

    # Bed brugeren om at fortsætte eller afslutte
    exit_choice = input("Type 'Exit' to terminate or press Enter to continue: ")
    if exit_choice == "Exit":
        break

# Luk klientsocketen når færdig
client.close()
