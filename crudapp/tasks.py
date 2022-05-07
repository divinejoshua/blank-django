from celery import shared_task
from .cron import my_cron_job
from threading import Thread


from .models import NameList, NumberGuess

import random
import string


from time import sleep

# This task is delayed by 20 seconds 
# The user is verified by this task 

# Threading for update verify
def update_verify_thread(id):
    sleep(20)
    print("was here")

    instance = NameList.objects.filter(pk=id).first()
    instance.verified = True
    instance.save()



@shared_task
def update_verify(id):
    thread = Thread(target = update_verify_thread, args = (id,))
    thread.start()

   
    return 'Done Celery'





# Add number Thread 
def add_number_thread():
    # printing values
    letters = string.ascii_lowercase
    random_value = ''.join(random.choice(letters) for i in range(10))

    # Instantiate the Models 
    instance = NumberGuess()
    instance.number = random_value
    instance.save()



# The user is verified by this task 
@shared_task
def add_number():
    thread = Thread(target = add_number_thread)
    thread.start()
    return 'Done Celery beat'


