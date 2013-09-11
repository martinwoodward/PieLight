#!/usr/bin/python3
from time import sleep
from random import randint, random
import pifacecommon
import pifacedigitalio

DELAY = 0.05  # seconds

try:
    pifacedigitalio.init()
    pifacedigital = pifacedigitalio.PiFaceDigital()
    while True:
        pifacedigital.leds[randint(2, 7)].toggle()
        sleep(DELAY)    
        
except (KeyboardInterrupt):
    pifacedigitalio.deinit()
