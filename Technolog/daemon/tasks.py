from celery import shared_task
import psycopg2, datetime



@shared_task
def writerShutdown():

    conn1 = psycopg2.connect( # Подключаемся к старой бд
        host='10.21.10.7',
        database="technolog",
        user='postgres',
        password=''
    )

    conn2 = psycopg2.connect( #подключаемся к местной бд
        host='localhost',
        database="technolog",
        user='admin_technolog',
        port="5432",
        password='0000'
    )

    number_furn = [1, 2, 3, 4,] # список с номерами печей
   # names_old_db = 'asutp.stoprtp' # наименование бд на conn1  без номера, программно подставляется
    names_furn_new = '' # сюда складывается название печей для linux бд
    date_begin = '' # сюда и ниже складываются строковые значения дат из старой бд
    date_end = ''
    interval =''
    last_dates_in_db = { # в нём сразу храняться и ключи пронумерованные и последние даты записи по печам из новой бд и названия агрегатов
        'Рудно-термическая печь №1': 0,
        'Рудно-термическая печь №2': 0,
        'Рудно-термическая печь №3': 0,
        'Рудно-термическая печь №4': 0,
    }
    cursor2 = conn2.cursor()
    cursor1 = conn1.cursor()
    for i in number_furn: # пошли перебирать номера печей
        print(i)
        # ниже выдёргиваем из новой бд даты окончания последних простоев
        cursor2.execute(f"SELECT date_end FROM public.shutdown_shutdown  WHERE agregate_name='Рудно-термическая печь №{str(i)}' ORDER BY date_end DESC LIMIT 1;")
        for date in cursor2:
            for d in date:
                last_dates_in_db[f'Рудно-термическая печь №{str(i)}'] = d #складываем эти даты в словарик универсальный 
                # если не преобразовать в секунды и после в таймштамп в запросе он будет складывать в бд многократно все записи за последний день
                # проверяет почему то имено дату без учёта часов и минут 
            print(last_dates_in_db)
        if last_dates_in_db[f'Рудно-термическая печь №{str(i)}']: # проверяем, выдернули ли вобще что то
            date_i=last_dates_in_db[f'Рудно-термическая печь №{i}'].timestamp()# преобразуем дату в секунды
            print('timestamp = ' + str(last_dates_in_db[f'Рудно-термическая печь №{i}'].timestamp()))
            cursor1.execute(f"SELECT * FROM asutp.stoprtp{i} WHERE date_end > to_timestamp('{date_i}')") # выбираем все записи, которые старше записанных в новой бд
            for date in cursor1:
                print(date)
                print(i)
                for f, value in enumerate(date): #перебираем записи и отправляем в переменные только 1, 2 элементы записи, 0 пропускаем(там не нужный нам id)
                    if f==1:
                        date_begin = value.strftime("%Y-%m-%d %H:%M:%S")
                        interval = value
                    if f==2:
                        date_end = value.strftime("%Y-%m-%d %H:%M:%S")
                        interval = value - interval
                        print('date_begin = '+ str(date_begin))
                        print('date_end = '+ str(date_end))
                        print('interval = '+ str(interval))
                names_furn_new = list(last_dates_in_db.keys())[i-1]# получаем название печи из ключа
                cursor2.execute(f"INSERT INTO public.shutdown_shutdown (date_begin, date_end, interval, agregate_name, commentary, flag_classification) VALUES ('{date_begin}', '{date_end}', '{interval}','{names_furn_new}', '', 'false')")
                conn2.commit() # сложили всё что надо, приняли и закрыли
    cursor1.close()
    conn1.close()    
    cursor2.close()
    conn2.close()
    return 'миграция выполнена, если были данные :D'

# writerShutdown()