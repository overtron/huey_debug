from huey.contrib.djhuey import task
from django.conf import settings


@task()
def task1():
    pass

@task()
def task2():
    pass
