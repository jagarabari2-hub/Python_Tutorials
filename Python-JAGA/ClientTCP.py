print("|========================================|"
      "| Connection with TCP Server "
      "||========================================|")
print()
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
port_no = 12345
host_name = socket.gethostname()
client_socket.connect((host_name, port_no))
message = client_socket.recv(1024)
client_socket.close()
print("Message from server: ", message.decode('ascii'))