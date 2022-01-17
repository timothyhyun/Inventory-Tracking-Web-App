# Timothy Hyun

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread, Lock
import json
from werkzeug.datastructures import RequestCacheControl

from werkzeug.utils import invalidate_cached_property


class Client:
    #self.inventory: list of lists
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
        # loads inventory from stored json file
        self.lock = Lock()
        self.lock.acquire()
        jsonFile = open("inventory.json", "r")
        jsonContent = jsonFile.read()
        res = json.loads(jsonContent)
        jsonFile.close()
        self.inventory = res
        self.lock.release()
        # continously updates inventory by receiving requests
        receive_thread = Thread(target=self.updateInventory)
        receive_thread.start()
        

    def updateInventory(self):
        """
        receive inventory updates from server
        :return: None
        """
        while True: 
            try:
                message = self.socket.recv(self.BUFSIZE).decode()
                # updates inventory based after receiving request
                if message[:4] == "edit":
                    index = message[4]
                    info = json.loads(message[5:])
                    self.lock.acquire()
                    self.inventory[int(index)] = info
                    self.lock.release()
                elif message[:6] == "delete":
                    index = message[6]
                    self.lock.acquire()
                    self.inventory.pop(int(index))
                    self.lock.release()
                else:
                    self.lock.acquire()
                    info = json.loads(message)
                    self.inventory.append(info)
                    self.lock.release()
                self.lock.acquire()
                # updates json file
                jsonString = json.dumps(self.inventory)
                jsonFile = open("inventory.json", "w")
                jsonFile.truncate()
                jsonFile.write(jsonString)
                jsonFile.close()
                self.lock.release()
            except Exception as err:
                print("Receiving Error", err)
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
    
    def getInventory(self):
        """
        gets total inventory 
        :return: list of list
        """
        return self.inventory

    def editInventory(self, name, sku, quantity, comments):
        """
        sends message to edit inventory with updated items
        :param data, sky, quantity, comments: str
        :return: status of the inputs
        """
        if int(quantity) < 0:
            return "Invalid Input"
        inv = self.getInventory()
        for i in range(len(inv)):
            if inv[i][1] == sku:
                # determine which fields to change
                l = []
                if name == "":
                    l.append(inv[i][0])
                else:
                    l.append(name)
                l.append(sku)
                if quantity == "":
                    l.append(inv[i][2])
                else:
                    try:
                        l.append(int(quantity))
                    except:
                        return "Invalid Input"
                if comments == "":
                    l.append(inv[i][3])
                else:
                    l.append(comments)
                temp = json.dumps(l)
                self.socket.send(bytes(f"edit{i}"+temp, "utf8"))
                return " "
        return "Invalid Input"
        
    
    def deleteInventory (self, sku):
        """
        sends inventory update to server
        :param sku:str
        :return: 
        """
        inv = self.getInventory()
        for i in range(len(inv)):
            if inv[i][1] == sku:
                self.socket.send(bytes(f"delete{i}", "utf8"))
                return " "
        return "Invalid Input"