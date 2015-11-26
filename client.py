import socket
import curses
import time
import os
from threading import Thread, Condition, Lock

#Threads
class InputManager(Thread):
    def __init__(self, window, name):
        Thread.__init__(self)
        self.window = window
        self.name = name

    def run(self):
        while True:
            self.window.move(2,5)
            self.window.addstr("> ")
            message = self.window.getstr()
            #Append handle to message
            message = "[" + username + "]: " + message
            self.window.erase()
            self.window.border(0)
            self.window.refresh()
            sock.send(message)

class ResponseManager(Thread):
    def __init__(self, window):
        Thread.__init__(self)
        self.window = window
        self.line = 1

    def run(self):
        while True:
            message = sock.recv(500)
            self.window.border(0)
            try:
                self.window.move(self.line,5)
            except:
                self.window.move(1,5)
            self.window.addstr("> ")
            self.window.addstr(message)
            self.window.refresh()
            self.line += 1

HOST = "192.168.1.5"
#HOST = "104.229.212.48"
PORT = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sock.connect((HOST, PORT))
username = raw_input("Enter a username: ")

#Create input window
stdscr = curses.initscr()
input_window = curses.newwin(5, 400, 0, 0)
input_window.border(0)
input_window.refresh()
#Create messages window
messsage_window = curses.newwin(50, 400, 5, 0)
messsage_window.border(0)
messsage_window.refresh()
messsage_window.refresh()

input_manager = InputManager(input_window, username)
response_manager = ResponseManager(messsage_window)
input_manager.start()
response_manager.start()
sock.send(username + " joined the chat.")
