import socket

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveraddress = ('127.0.0.1', 12345)

print('Starting the server on the %s port %s' % serveraddress)
serversock.bind(serveraddress)
serversock.listen(1)

while True:
    print('Waiting for a connection from a client')
    conn, clientaddress = serversock.accept()
    try:
        print('Received connection from', clientaddress)
        while True:
            data = conn.recv(1024)
            print('Received data is "%s"' % data)
            if data:
                print('Sending data back to the client.')
                conn.sendall(data)
            else:
                print('There is no more data.', clientaddress)
                break
    finally:
        conn.close()
        