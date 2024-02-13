import psycopg2
# from shutdown.models import Shutdown

conn = psycopg2.connect(
    host='10.21.10.7',
    database="technolog",
    user='postgres',
    password=''
)

buf = []

cursor = conn.cursor()
# cursor.execute("SELECT * FROM stoprtp1, stoprtp2, stoprtp3, stoprtp4 WHERE date_end NOT IN ('information_schema','pg_catalog');")
# cursor.execute("""SELECT * FROM asutp.stoprtp1 WHERE date_end BETWEEN  date('2023-08-01 00:00:00') AND  date('2023-08-20 00:00:00');""")
cursor.execute("""SELECT date_begin, date_end FROM asutp.stoprtp1 ORDER BY id_row DESC LIMIT 4;""")
# print(cursor.fetchall())
for i, row in enumerate(cursor):
    buf.append([])
    for j, value in enumerate(row):
        buf[i].append(value)
        # print(j)
print(buf)
cursor.close()
conn.close()

