# Inventory-Tracking-Web-App



## Background: 

This an inventory app that allows users to track items using flask
Users can add, edit and delete items, and save all inventory to a csv file

I used threading and sockets to allow multiple users to use the app simulatenously. 

## Setup:

Ensure Python 3.6+ is installed on the device. 

Clone and Navigate to the Repository

```bash
pip install -r requirements.txt
```

## Execution: 
You will need to run these files in seperate shells. Server.py runs the server that communicates with all the clients. main.py runs the website that processes user requests
```bash 
py server.py
py main.py
```
Go to http://localhost:5000


## Optional: 

To clear all previous inventory data, clear the inventory.json file
To access the program from another device, change hostname in server.py to '' and in client.py to the device's private IP address
