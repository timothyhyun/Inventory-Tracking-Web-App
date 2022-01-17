# Inventory-Tracking-Web-App
Shopify Summer 2022 Backend Project


## Background: 

This an inventory app that allows users to track items using flask
Users can add, edit and delete items, and save all inventory to a csv file

I used threading and sockets to allow multiple users to use the app simulatenously. 

## Setup:

Ensure Python 3.6+ is installed on the device. 
To clear all previous inventory data, clear the inventory.json file

```bash
pip install -r requirements.txt
```

## Execution: 
```bash 
py server.py &
py main.py
```
Go to http://localhost:5000

## Optional: 

To access the program from another device, change hostname in server.py to '' and in client.py to the device's private IP address
