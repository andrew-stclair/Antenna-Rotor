"""Main function for the Antenna Rotor Controller"""

from time import sleep

from boot import elevation
print("start")
sleep(2)


for i in range(0, 181, 45):
    print(i)
    elevation.angle(i)

    sleep(1)

elevation.angle(90)
sleep(2)

elevation.angle(0)
sleep(2)
elevation.angle(180)
sleep(2)
elevation.angle(0)
sleep(2)
elevation.angle(180)
sleep(2)
elevation.angle(90)
sleep(2)

print("end")

elevation.close()
