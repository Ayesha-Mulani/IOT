import RPi.GPIO as GPIO
import time
GPIO.Setwarnings(False)
GPIO.Setmode(GPIO.BCM)
GPIO.Setup(4,GPIO.OUT)
while True:
      GPIO.output(4,GPIO.HIGH)
      time.sleep(3)
      GPIO.output(4,GPIO.LOW)
      time.sleep(3)
