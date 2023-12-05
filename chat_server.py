import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {address}: {data.decode('utf-8')}")
        
        # Broadcast the received message to all connected clients
        broadcast(data, client_socket)
    
    print(f"Connection from {address} closed")
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if there is an issue sending the message
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Configure the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()

print("Server is listening for incoming connections...")

# Store the connected clients
clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)

    # Create a thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")
    
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Received from {address}: {data.decode('utf-8')}")
        
        # Broadcast the received message to all connected clients
        broadcast(data, client_socket)
    
    print(f"Connection from {address} closed")
    client_socket.close()

def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if there is an issue sending the message
                remove(client)

def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)

# Configure the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen()

print("Server is listening for incoming connections...")

# Store the connected clients
clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)

    # Create a thread to handle the client
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
