from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
while True:
    north = sense.get_compass()
    print("North: %s" %north)
    sleep(0.1)

