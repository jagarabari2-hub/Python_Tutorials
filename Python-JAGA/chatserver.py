import socket
import threading

print("|========================================|")
print("| Chat Server Socket Programming         |")
print("|========================================|")
print()

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Send message to all clients except sender
def broadcast(message, sender=None):
    for client in clients:
        if client != sender:
            try:
                client.send(message)
            except:
                pass

def handle(client):
    while True:
        try:
            message = client.recv(1024)

            if not message:
                break

            # Print client message on server terminal
            print(message.decode("utf-8"))

            # Send message to other clients
            broadcast(message, client)

        except:
            break

    # Remove disconnected client
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]

        clients.remove(client)
        nicknames.remove(nickname)
        client.close()

        print(f"{nickname} disconnected.")
        broadcast(f"{nickname} left the chat.".encode("utf-8"))

def receive():
    print("Server is running on 127.0.0.1:5000")

    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")

        broadcast(f"{nickname} joined the chat!".encode("utf-8"))
        client.send("Connected to the server!".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()