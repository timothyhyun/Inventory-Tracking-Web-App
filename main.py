from flask import Flask, render_template, url_for, redirect, request, session, jsonify
from client import Client
from threading import Thread
import time


client = None
inventory = []

id = 0
app = Flask(__name__)
app.secret_key = "secret_key"
key = "id"


def disconnect_client():
    global client
    if client:
        client.addInventory("close")



def background():
    global inventory
    run = True
    while run:
        time.sleep(0.1)
        if key not in session:
            disconnect_client()
            break
        if not client:
            continue
        inventory = client.getInventory()
        for item in inventory:
            if item == "close":
                run = False
                break



@app.route("/home")
@app.route("/", methods=["POST","GET"])
def index():
    global client
    global id
    if key not in session:
        disconnect_client()
        if request.method == "POST":
            session[key] = id
            id += 1
        else:
            redirect(url_for("home"))
    client = Client()
    return render_template("index.html")

if __name__ == "__main__":
    Thread(target=background).start()
    app.run(debug=True)