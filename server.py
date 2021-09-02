# Socket and Threading Library
import socket
import threading
import sys
from const import HOST, PORT


# Initialize Socket Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind host and port
server.bind((HOST, PORT))
# Start Server
server.listen()
# Clients
clients = []
# Users
users = []


# Send Message To All Clients
def broadcast(message: bytes) -> None:
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            # Receive Message
            message = client.recv(1024)
            # Broadcast message to all clients
            broadcast(message)
        except socket.error:
            # Get The Index of the client
            index = clients.index(client)
            # Remove Client
            clients.remove(client)
            # Close Client Connection
            client.close()
            # Get username
            username = users[index]
            broadcast('{} left!'.format(username).encode('ascii'))
            # Remove user
            users.remove(username)
            break


def receive():
    while True:
        # Get Client and address
        client, address = server.accept()
        # Print out
        sys.stdout.write("Connected with {}\n".format(str(address)))
        # Send Data
        client.send('NICKNAME'.encode('ascii'))
        # Get Username
        username = client.recv(1024).decode('ascii')
        # Append data
        users.append(username)
        # Append Client
        clients.append(client)
        sys.stdout.write("User with username is {}\n".format(username))
        broadcast("{} joined!".format(username).encode('ascii'))
        # Send Client Message
        client.send('Connected to server!'.encode('ascii'))
        # Start Thread
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
