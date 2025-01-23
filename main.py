"""Main function for the Antenna Rotor Controller"""
from time import sleep
from boot import servo
print("start")
sleep(2)

for i in range(0, 181, 45):
    print(i)
    servo.angle(i)
    sleep(1)

servo.angle(90)
sleep(2)

servo.angle(0)
sleep(2)
servo.angle(180)
sleep(2)
servo.angle(0)
sleep(2)
servo.angle(180)
sleep(2)
servo.angle(90)
sleep(2)
print("end")

servo.close()
