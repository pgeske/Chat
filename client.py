import socket
import time
from threading import Thread, Condition, Lock

class InputManager(Thread):
    def __init__(self, lock):
        Thread.__init__(self)
        self.lock = lock;

    def run(self):
        while True:
            time.sleep(.01)
            with self.lock:
                message = raw_input("> ")
                sock.send(message)

class ResponseManager(Thread):
    def __init__(self, lock):
        Thread.__init__(self)
        self.lock = lock

    def run(self):
        while True:
            message = sock.recv(500)
            with self.lock:
                print message

HOST = "127.0.0.1"
PORT = 8801

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
sock.connect((HOST, PORT))


display_lock = Lock()
input_manager = InputManager(display_lock)
response_manager = ResponseManager(display_lock)
input_manager.start()
response_manager.start()
