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
import numpy as np
import time

class Servo:
    def __init__(self, pin: int, freq: int):
        self.pin = pin
        self.freq = freq    # frequency
        self.duty = 0       # duty cycle
        self.min_duty = 1.44
        self.max_duty = 12.63   # TODO: angle reaches > 180deg, lower max duty cycle or smth
        self.angle = 0      # angle in degrees
        self.min_angle = 0
        self.max_angle = 180
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin, self.freq)
        self.pwm.start(self.duty)

    def set_angle(self, angle: int):
        self.angle = angle
        self.duty = np.interp(self.angle, [self.min_angle, self.max_angle], [self.min_duty, self.max_duty])
        self.pwm.ChangeDutyCycle(self.duty)

    def stop(self):
        self.pwm.stop()
        GPIO.cleanup()
