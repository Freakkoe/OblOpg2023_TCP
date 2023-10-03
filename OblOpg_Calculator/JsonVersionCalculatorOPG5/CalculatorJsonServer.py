import json
from socket import *
import threading

# Function to handle a connected client
def handleClient(connectionSocket, address):
    while True:
        try:
            data = connectionSocket.recv(1024)  # Receive data from the client (up to 1024 bytes)
            if not data:
                break
            
            request = json.loads(data.decode())  # Decode the received JSON data into a Python dictionary
            
            # Check if the request has required fields
            if "method" not in request or "Tal1" not in request or "Tal2" not in request:
                response = {"error": "Invalid request format"}
            else:
                method = request["method"]
                num1 = request["Tal1"]
                num2 = request["Tal2"]
                result = 0
                
                # Perform the requested calculation based on the method
                if method == "+":
                    result = num1 + num2
                elif method == "-":
                    result = num1 - num2
                elif method == "*":
                    result = num1 * num2
                elif method == "/":
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        response = {"error": "Division by zero"}
                        connectionSocket.send(json.dumps(response).encode())
                        continue
                
                response = {"result": result}
            
            connectionSocket.send(json.dumps(response).encode())  # Encode and send the response as JSON
            
        except json.JSONDecodeError:
            response = {"error": "Invalid JSON format"}
            connectionSocket.send(json.dumps(response).encode())
        
        except Exception as e:
            response = {"error": str(e)}
            connectionSocket.send(json.dumps(response).encode())
    
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
