from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
TCP_PORT = 6789
BUFFER_SIZE = 4096
serverSocket.bind(("127.0.0.1", TCP_PORT))
serverSocket.listen(4)
print('Server initialized')
while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connection address:', addr)
    try:
        message = connectionSocket.recv(BUFFER_SIZE)
        filename = message.split()[1]
        f = open(filename[1:], 'r')
        outputData = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
        for i in range(0, len(outputData)):
            connectionSocket.send(outputData[i].encode('utf-8'))
        connectionSocket.send("\r\n".encode('utf-8'))
        print("File sent.\n")
    except IOError:
        fail = '''<html> <head> <title> 404 </title> </head> <body><h1>404 NOT FOUND</h1> <h3> Nothing was found! </h3> 
        </body></html> '''
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
        for q in fail:
            connectionSocket.send(q.encode('utf-8'))
        connectionSocket.close()
