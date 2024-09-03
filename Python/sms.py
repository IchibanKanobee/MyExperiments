import json
import os
import time, threading


import smtplib

my_path = os.path.abspath(os.path.dirname(__file__))
settings_file_name = os.path.join(my_path, "../pyfin/utils/security/settings.json")
with open(settings_file_name) as json_file:
    settings = json.load(json_file)


server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( settings["email"], settings["email_password"])
#insert blank line for semicolon https://stackoverflow.com/questions/7294885/python-emailing-use-of-colon-causes-no-output
message = "\nHello 2:32"
server.sendmail('Markets Data Intelligence', '4168733699@msg.telus.com', message)


