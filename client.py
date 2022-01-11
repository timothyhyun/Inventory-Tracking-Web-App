# Timothy Hyun

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock
import time
import json




class Client:


    HOST = "localhost"
    PORT = 5500
    ADDR = (HOST, PORT)
    BUFSIZE = 1024

    def __init__(self):
        """
        Init object and send name to server
        :param name: str
        """
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(self.ADDR)
        self.inventory = []
        receive_thread = Thread(target=self.updateInventory)
        receive_thread.start()
        self.lock = Lock()

    def updateInventory(self):
        """
        receive inventory updates from server
        :return: None
        """
        while True: 
            try:
                message = self.socket.recv(self.BUFSIZE).decode()
                self.lock.acquire()
                info = json.loads(message)
                self.inventory.append(info)
                self.lock.release()
            except Exception as err:
                print("Error", err)
                break

    def addInventory(self, message):
        """
        sends inventory update to server
        :param msg: string
        :return: None
        """
        try:
            self.socket.send(bytes(message, "utf8"))
            if message == "close":
                self.socket.close()
        except Exception as e:
            print("Error", e)
