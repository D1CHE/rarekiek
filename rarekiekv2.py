#! /usr/bin/python

import time
from neopixel import *
import argparse
import json

# LED strip configuration:
LED_COUNT      = 9      # Number of LED pixels.
LED_PIN        = 10      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def update_leds(strip, data):
    
    #print(data["1_locomotief"])
    #print(data["1_station"])
    #print(data["2_paleis"])
    #print(data["2_boom"])
    #print(data["3_kachel"])
    #print(data["3_model"])
    #print(data["4_vincent"])
    #print(data["5_raam"])
    #print(data["5_stoom"])
        
    c1 = Color(data["1_locomotief"][1], data["1_locomotief"][0], data["1_locomotief"][2])
    c2 = Color(data["1_station"][1], data["1_station"][0], data["1_station"][2])
    c3 = Color(data["2_paleis"][1], data["2_paleis"][0], data["2_paleis"][2])
    c4 = Color(data["2_boom"][1], data["2_boom"][0], data["2_boom"][2])
    c5 = Color(data["3_kachel"][1], data["3_kachel"][0], data["3_kachel"][2])
    c6 = Color(data["3_model"][1], data["3_model"][0], data["3_model"][2])
    c7 = Color(data["4_vincent"][1], data["4_vincent"][0], data["4_vincent"][2])
    c8 = Color(data["5_raam"][1], data["5_raam"][0], data["5_raam"][2])
    c9 = Color(data["5_stoom"][1], data["5_stoom"][0], data["5_stoom"][2])
    
    strip.setPixelColor(0, c1)
    strip.setPixelColor(1, c2)
    strip.setPixelColor(2, c3)
    strip.setPixelColor(3, c4)
    strip.setPixelColor(4, c5)
    strip.setPixelColor(5, c6)
    strip.setPixelColor(6, c7)
    strip.setPixelColor(7, c8)
    strip.setPixelColor(8, c9)
    
    strip.show()
        
def update_audio(data):
    
    audio_state = data["audio"]

def main():
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    
    # Audio setup
    
    while True:
        try:
            with open("/home/pi/Desktop/rarekiek/leds.json", "r") as f:
                d = json.load(f)
        except:
            continue
        
        update_leds(strip, d)
        #update_audio(d)

if __name__ == "__main__":
    main()