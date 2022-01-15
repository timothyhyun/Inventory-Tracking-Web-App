# Timothy Hyun

# Imports
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time



# Global Constants
HOST = "localhost"
PORT = 5500
ADDR = (HOST, PORT)
MAX_CONNETIONS = 10
BUFSIZE = 1024

# Global Variables
clients = []
server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDR)


def send_message(message):
    """
    Send a message to all connected clients
    :param message: bytes (utf8)
    :return: None
    """
    for client in clients:
        cli, addr = client
        try:
            cli.send(message)
        except Exception as err:
            print("Error", err)

def communicate(client, addr):
    """
    Thread to handle inventory inputs from client
    :param client: socket object
    :param addr: address
    :return: None
    """
    while True:
        try:
            message = client.recv(BUFSIZE)
            if (message == bytes("close", "utf8")):
                client.close()
                clients.remove((client, addr))
                print("A client has disconnected")
                break
            else:
                send_message(message)
                print("Message Sent:", message.decode("utf8"))
        except Exception as err:
            print("Error", err)
            break



def connect():
    """
    Wait for connecton from new clients, start new thread once connected
    :return: None
    """

    while True:
        try: 
            client, addr = server.accept()
            clients.append((client, addr))
            print(f"{addr} connected to server at {time.time()}")
            Thread(target=communicate, args=(client, addr)).start()
        except Exception as err:
            print("Error", err)
            break


def main():
    server.listen(MAX_CONNETIONS)
    print("Waiting for Connections...")
    accept = Thread(target=connect)
    accept.start()
    accept.join()
    server.close()




if __name__ == "__main__":
    main()