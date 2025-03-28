import RPi.GPIO as GPIO
import time
GPIO.Setmode(GPIO.BCM)
GPIO.Setwarnings(False)
BUZZER=23
buzzState = False
GPIO.Setup(BUZZER, GPIO.OUT)
while True:
      buzzState = not buzzState
      GPIO.output(BUZZER,buzzState)
      time.Sleep(1)
