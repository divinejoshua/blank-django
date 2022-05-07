from time import sleep
from threading import Thread

def threaded_function():
    for i in range(5):
        print(i)
        sleep(3)


def my_cron_job():
    thread = Thread(target = threaded_function)
    thread.start()
    print("coo")
    # your functionality goes here


