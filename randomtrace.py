import time
import numpy as num
from pyrocko import trace

now = time.time()
ydata = num.random.random(1000) - 0.5

tr = trace.Trace('', 'stationname', '', 'channelname',
        deltat=0.1,
        tmin=now,
        ydata=ydata)

tr.snuffle()
