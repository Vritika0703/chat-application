import socket
import threading

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            # Handle any issues with receiving messages
            break

def send_messages():
    while True:
        message = input()
        client_socket.send(bytes(message, 'utf-8'))

# Connect to the server
server_ip = input("Enter the server IP: ")
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_messages)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()
