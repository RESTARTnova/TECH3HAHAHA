from Technolog.celery import app



@app.task(bind=True) #(name="repeat_order_make") #регистриуем таску
def repeat_order_make():
    print('adsdasd')

    #url = 'sdasd'
    #obj = Person.objects.get_or_create(last_name=f'{time.time()}11111111111111111', first_name='1111')
    return "необязательная заглушка"