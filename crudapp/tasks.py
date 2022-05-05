from celery import shared_task

from time import sleep

@shared_task(bind=True)
def update_verify(self, duration):
    sleep(duration)
    print("success")
    return 'Done'
