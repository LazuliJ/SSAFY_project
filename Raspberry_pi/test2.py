from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    accel = sense.get_accelerometer()
    x = accel['pitch']
    y = accel['roll']
    z = accel['yaw']
    print(f"Accel - X: {x}, Y: {y}, Z: {z}")
    sleep(0.1)
