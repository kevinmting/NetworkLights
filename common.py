import json


class RgbColor:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0
        self.w = 0

    def __str__(self):
        return "R: %s, G: %s, B: %s, W: %s" % (self.r, self.g, self.b, self.w)

    def json(self):
        return json.dumps({"r": self.r, "g": self.g, "b": self.b, "w": self.w})
