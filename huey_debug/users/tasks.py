from hueyx.queues import hueyx
from django.conf import settings

HUEY = hueyx(settings.GENERAL_QUEUE)

@HUEY.task()
def task1():
    pass

@HUEY.task()
def task2():
    pass
