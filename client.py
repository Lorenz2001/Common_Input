import socket
from pynput.mouse import Listener as muoseList
from pynput.keyboard import Listener as keybList

server_ip = "192.168.1.2" #server ip
server_port = 5000

def on_move(x,y):
    client.send(f"mouse_move:{x},{y}".encode())

def on_click(x,y,button, pressed):
    action = "pressed" if pressed else "released"
    client.send(f"mouse_click:{x},{y},{button},{action}".encode())
def on_key_press(key)
    client.send(f"key_press:{key}".encode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_ip,server_port))

with mouseList(on_move=on_move, on_click=on_click) as mouse_listener:
    with keybList(on_press=on_key_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()