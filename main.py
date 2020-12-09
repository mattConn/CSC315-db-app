import mysql.connector
import sys

# connect to db as app user
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

# insert a new integer sequence (powers of 2)
cursor.execute(f'insert into Sequences values(5, \'Powers of 2\', \'{str([2**i for i in range(30)])[1:-1]}\')') # mean one-liner

# select parametrized query 
selectSeq = 'select %s from Sequences where %s;'

# select pi digits
cursor.execute(selectSeq % ('seq','name = \'Pi Digits\'') )

# print results
for i in cursor: print(i)

db.commit() # make changes stick 
db.close()