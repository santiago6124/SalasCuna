Run the following commands to instatiate the Celery server and schedule tasks:

1- cd .. --> pip install -r requirements.txt
2- install RabbitMQ --> [https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html](https://www.rabbitmq.com/install-windows.html)
3- start rabbitmq server
4- cd SalasCuna --> manage.py migrate
5- manage.py runserver
6- celery -A SalasCuna worker -l INFO -P gevent
7- celery -A SalasCuna flower 
8- celery -A SalasCuna beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
9- celery -A SalasCuna worker -l INFO -P gevent

local routes:
-http://localhost:5555/tasks (Flower)

(See Celery docs for deployment)

Source links:
https://flower.readthedocs.io/en/latest/install.html
http://127.0.0.1:8000/admin/django_celery_beat/periodictask/
https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html
https://docs.celeryq.dev/en/stable/getting-started/introduction.html
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#django-first-steps
https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#beat-custom-schedulers
https://docs.celeryq.dev/en/stable/userguide/daemonizing.html#daemonizing
https://docs.celeryq.dev/en/stable/getting-started/next-steps.html#next-steps
https://youtube.com/playlist?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20&si=MIYCNGCNFip6gjhn
