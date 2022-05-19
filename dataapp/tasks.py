from celery import shared_task
from threading import Thread


from .models import NameListCheck


from time import sleep

# This task is delayed by 20 seconds 
# The user is verified by this task 

# Threading for update verify
def addcheck_thread():
    sleep(20)
    instance = NameListCheck()
    instance.name = "done"
    instance.save()



@shared_task
def addcheck():
    thread = Thread(target=addcheck_thread)
    thread.start()

   
    return 'Done Add check'


