from celery import shared_task
from .models import NameList, BlogPost


from time import sleep

# This task is delayed by 20 seconds 
# The user is verified by this task 
@shared_task
def update_verify(id):
    sleep(20)

    instance = NameList.objects.filter(pk=id).first()
    instance.verified = True
    instance.save()
    return 'Done'
