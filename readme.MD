# Python Socket Chat

This is built using multithreading and socket, for multithreading `threading` module has been used and for socket `socket` module has been used


#### `client.py`

Handles the client side of the program including: sending message and receiving message


#### `server.py`

This is the root socket server that receives message from client program and broadcasts it to all clients that is currently connected to the server


#### `const.py`

Contains HOST and PORT 