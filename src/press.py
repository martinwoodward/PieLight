#!/usr/bin/python3
import pifacecommon
import pifacedigitalio


def switch_pressed(event):
    global pifacedigital
    pifacedigital.output_pins[3 - event.pin_num].toggle()


if __name__ == "__main__":
    pifacedigitalio.init()

    global pifacedigital
    pifacedigital = pifacedigitalio.PiFaceDigital()

    listener = pifacedigitalio.InputEventListener()
    for i in range(4):
        listener.register(i, pifacedigitalio.IODIR_ON, switch_pressed)
    listener.activate()
