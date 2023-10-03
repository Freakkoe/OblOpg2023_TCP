from socket import *

# Server configuration
serverName = "127.0.0.1"  # Server's IP address
serverPort = 12000  # Port to connect to
client = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
client.connect((serverName, serverPort))  # Connect to the server

# Welcome message
print("Welcome To My Calculator")
print(" ")

while True:
    oprnd1 = input("Enter the first operand: ")
    operation = input("Enter the operation (+, -, *, /): ")
    oprnd2 = input("Enter the second operand: ")

    # Combine the user inputs into a single string
    inp = f"{oprnd1} {operation} {oprnd2}"

    # Send the user's input to the server
    client.send(inp.encode())  # Encode and send the input as bytes to the server

    # Receive and display the result from the server
    answer = client.recv(1024)  # Receive up to 1024 bytes from the server
    print("Answer is " + answer.decode())  # Decode and print the result as a string
    
    # Prompt the user to continue or exit
    exit_choice = input("Type 'Exit' to terminate or press Enter to continue: ")
    if exit_choice == "Exit":
        break

# Close the client socket when done
client.close()
