from celery import shared_task

@shared_task
def test2():
    print('test2')
    return 'print from test2'