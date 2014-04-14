# -*- coding: utf-8 -*-


# Файл mytimer.py

import time
reps = 1000
repslist = range(reps)

def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs,**kargs)
    elapsed = time.clock() - start
    return(elapsed, ret)

if __name__ == '__main__':
