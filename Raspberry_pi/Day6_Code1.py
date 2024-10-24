from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
    humid = sense.get_humidity()
    temp = sense.get_temperature()

    print("Humidity(%) : ", humid)
    print("Temperature(oC) : ", temp)
    sleep(1)
