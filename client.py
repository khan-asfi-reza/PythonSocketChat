import socket
import sys
import threading
import time

from const import HOST, PORT

# Get Username
username = input("Choose your username: ")
# socket initialization
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Client Connection
client.connect((HOST, PORT))


# Receive socket data
def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(username.encode('ascii'))
            else:
                sys.stdout.write(f"{message}\n")
        except socket.error:
            sys.stdout.write("An error occurred!\n")
            client.close()
            break


def write():
    while True:  # message layout
        time.sleep(1)
        print("Your Message: ", end="")
        inp = input('')
        message = '{}: {}'.format(username, inp)
        client.send(message.encode('ascii'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()
time.sleep(3)
write_thread = threading.Thread(target=write)
write_thread.start()
