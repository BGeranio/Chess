import socket
import chess
import pickle
from threading import Thread

newBoard = chess.board(0, 'white')
newBoard.makeBoard()

def acceptConnection():
    while True:
        client, addr = s.accept()
        print(f"{addr} has connected")
        client.send(bytes("greetings!", 'utf-8'))
        addresses[client] = addr
        Thread(target=handleClient, args=(client,)).start()


def handleClient(client):
    name = client.recv(1024).decode('utf-8')
    welcome = 'welcome %s if you ever want to quit, type {quit} to exit' % name

    
    client.send(bytes(welcome, 'utf-8'))

    msg = '%s has joined the game!' % name
    
    clients[client] = name
    broadcastBoard(newBoard.printBoard())
    broadcast(msg)
    while True:
        msg = client.recv(1024)
        if msg != bytes('{quit}', 'utf-8'):
            newBoard.handleMoves(newBoard, msg.decode('utf-8')[:2], msg.decode('utf-8')[2:])
            broadcastBoard(newBoard.printBoard())
            broadcast('\n')
        else:
            client.send(bytes('{quit}', 'utf-8'))
            client.close()
            del clients[client]
            broadcast(bytes('%s has left' % name, 'utf-8'))
            break


def broadcastBoard(msg,):
    for socket in clients:
        socket.send(bytes(msg, 'utf-8'))

def broadcast(msg, prefix=""):
    for socket in clients:
        sender = prefix + msg
        socket.send(bytes(sender, 'utf-8'))


clients = {}
addresses = {}

host = "127.0.0.1"
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))

if __name__ == "__main__":

    s.listen(5)
    print('waiting for connection...')
    ACCEPT_THREAD = Thread(target=acceptConnection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    s.close()
