import mysql.connector
import sys

try:
    db  = mysql.connector.connect(
        host='localhost',
        user='intseq_app',
        database='intseq'
    )
except:
    print('Error connecting to database.')
    sys.exit(1)


cursor = db.cursor()

cursor.execute('select name,seq from Sequences;')
for i in cursor:
    print(i[0]) # name
    for j in i[1].split(', '): print(j)
# cursor.execute('select * from Sequences;')
