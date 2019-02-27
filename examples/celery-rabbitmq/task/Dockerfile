#FROM library/celery
FROM python:3.6.6

ADD requirements.txt /data/requirements.txt
RUN pip install --user --upgrade pip
RUN python -m pip install --user -r /data/requirements.txt

ADD celery_conf.py /data/celery_conf.py
ADD celeryconfig.py /data/celeryconfig.py
ADD run_tasks.py /data/run_tasks.py
ADD run.sh /usr/local/bin/run.sh

ENV C_FORCE_ROOT 1

#CMD ["/bin/bash", "/usr/local/bin/run.sh"]
WORKDIR /data
CMD ["python","run_tasks.py"]
