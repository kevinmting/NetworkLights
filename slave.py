from flask import Flask
from flask import request

class RgbColor:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

    def __str__(self):
        return f"R: {self.r}, G: {self.g}, B: {self.b}"


app = Flask(__name__)
light = RgbColor()

@app.route("/")
def hello():
    return "slave root path hello"

@app.route("/color", methods=["GET","POST"])
def color():
    if request.method == "GET":
        return str(light)
    elif request.method == "POST":
        light.r = request.json["r"]
        light.g = request.json["g"]
        light.b = request.json["b"]
        return ""

