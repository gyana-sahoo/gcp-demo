# The Docker image contains the following code to demo for Seiza.ai
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h1 style='text-align:center;margin:20px;'>Greetings to everyone at Shiza.ai in this training </h1>  <BR> <h2> <p><a href=\"sample-homepage.html\">click here</a></p> </h2>"
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)
  