# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
TCP_PORT = 6789
BUFFER_SIZE = 4096
serverSocket.bind(("127.0.0.1", TCP_PORT))
serverSocket.listen(4)
print('Server initialized\n')
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()  # Fill in start #Fill in end
    try:
        message = connectionSocket.recv(BUFFER_SIZE)  # Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()  # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        # Fill in end
        # Send the content of the requested file to the client
        connectionSocket.send(outputdata.encode())
        connectionSocket.send("\r\n".encode('UTF-8'))
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n\r\n'.encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
serverSocket.close()
