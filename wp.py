import socket
import chess
from threading import Thread
import tkinter


def receive():
    while True:
        try:
            msg = s.recv(1024).decode('utf-8')
            newArr = msg.split('\n')
            
            for i in newArr:
                msgList.insert(tkinter.END, i)
        except OSError:
            break

def send(event = None):
    newMsg = myMsg.get() + myMsg2.get()
    myMsg.set("")
    myMsg2.set("")
    s.send(bytes(newMsg, 'utf-8'))
    if newMsg == "{quit}":
        s.close()
        top.quit()

def onClosing(event=None):
    myMsg.set("{quit}")
    send()

top = tkinter.Tk()

top.title('Chattter')

messages_frame = tkinter.Frame(top)
myMsg = tkinter.StringVar()
myMsg.set('From: ')
myMsg2 = tkinter.StringVar()
myMsg2.set('To: ')

scrollbar = tkinter.Scrollbar(messages_frame)

msgList = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msgList.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msgList.pack()
messages_frame.pack()

entry = tkinter.Entry(top, textvariable=myMsg)
entrytwo = tkinter.Entry(top, textvariable=myMsg2)
entry.bind("<Return>", send)
entrytwo.bind("<Return>", send)
entry.pack()
entrytwo.pack()
sendButton = tkinter.Button(top, text="Send", command=send)
sendButton.pack()

fromLabel = tkinter.Label(entry, text='From: ')

top.protocol("WM_DELETE_WINDOW", onClosing)




host = "127.0.0.1"
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

receiveThread  = Thread(target=receive)
receiveThread.start()
tkinter.mainloop()