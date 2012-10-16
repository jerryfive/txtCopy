import os
import time

while True:
    fname=time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.txt'
    if os.path.exists(fname):
        print "Error:'%s' already exists" %fname
    else:
        break


fobj=open(fname,'w')
fobj.close()

