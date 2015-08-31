import time
def timecall (fn):
    "Call function and return elapsed time."
    t0 = time.clock()
    fn()
    t1 = time.clock()
    return t1-t0
