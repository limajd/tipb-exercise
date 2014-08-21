import time
import numpy as num
from pyrocko import trace
from pyrocko.io import save

now = time.time()
ydata = num.random.random(1000) - 0.5

tr = [trace.Trace('', 'stat', '', 'N',
        deltat=0.1,
        tmin=now,
        ydata=ydata),
        trace.Trace('', 'stat', '', 'E',
        deltat=0.1,
        tmin=now,
        ydata=ydata)]

#tr.snuffle()
c=0
for t in tr:
	c=c+1
	save(tr,'/home/riccardo/projects/sources/misc/tipb-exercise/tmp_file_'+str(c)+".txt",'text')
