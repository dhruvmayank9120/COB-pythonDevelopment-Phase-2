import socket
import threading

# Define the server address and port
HOST = '0.0.0.0'  # Allows connections from any network interface
PORT = 8082

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

# List to store connected clients
clients = []

# Function to broadcast messages to all connected clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                # Remove the client if unable to send a message
                clients.remove(client)

# Function to handle each client separately
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                # Remove the client if they disconnect
                clients.remove(client_socket)
                break
            broadcast(message, client_socket)
        except:
            continue

# Main function to accept client connections
def main():
    print(f"Chat server is running on {HOST}:{PORT}")
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"New connection from {client_address}")
        clients.append(client_socket)

        # Create a thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == '__main__':
    main()
