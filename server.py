import socket 
from threading import Thread

HOST = "0.0.0.0"
PORT = 3434 

# initialize list/set of all connected client's sockets
client_sockets = set()

# create a TCP socket
s = socket.socket()

# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind the socket to the address we specified
s.bind((HOST, PORT))

# listen for upcoming connections
s.listen(5)

print(f"[*] Listening at {HOST}:{PORT}")


def listen_for_client(cs):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
       
        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg.encode())

while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()

    print(f"[+] {client_address} connected.")

    # add the new connected client to connected sockets
    client_sockets.add(client_socket)

    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))

    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True

    # start the thread
    t.start()

    # goodbye clients
    for cs in client_sockets:
        cs.close()

    # goodbye socket
    s.close()