import socket
import random
from threading import Thread
from datetime import datetime

# choose a random color for the client
client_color = 'white'

# server's IP address
# if the server is not on this machine, 
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 3434 # server's port

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")


name = input('your name please: ')

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)

# make the thread daemon so it ends whenever the main thread ends
t.daemon = True

# start the thread
t.start()


while True:
    # input message we want to send to the server
    to_send =  input()
    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    to_send = f"{client_color}[{date_now}] {name}{to_send}"
    # finally, send the message
    s.send(to_send.encode())

# close the socket
s.close()