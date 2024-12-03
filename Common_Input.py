import socket
from pynput.mouse import Controller as mouseCtlr
from pynput.keyboard import Controller as KeybCtrl

mouse = mouseCtlr()
keyboard= KeybCtrl()

def handle_client(client_socket)
    while True:
        data = client_socket.recv(1024).decode()
        if not data: 
            break
        print("Received:", data)
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',5000)) #port ip
server.listen(5)

print("Server online")
while True:
    client_socket, addr = server.accept()
    print("Connection accepted by: ", addr)
    handle_client(client_socket)