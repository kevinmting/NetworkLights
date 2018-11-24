import json

class RgbColor:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

    def __str__(self):
        return f"R: {self.r}, G: {self.g}, B: {self.b}"

    def json(self):
        return json.dumps({"r":self.r,"g":self.g,"b":self.b})