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
import pigpio
import numpy as np
import time

class Servo:
    def __init__(self, pin: int, freq: int):
        self.pin = pin
        self.freq = freq    # frequency
        self.pw = 0
        self.min_pw = 500
        self.max_pw = 2500  # TODO: angle reaches > 180deg, lower max duty cycle or smth
        self.angle = 0      # angle in degrees
        self.min_angle = 0
        self.max_angle = 180
        self.pwm = pigpio.pi()
        self.pwm.set_mode(pin, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(pin, freq)

    def set_angle(self, angle: int):
        self.angle = angle
        self.pw = np.interp(self.angle, [self.min_angle, self.max_angle], [self.max_pw, self.min_pw])
        self.pwm.set_servo_pulsewidth(self.pin, self.pw)

    def stop(self):
        self.pwm.set_PWM_dutycycle(self.pin, 0)
        self.pwm.set_PWM_frequency(self.pin, 0)
