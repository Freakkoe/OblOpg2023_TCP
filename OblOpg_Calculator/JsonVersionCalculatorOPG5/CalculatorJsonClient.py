import json
from socket import *

# Server configuration
serverName = "127.0.0.1"  # Server's IP address
serverPort = 12000  # Port to connect to
client = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
client.connect((serverName, serverPort))  # Connect to the server

# Welcome message
print("Welcome To My Calculator\n")

while True:
    oprnd1 = input("Enter the first operand: ")
    operation = input("Enter the operation (+, -, *, /): ")
    oprnd2 = input("Enter the second operand: ")

    # Create a JSON request object
    request = {
        "method": operation,
        "Tal1": int(oprnd1),
        "Tal2": int(oprnd2)
    }

    client.send(json.dumps(request).encode())  # Encode and send the JSON request to the server
    response = client.recv(1024)  # Receive up to 1024 bytes from the server

    try:
        response_data = json.loads(response.decode())  # Decode the received JSON response into a Python dictionary
        if "error" in response_data:
            print("Error:", response_data["error"])
        else:
            print("Answer is", response_data["result"])
    except json.JSONDecodeError:
        print("Invalid JSON response from server")

    exit_choice = input("Type 'Exit' to terminate or press Enter to continue: ")
    if exit_choice.lower() == "exit":
        break

# Close the client socket when done
client.close()
