import socket
import threading

# Define the server address and port
HOST = '0.0.0.0'  # Replace with the IP address or hostname of your server
PORT = 8082

# Create a socket to connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Function to receive messages from the server
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print(message)
        except:
            continue

# Function to send messages to the server
def send_message():
    while True:
        message = input()
        client_socket.send(message.encode())

if __name__ == '__main__':
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    send_thread = threading.Thread(target=send_message)
    send_thread.start()
