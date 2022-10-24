#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

serwo = GPIO.PWM(pin, 50)
wypelnienie_serwo = 0
serwo.start(wypelnienie_serwo)

try:
    while True:
        print(f'wypelnienie: {wypelnienie_serwo}')
        wypelnienie_serwo += 0.1
        if wypelnienie_serwo > 13:
            wypelnienie_serwo = 0
        serwo.ChangeDutyCycle(wypelnienie_serwo)
        time.sleep(0.05)
except KeyboardInterrupt:
    print('Koniec')

serwo.stop()
GPIO.cleanup()
