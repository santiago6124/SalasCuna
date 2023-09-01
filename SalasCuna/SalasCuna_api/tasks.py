# Create your tasks here

from .models import Child

from celery import shared_task


@shared_task
def getChild(child_id):
    return Child.objects.all().get(id = int(child_id)).dni


@shared_task
def mul(x, y):
    return x * y


# @shared_task
# def xsum(numbers):
#     return sum(numbers)


# @shared_task
# def count_widgets():
#     return Widget.objects.count()


# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()