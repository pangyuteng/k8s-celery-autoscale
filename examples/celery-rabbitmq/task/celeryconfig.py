broker_service_host = os.environ.get('RABBITMQ_SERVICE_SERVICE_HOST')
# Get Kubernetes-provided address of the broker service
BROKER_URL = 'amqp://guest@{}:5672//'.format(broker_service_host)
print(BROKER_URL)
#CELERY_RESULT_BACKEND = 'redis://localhost'