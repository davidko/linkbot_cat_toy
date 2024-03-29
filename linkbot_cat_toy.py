#!/usr/bin/env python
# Program generated by BaroboLink
from barobo.linkbot import *
import time
import math
linkbot1 = Linkbot()
linkbot1.connect()
curtime = 0.0
while True:
    # Move the arm of the toy in a circular fashion, tracing a cone in space
    j1pos = 5 + 15 * math.sin(4 * curtime)
    j2pos = 158 + 15 * math.cos(4 * curtime)
    linkbot1.driveJointToNB(1, j1pos)
    linkbot1.driveJointToNB(2, j2pos)
    curtime = curtime + 0.1
    time.sleep(0.05)
