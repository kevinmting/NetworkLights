import requests
import time

from common import RgbColor


light_cmd = RgbColor()


def get_color():
    # get latest setting from MASTER
    response = requests.get('http://127.0.0.1:5000/color')
    response.raise_for_status()
    new_light_setting = response.json()
    print(f'new setting from Master {new_light_setting}')

    # update locally stored setting
    light_cmd.r = new_light_setting['r']
    light_cmd.g = new_light_setting['g']
    light_cmd.b = new_light_setting['b']

    update_LEDS()


def update_LEDS():
    print('LEDs updated')


def run():
    while True:
        start_time = time.time()
        get_color()
        elapsed_time = time.time() - start_time
        print(elapsed_time)
