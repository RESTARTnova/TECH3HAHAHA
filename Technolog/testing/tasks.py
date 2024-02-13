from celery import shared_task



@shared_task #(name="repeat_order_make") #регистриуем таску
def repeat_order_make():
    print('adsdasd')
    return "pfdslkgfslkhfdh123"


