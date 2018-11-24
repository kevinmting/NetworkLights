import requests
import time

from common import RgbColor

#these will only work on the RPi since they are only installed on that.
try:
    from neopixel import ws, Adafruit_NeoPixel, Color
except ImportError:
    pass


light_cmd = RgbColor()


def get_color():
    # get latest setting from MASTER
    response = requests.get('http://192.168.86.25:5000/color')
    response.raise_for_status()
    new_light_setting = response.json()
    print('new setting from Master %s' % (new_light_setting))

    # update locally stored setting
    light_cmd.r = new_light_setting['r']
    light_cmd.g = new_light_setting['g']
    light_cmd.b = new_light_setting['b']
    light_cmd.w = new_light_setting['w']



def rpi_update_LEDS(strip, pixel):
    new_color = Color(light_cmd.b, light_cmd.g, light_cmd.r, light_cmd.w)
    strip.setPixelColor(pixel, new_color)
    strip.show()
    print('LEDs updated')

def rpi_setup():


    # LED strip configuration:
    LED_COUNT = 1  # Number of LED pixels.
    LED_PIN = 18  # GPIO pin connected to the pixels (must support PWM!).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10  # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False  # True to invert the signal (when using NPN transistor level shi$
    LED_CHANNEL = 0
    LED_STRIP = ws.SK6812_STRIP_BGRW

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL,
                              LED_STRIP)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    return strip


def run(rpi):
    #setup if using RPi
    if rpi:
        strip = rpi_setup()
        led_pixel = 0 #currently using one LED, but can use multiple


    while True:
        start_time = time.time()
        get_color()

        #if using RPi, actually update real leds
        if rpi:
            rpi_update_LEDS(strip, led_pixel)

        elapsed_time = time.time() - start_time
        print(elapsed_time)

