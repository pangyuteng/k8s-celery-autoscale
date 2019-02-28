#!/usr/bin/env python

import os
import celeryconfig

from multiprocessing import Pool
from multiprocessing import cpu_count
VAL = 5000

def f(x):
    for _ in range(VAL):
        x*x    

from celery import Celery
print('yolo1')
app = Celery('tasks')
app.config_from_object(celeryconfig)
print('!!',app.conf.broker_url)

print('yolo2')
@app.task
def add(x, y):
    print(x,y)
    #processes = cpu_count()
    #pool = Pool(processes)
    #pool.map(f, range(VAL))
    return x + y
print('yolo3')