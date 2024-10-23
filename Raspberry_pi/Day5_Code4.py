import gpiozero import LED, Button
from time import sleep

b1 = Button(14)
b2 = Button(27)

led = LED(17)
t = 0.001
cur = 0.001

while(1):
  led.on()
  sleep(cur)
  led.off()
  sleep(0.01-cur)

  if b1.is_pressed:
    if (cur < 0.009):
      print("up")
      cur+=t
    sleep(0.5)
  if b2.is_pressed:
    if (cur > 0.001):
      print("down")
      cur-=t
    sleep(0.5)
