# Create your tasks here

from .models import Child

from celery import shared_task

from datetime import datetime

@shared_task
def getChild(child_id):
    return Child.objects.all().get(id = int(child_id)).dni

@shared_task
def disenrollOldChild():
    qs = Child.objects.all().filter(is_active = True)
    
    children_disenroll = {
        
    }
    
    for child in qs:
        current_date = datetime.now()
        
        # check 1st part of the year (Jan[01] - Jun[06])
        # --> disenroll children where their birthday is between Jan and Jun
        # ----> if the current month is between Jan and Jun and they are older than 4
        
        if current_date.month >= 1 and current_date.month <= 6:
            age = current_date.year - child.birthdate.year - ((6, 30) < (child.birthdate.month, child.birthdate.day))

        else:
            age = current_date.year - child.birthdate.year - ((current_date.month, current_date.day) < (child.birthdate.month, child.birthdate.day))

        disenroll = True if age >= 4 else False
        if disenroll:
            child.is_active = False
            child.save()
            children_disenroll[child.id] = age
    
    return str(children_disenroll)
