from gpiozero import PWMLED, RotaryEncoder, Button
from signal import pause

rotor = RotaryEncoder(15, 18, wrap=True, max_steps=180)
rotor.steps = -180
rot_btn = Button(14)

led1 = PWMLED(17)
led2 = PWMLED(27)
led3 = PWMLED(22)

def change_rot():
  print(rotor.steps)
  if (rotor.steps >= -180 and rotor.steps<=-60):
    led1.value = (180+rotor.steps)/120
  elif (rotor.steps >= -60 and rotor.steps<=60):
    led2.value = (60+rotor.steps)/120
  elif (rotor.steps >= 60 and rotor.steps<=180):
    led3.value = (rotor.steps-60)/120

def click_btn():
  print("OFF")
  led1.value = 0
  led2.value = 0
  led3.value = 0

rotor.when_rotated = change_rot
rot_btn.when_pressed = click_btn
pause()
