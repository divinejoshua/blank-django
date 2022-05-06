from celery import shared_task
from .models import NameList, NumberGuess

import random
import string


from time import sleep

# This task is delayed by 20 seconds 
# The user is verified by this task 
@shared_task
def update_verify(id):
    sleep(20)

    instance = NameList.objects.filter(pk=id).first()
    instance.verified = True
    instance.save()
    return 'Done Celery'



# The user is verified by this task 
@shared_task
def add_number():

    # printing values
    letters = string.ascii_lowercase
    random_value = ''.join(random.choice(letters) for i in range(10))

    # Instantiate the Models 
    instance = NumberGuess()
    instance.number = random_value
    instance.save()

    return 'Done Celery beat'
