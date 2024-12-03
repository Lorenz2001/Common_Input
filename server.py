import socket
from pynput.mouse import Controller as mouseCtlr
from pynput.keyboard import Controller as KeybCtrl

HOST = '0.0.0.0'
PORT = 12345

def handle_client(client_socket)
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        if not data: 
            break
        print("Received:", data)
    client_socket.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',5000)) #port ip
server.listen(5)


def start_server():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST,PORT))
        server_socket.listen(5)
        
        print(f"Server online on {HOST}:{PORT}")
        while True:
            client_socket, addr = server.accept()
            print("Connection accepted by: ", addr)
            handle_client(client_socket)

if __name__ == "__main__"
    start_server()