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

# imports
from flask import Flask
from servo import *

# create flask app
app = Flask(__name__)

# to set servo0 to 90deg just send this api call \/
#                                       localhost:5000/api/0/90

@app.route('/api/<int:servo_id>/<int:angle>')
def api_set_angle(servo_id: int, angle: int):
    status = 'ok'               # normally ok
    if servo_id > len(servos):  # error
        status = 'servo id not in our servo list'
    current_servo = servos[servo_id]
    current_servo.set_angle(angle)
    return {'status': status}

# servo settings
pin = 21
freq = 50
s = Servo(pin, freq)

# add s to servo list with id 0
servos = []
servos.append(s)
