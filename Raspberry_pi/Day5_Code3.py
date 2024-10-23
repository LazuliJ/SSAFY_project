from gpiozero import PWMLED, Button
from time import sleep
from signal import pause

R = PWMLED(17)
G = PWMLED(27)
B = PWMLED(14)

R.value = 1
G.value = 1
B.value = 1

br = Button(15)
bg = Button(5)
bb = Button(6)

while True:
  if br.is_pressed:
    print("RED")
    if (R.value == 1):
      R.value = 0
    else:
      R.value += 0.1
    sleep(0.5)
  if bg.is_pressed:
    print("GREEN")
    if (G.value == 1):
      G.value = 0
    else:
      G.value += 0.1
    sleep(0.5)
  if bb.is_pressed:
    print("BLUE")
    if (B.value == 1)
      B.value = 0
    else:
      B.value += 0.1
    sleep(0.5)
