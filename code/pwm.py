#!/usr/bin/python

# Copyright (c) 2022 Bartosz Piech, Politechnika Wrocławska / Wrocław
# University of Science and Technology
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import RPi.GPIO as GPIO
import time

# connected pwm servo pin
pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

serwo = GPIO.PWM(pin, 50)   # 50Hz PWM frequency
wypelnienie_serwo = 0       # starting position
serwo.start(wypelnienie_serwo)

try:
    while True:
        print(f'wypelnienie: {wypelnienie_serwo}')
        wypelnienie_serwo += 0.1
        if wypelnienie_serwo > 13:  # tested experimentally when servo reaches it's limits
            wypelnienie_serwo = 0   # reset
        serwo.ChangeDutyCycle(wypelnienie_serwo)
        time.sleep(0.05)            # time delay
except KeyboardInterrupt:
    print('Koniec')

serwo.stop()
GPIO.cleanup()
