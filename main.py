from flask import Flask, render_template, url_for, redirect, request, session, jsonify
from client import Client
from threading import Thread
import time
import json

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
        inv = client.getInventory()
        for item in inv:
            if item == "close":
                run = False
                break
        inventory = inv


#base off SKU number

@app.route("/addInventory")
def add_inventory():
    global client
    date = ""
    quantity = 0
    sku = ""
    comments = ""
    if quantity <= 0 or sku < 0:
        # invalid input
        return
    inv = client.getInventory()
    for item in inv:
        if sku == item[1]:
            # invalid input
            return
    temp = [date, sku, quantity, comments]
    client.addInventory(json.dumps(temp)) 

@app.route("/editInventory")
def edit_inventory():
    global client
    date = ""
    quantity = 0
    sku = ""
    comments = ""
    if client.editInventory(date, sku, quantity, comments) == "Invalid Input":
        pass

@app.route("/deleteInventory")
def delete_inventory():
    global client
    sku = ""    
    if client.deleteInventory(sku) == "Invalid Input":
        pass


# Date, Name, Quantity, SKU, Comments


def get_inventory():
    pass


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