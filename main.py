from socket import *


def send_file(conn_socket: socket, http_response: str, data_str: str) -> None:
    """
    Sends a string through the connection socket
    :param http_response: HTTP response message
    :rtype: None
    :param conn_socket: The open connection socket
    :param data_str: The string 
    """
    conn_socket.send(http_response.encode())
    conn_socket.send(data_str.encode())
    connectionSocket.send("\r\n".encode('UTF-8'))


def get_filename_from_http_request(request: str) -> str:
    """
    Gets the requested file's name from the http request by splitting the request to multiple strings,
    getting the second string, and removing the first character.
    :param request: the http request string
    :return: the file name requested in the http request.
    """
    return request.split()[1][1:]


HOST_IP: str = "127.0.0.1"
TCP_PORT: int = 6789
BUFFER_SIZE: int = 4096

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST_IP, TCP_PORT))
serverSocket.listen(4)
print('Server initialized\n')

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print('Connection address:', addr)
    http_request = connectionSocket.recv(BUFFER_SIZE).decode('utf-8')
    print("HTTP Request: " + http_request)
    filename = get_filename_from_http_request(http_request)
    try:
        requestedFile = open(filename, 'r')
        requestedFileData = requestedFile.read()
        send_file(connectionSocket, 'HTTP/1.1 200 OK\r\n\r\n', requestedFileData)

        print("*** File sent. ***\n")
    except IOError:
        errFile = open('err_page.html', 'r')
        errFileData = errFile.read()
        send_file(connectionSocket, 'HTTP/1.1 404 NOT FOUND\r\n\r\n', errFileData)
        connectionSocket.close()

# noinspection PyUnreachableCode
serverSocket.close()
