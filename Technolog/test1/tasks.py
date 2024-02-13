from celery import shared_task

@shared_task
def test1():
    print('test1')
    return 'print from test1'