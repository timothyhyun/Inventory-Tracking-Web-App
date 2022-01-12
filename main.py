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




@app.route("/", methods=["POST","GET"])
def index():
    global client
    if key not in session:
        pass
    else:
        return render_template("index.html")

#somehow create background task, if id not in session, close socket
#not sure hwo to do 