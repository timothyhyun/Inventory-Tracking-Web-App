from flask import Flask, render_template, url_for, redirect, request, session, jsonify
from client import Client
from threading import Thread
import time


