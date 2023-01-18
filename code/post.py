#!/usr/bin/python

import requests

ip='https://lsumikb-piechbart.pitunnel.com'
angle=180
res = requests.post(f'{ip}/api/', json={'driverSeatTilt': angle, 'passengerSeatTilt': angle, 'driverMirrorTiltX': angle, 'driverMirrorTiltY': angle, 'passengerMirrorTiltX': angle, 'passengerMirrorTiltY': angle})
if res.ok:
    print(res.json())
