import pyperclip
import socket


server_ip = "192.168.1.2" #server ip
server_port = 5000


def sync_clipboard():
    last_clipboard = ""
    while True:
        current_clipboard = pyperclip.paste()
        if current_clipboard != last_clipboard
        client.send(f"clipboard:{current_clipboard}".encode)
        last_clipboard = current_clipboard
        
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip,server_port))