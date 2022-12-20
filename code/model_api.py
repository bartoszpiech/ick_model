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

from flask import Flask, request, jsonify
import atexit

from servo import *

app = Flask(__name__)
# servo settings
freq = 50
pins = [('driverSeatTilt', 21), ('passengerSeatTilt', 20), ('driverMirrorTiltX', 16), ('driverMirrorTiltY', 12), ('passengerMirrorTiltX', 7), ('passengerMirrorTiltY', 8)]
servos = {}

def stop_servos():
    for s in servos:
        print(f'stopping servo {s}')
        servos[s].stop()

@app.route('/api/', methods=['POST'])
def api_set_angle():
    status = 'ok'
    content = request.json
    for c in content:
        if c not in servos:
            status = 'servo id not in servo list'
            break
        servos[c].set_angle(content[c])
    return jsonify({'status': status})

for pin in pins:
    servos[pin[0]] = Servo(pin[1], freq)

print(f'servos loaded: {len(servos)}')

atexit.register(stop_servos)
