from threading import Lock, Thread
import time

from flask import request, Flask

from common import RgbColor


app = Flask(__name__)
light_cmd_lock = Lock()
light_cmd = RgbColor()
UPDATE_FREQ_HZ = 30


@app.route("/", methods=["GET"])
def check_if_alive():
    return 'server is up :)'


@app.route("/color", methods=["GET","PUT"])
def color():
    if request.method == "GET":
        with light_cmd_lock:
            light_cmd_copy = light_cmd
        return light_cmd_copy.json()
    elif request.method == "PUT":
        with light_cmd_lock:
            light_cmd.r = request.json["r"]
            light_cmd.g = request.json["g"]
            light_cmd.b = request.json["b"]
            light_cmd.w = request.json["w"]
        return ""


def run_server():
    app.run(host="0.0.0.0")


def generate_commands():
    step_sz = 25
    while True:
        for r in range(0, 256, step_sz):
            for g in range(0, 256, step_sz):
                for b in range(0, 256, step_sz):
                    with light_cmd_lock:
                        #set color
                        light_cmd.r = r
                        light_cmd.g = g
                        light_cmd.b = b
                    time.sleep(1/UPDATE_FREQ_HZ)


def run():
    # start web server
    server_thread = Thread(target=run_server)
    server_thread.start()

    # generate LED commands
    command_thread = Thread(target=generate_commands)
    command_thread.start()
    server_thread.join()
