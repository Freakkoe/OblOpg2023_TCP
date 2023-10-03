from socket import *
import threading

# Function to handle a connected client
def handleClient(connectionSocket, address):
    while True:
        # Receive data from the client (up to 1024 bytes)
        data = connectionSocket.recv(1024)
        msg = data.decode()  # Decode the received data into a string
        msg = msg.strip().lower()  # Remove leading/trailing spaces and convert to lowercase
        
        # Check if the client wants to exit
        if msg == 'Exit':
            print("Connection Is Terminated")
            connectionSocket.close()  # Close the connection with the client
            break

        print("Received message from client:", msg)

        # Perform a calculation based on the received message
        result = 0
        operation_list = msg.split()  # Split the message into parts (operands and operator)
        oprnd1 = operation_list[0]  # Extract the first operand
        operation = operation_list[1]  # Extract the operator
        oprnd2 = operation_list[2]  # Extract the second operand

        num1 = int(oprnd1)  # Convert the first operand to an integer
        num2 = int(oprnd2)  # Convert the second operand to an integer

        # Perform the appropriate calculation based on the operator
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "*":
            result = num1 * num2

        # Send the result back to the client
        output = str(result)
        connectionSocket.send(output.encode())  # Encode and send the result to the client

    connectionSocket.close()  # Close the connection with the client when done

# Server configuration
serverName = "127.0.0.1"  # Server's IP address
serverPort = 12000  # Port to listen on
serverSocket = socket(AF_INET, SOCK_STREAM)  # Create a TCP socket
serverSocket.bind((serverName, serverPort))  # Bind the socket to the server's address and port
serverSocket.listen(5)  # Listen for incoming connections with a backlog of 5
print('Server is ready to listen')

# Continuously accept and handle incoming connections
while True:
    connectionSocket, addr = serverSocket.accept()  # Accept an incoming connection
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()  # Start a new thread to handle the client
