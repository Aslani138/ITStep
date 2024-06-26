import socket

def client_program():
    host = socket.gethostname()
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = client_socket.recv(1024).decode()  # receive response
    print('Received from server: ' + message)  # show in terminal

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
