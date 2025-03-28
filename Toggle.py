import RPi.GPIO as GPIO
import time
GPIO.Setmode(GPIO.BCM)
LED1_PIN = 17
LED2_PIN = 27
GPIO.Setup(LED1_PIN, GPIO.OUT)
GPIO.Setup(LED2_PIN, GPIO.OUT)
try:
   while True :
         GPIO.output(LED1_PIN, GPIO.HIGH)
         GPIO.output(LED2_PIN, GPIO.LOW)
         Print("LED1 ON, LED2 OFF")
         time.sleep(1)
except keyboardInterrupt :
      GPIO.Cleanup()
      print("Paogram exited cleanly")
