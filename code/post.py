#!/usr/bin/python

ip='ick-piechbart.pitunnel.com'
angle=0
import requests
res = requests.post(f'{ip}/api/', json={'driverSeatTilt': angle, 'passengerSeatTilt': angle, 'driverMirrorTiltX': angle, 'driverMirrorTiltY': angle, 'passengerMirrorTiltX': angle, 'passengerMirrorTiltY': angle})
if res.ok:
    print(res.json())
