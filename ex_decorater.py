from time import time
def deco(fn):
    def warrper(*args,**kargs):
        t1 = time()
        result = fn(*args,**kargs)
        t2 = time()
        print(f'took {t2 - t1} second')
        return result
    return warrper

@deco
def measer():
    for i in range(100000000):
        i*5
measer()        