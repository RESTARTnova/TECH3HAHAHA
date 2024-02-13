import psycopg2, datetime
# from shutdown.models import Shutdown

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
    password=''
)

number_furn = [1, 2, 3, 4,] # список с номерами печей
names_old_db = 'asutp.stoprtp' # наименование бд на conn1  без номера, программно подставляется
names_furn_new = '' # сюда складывается название печей для linux бд
date_begin = '' # сюда и ниже складываются строковые значения дат из старой бд
date_end = ''
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
        cursor1.execute(f"SELECT * FROM asutp.stoprtp{i} WHERE date_end > to_timestamp('{date_i}')") # выбираем все записи, которые старше записанных в новой бд
        for date in cursor1:
            print(date)
            print(i)
            for f, value in enumerate(date): #перебираем записи и отправляем в переменные только 1, 2 элементы записи, 0 пропускаем(там не нужный нам id)
                if f==1:
                    date_begin = value.strftime("%Y-%m-%d %H:%M:%S")
                if f==2:
                    date_end = value.strftime("%Y-%m-%d %H:%M:%S")
            names_furn_new = list(last_dates_in_db.keys())[i-1]# получаем название печи из ключа
            cursor2.execute(f"INSERT INTO public.shutdown_shutdown (date_begin, date_end, agregate_name, commentary, flag_classification) VALUES ('{date_begin}', '{date_end}', '{names_furn_new}', '', 'false')")
            conn2.commit() # сложили всё что надо, приняли и закрыли
cursor1.close()
conn1.close()    
cursor2.close()
conn2.close()

# cursor = conn.cursor()
# # cursor.execute("SELECT * FROM stoprtp1, stoprtp2, stoprtp3, stoprtp4 WHERE date_end NOT IN ('information_schema','pg_catalog');")
# # cursor.execute("""SELECT * FROM asutp.stoprtp1 WHERE date_end BETWEEN  date('2023-08-01 00:00:00') AND  date('2023-08-20 00:00:00');""")
# cursor.execute("""SELECT date_begin, date_end FROM asutp.stoprtp1 ORDER BY id_row DESC LIMIT 4;""")
# # print(cursor.fetchall())
# for i, row in enumerate(cursor):
#     buf.append([])
#     for j, value in enumerate(row):
#         buf[i].append(value)
#         # print(j)
# print(buf)
# cursor.close()
# conn.close()

# cursor = conn2.cursor()
# # cursor.execute("SELECT version()")
# cursor.execute("SELECT date_end FROM public.shutdown_shutdown  WHERE agregate_name='Рудно-термическая печь №4' ORDER BY date_end DESC LIMIT 1;")
# for i in cursor:
#     print(i)
# cursor.execute("SELECT date_end FROM public.shutdown_shutdown  WHERE agregate_name='Рудно-термическая печь №3' ORDER BY date_end DESC LIMIT 1;")
# print(cursor.fetchone())
# cursor.close()
# conn.close()
# print(date_execute)