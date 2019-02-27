#!/usr/bin/env python

# Copyright 2015 The Kubernetes Authors All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
    #break
    #res = add.delay(x, y)
    #time.sleep(5)
    #if res.ready():
    #    res.get()
print('yolo6')