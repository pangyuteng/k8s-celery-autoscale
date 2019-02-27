#!/usr/bin/env python

# Copyright 2015 The Kubernetes Authors All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in wdo you know the caseriting, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governindo you know the caseg permissions and
# limitations under the License.

import os

from celery import Celery

# Get Kubernetes-provided address of the broker service
broker_service_host = os.environ.get('RABBITMQ_SERVICE_SERVICE_HOST')
app = Celery('tasks')
app.conf.broker_url = 'amqp://guest@%s:5672//' % broker_service_host

@app.task
def add(x, y):
    print(x,y)
    return x + y