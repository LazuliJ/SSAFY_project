from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
while True:
    ori = sense.get_orientation_degrees()
    x = ori['pitch']
    y = ori['roll']
    z = ori['yaw']
    print(f"Degree : X: {x}, Y: {y}, Z: {z} ")
    sleep(0.1)
