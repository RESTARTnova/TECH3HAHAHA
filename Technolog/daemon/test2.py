import psycopg2


dict = {
    'key1':123,
    'key2':345
}

print(type(list(dict.keys())[0])) # это песочница

#ВОТ НИЖЕ скрипт для удаления дубликатов в бд

conn = psycopg2.connect( #подключаемся к местной бд
    host='localhost',
    database="technolog",
    user='admin_technolog',
    port="5432",
    password=''
)


date_begin=''
date_end=''
name=''
mass=[]
mass_deffect_id=[]

cursor = conn.cursor()
cursor.execute("SELECT * FROM public.shutdown_shutdown")
for i, value in enumerate(cursor):
    mass.append([])
    for j in value:
        mass[i].append(j)

# cursor.close()
# conn.close()
print(mass) 

# for i, spisok in enumerate(mass):
#     for j, value in enumerate(spisok):
#         if 
i=0
j=0
while i< len(mass):
    j=i+1
    while j<len(mass):
        if mass[i][1]==mass[j][1] and mass[i][2]==mass[j][2] and mass[i][3]==mass[j][3]:
            mass_deffect_id.append(mass[j][0])
            mass.pop(j)
            j-=1
        j+=1
    i+=1

print(mass_deffect_id)
# cursor = conn.cursor()
for i in mass_deffect_id:
    cursor.execute(f"DELETE FROM public.shutdown_shutdown WHERE id={i}")
    conn.commit()
cursor.close()
conn.close()