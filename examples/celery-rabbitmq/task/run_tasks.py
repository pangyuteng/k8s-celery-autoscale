import random
import syslog
import time
print('yolo4')
from celery_conf import add
import celeryconfig
print('yolo5')
while True:
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    print('hola!!!',time.time())
    add.apply_async(args=(x, y))
    print('laho!!!',time.time(),celeryconfig.CELERY_BROKER_URL)
    time.sleep(10)
    #break
    #res = add.delay(x, y)
    #time.sleep(5)
    #if res.ready():
    #    res.get()
print('yolo6')