# Celery Server and Task Scheduling Setup Guide

Follow these steps to set up the Celery server and schedule tasks for your project. Make sure you have the required dependencies installed before proceeding.

## Installation

1. Change to the project directory:
   ```
   cd ..
   ```

2. Install project dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

3. Install RabbitMQ by following the instructions [here](https://www.rabbitmq.com/install-windows.html).

## Start Celery Server

4. Start the RabbitMQ server.

5. Change to the project directory:
   ```
   cd SalasCuna
   ```

6. Apply database migrations:
   ```
   python manage.py migrate
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Start the Celery worker with gevent concurrency:
   ```
   celery -A SalasCuna worker -l INFO -P gevent
   ```

9. Monitor tasks with Flower (optional):
   ```
   celery -A SalasCuna flower
   ```

10. Schedule periodic tasks with Celery Beat:
    ```
    celery -A SalasCuna beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ```

## Local Routes

Access these local routes for additional functionality:

- Flower Dashboard: [http://localhost:5555/tasks](http://localhost:5555/tasks)

## Additional Resources

Refer to the following sources for more information:

- [Celery Documentation](https://docs.celeryq.dev/en/stable/getting-started/introduction.html)
- [Celery Deployment Guide](https://docs.celeryq.dev/en/stable/getting-started/next-steps.html)
- [Flower Installation](https://flower.readthedocs.io/en/latest/install.html)
- [Celery RabbitMQ Setup](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/rabbitmq.html)
- [Django Celery Integration](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html#django-first-steps)
- [Celery Custom Schedulers](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#beat-custom-schedulers)
- [Daemonizing Celery](https://docs.celeryq.dev/en/stable/userguide/daemonizing.html)

For more in-depth tutorials, check out this [YouTube playlist](https://youtube.com/playlist?list=PLOLrQ9Pn6caz-6WpcBYxV84g9gwptoN20&si=MIYCNGCNFip6gjhn).

Happy coding!
