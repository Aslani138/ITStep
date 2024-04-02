import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()  # get instance
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    message = 'Connection successful to server ' + str(host)
    conn.send(message.encode())  # send message
    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()
