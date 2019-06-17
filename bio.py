#Turn the stepper motor when the waste is bio
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control pins = [7,11,13,15]
for pin in control pins:
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, 0)
halfstep seq = [
[1,0,0,0],
[1,1,0,0],
[0,1,0,0],
[0,1,1,0],
[0,0,1,0],
[0,0,1,1],
[0,0,0,1],
[1,0,0,1]
]
for i in range(128):
for halfstep in range(8):
for pin in range(4):
GPIO.output(control pins[pin], halfstep seq[halfstep][pin])
time.sleep(0.001)
GPIO.cleanup()