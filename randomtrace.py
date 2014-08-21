import time
import numpy as num
from pyrocko import trace
from pyrocko.io import save


now = time.time()
ydata = num.random.random(1000) - 0.5

tr = [trace.Trace('', 'sta1', '', 'N',
        deltat=0.1,
        tmin=now,
        ydata=ydata),
        trace.Trace('', 'sta2', '', 'E',
        deltat=0.1,
        tmin=now,
        ydata=ydata)]

trace.snuffle(tr)

c=0
for t in tr:
	c=c+1
	save(tr,'/home/djamil/Workspace/Python/Course-Boot-Camp/git/tipb-exercise/tmp_file_'+str(c)+".txt",'text')
