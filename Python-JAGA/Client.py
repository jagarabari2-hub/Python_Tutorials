import socket
import time

serveraddress = ('127.0.0.1', 12345)
print('Connecting to server at %s:%s' % serveraddress)

clientsock = None
for attempt in range(5):
    try:
        clientsock = socket.create_connection(serveraddress, timeout=2)
        break
    except ConnectionRefusedError:
        if attempt < 4:
            print('Server is not ready yet. Retrying...')
            time.sleep(1)
        else:
            print('Could not connect. Start Server.py first and try again.')
            raise

try:
    senddata = input('Send The message to the server: ')
    print('Sending the message... "%s"' % senddata)
    clientsock.sendall(senddata.encode('utf-8'))
    recvdata = clientsock.recv(1024)
    print('Received data: "%s"' % recvdata)
finally:
    print('Closing the socket')
    clientsock.close()