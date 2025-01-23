from machine import Pin, PWM

# MAX = 54612.5
# MIN = 10922.5
# DEG = 180
class Servo:
    """Hacked together servo driver using PWM"""

    def __init__(self, pin: Pin, min_duty: float, max_duty: float, degrees: int):
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.degrees = degrees
        self.servo = PWM(pin, freq=333, duty_u16=int(min_duty+((degrees/2)*(max_duty-min_duty)/degrees)))

    def angle(self, degrees):
        """Set the servo to this position in degrees"""
        multiple = (self.max_duty-self.min_duty)/self.degrees
        self.servo.duty_u16(int(self.min_duty+(degrees*multiple)))

    def close(self):
        """Close this object"""
        self.servo.deinit()
        del self.min_duty
        del self.max_duty
        del self.degrees
        del self.servo
        del self
