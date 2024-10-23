from gpiozero import PWMLED
from time import sleep

led = PWMLED(14)
led.value = 1

while True:
  mesg = input(">> ")
  if (mesg == "1"):
    if (led.value != 1):
      led.value += 0.1
      sleep(0.5)
  elif (mesg == "2"):
    if (led.value != 0):
      led.value -= 0.1
      sleep(0.5)
