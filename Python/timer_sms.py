import sys
#sys.path.append("../..")

import json
import os
import numpy as np
import time, threading
import random


import smtplib

stop_event = threading.Event()
limit_event = threading.Event()

def start_monitor(server, symbol, stop_price, limit_price, email, password):
    timer = threading.Timer(10, start_monitor, [server, symbol, stop_price, limit_price, email, password])
    timer.start()
    
    price = random.uniform(0, 9)
    message = "Symbol " + symbol + " reached price " + str(price)
    
    print (message)
    if not stop_event.is_set():
        if (price <= stop_price):
            message = "Symbol " + symbol + " reached stop price " + str(price)
            server.sendmail('Markets Data Intelligence', '4168733699@msg.telus.com', message)
            stop_event.set()
    elif stop_event.is_set() and not limit_event.is_set():
        if (price <= limit_price):
            message = "Symbol " + symbol + " reached limit price " + str(price)
            server.sendmail('Markets Data Intelligence', '4168733699@msg.telus.com', message)
            limit_event.set()
    elif stop_event.is_set() and limit_event.is_set():
        print ("Exiting the app")
        timer.cancel()
        timer.join()


my_path = os.path.abspath(os.path.dirname(__file__))
settings_file_name = os.path.join(my_path, "../pyfin/utils/security/settings.json")
with open(settings_file_name) as json_file:
    settings = json.load(json_file)


stop_price = 4
limit_price = 3
symbol = "TQQQ"
print ("Started monitoring for stop price " + str(stop_price))
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( settings["email"], settings["email_password"])

start_monitor(server, symbol, stop_price, limit_price, settings["email"], settings["email_password"])
