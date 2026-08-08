print("|========================================|"
      "| Connection with TCP Client "
      "||========================================|")
print()
import socket
s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
port_no = 12345
host_name = socket.gethostname()
s_socket.bind((host_name, port_no))
s_socket.listen(3)

while 1:
    c_socket, address = s_socket.accept()
    print("Connection accepted from %s" % str(address))
    msg = input("Enter message to send to client: ")
    c_socket.send(msg.encode('ascii'))
    c_socket.close()