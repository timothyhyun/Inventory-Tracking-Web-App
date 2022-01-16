import re
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
        print("disconnecting client")
        client.addInventory("close")


def background():
    global inventory
    run = True
    while run:
        time.sleep(0.1)
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
    if client == None:
        return "Error"
    name = request.args.get("name")
    quantity = request.args.get("quantity")
    sku = request.args.get("sku")
    comments = request.args.get("comments")
    try:
        if int(quantity) <= 0 or sku == "":
            # invalid input
            return "Error"
        inv = client.getInventory()
        for item in inv:
            if sku == item[1]:
                # invalid input
                return "Error"
        temp = [name, sku, quantity, comments]
        if client:
            print(temp)
            client.addInventory(json.dumps(temp)) 
        return "none"
    except Exception as err:
        print("Error", err)
        return "Error"


@app.route("/editInventory")
def edit_inventory():
    global client
    if client == None:
        return "Error"
    name = request.args.get("name")
    quantity = request.args.get("quantity")
    sku = request.args.get("sku")
    comments = request.args.get("comments")
    try:
        int(quantity)
    except Exception as err:
        print("Error", err)
        return "Error"
    if client.editInventory(name, sku, quantity, comments) == "Invalid Input":
        return "Error"
    return "none"

@app.route("/deleteInventory")
def delete_inventory():
    global client
    if client == None:
        return "Error"
    sku = request.args.get("sku")  
    if client.deleteInventory(sku) == "Invalid Input":
        return "Error"
    return "none"


# Name, Quantity, SKU, Comments

@app.route("/get_inventory")
def get_inventory():
    return jsonify({"inventory":inventory})


@app.route("/")
@app.route("/home")
def home():
    global client
    if key not in session:
        return redirect(url_for("log"))
    client = Client()
    return render_template("index.html")


@app.route("/log", methods=["POST","GET"])
def log():
    print(request.method)
    global id
    disconnect_client()
    session[key] = id
    id += 1
    return redirect(url_for("home"))
        
    
        



if __name__ == "__main__":
    Thread(target=background).start()
    app.run(debug=True)