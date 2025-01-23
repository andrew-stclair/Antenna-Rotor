"""Boot function for the Antenna Rotor Controller"""
from machine import Pin
from lib.Servo import Servo

servo = Servo(Pin(0), 10922.5, 54612.5, 180)
