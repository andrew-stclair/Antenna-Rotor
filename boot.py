"""Boot function for the Antenna Rotor Controller"""

from machine import Pin
from machine import UART

from lib.Servo import Servo

# Initialize the USB Serial device for commands
uart = UART(0, 115200)
uart.init(115200, bits=8, parity=None, stop=1)
uart.write("UART Initialized\n")

# Initialize the elevation servo
elevation = Servo(Pin(0), 10922.5, 54612.5, 180)

