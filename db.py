# connects to database for server.py
# server.py imports cursor 

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
    db = None
    sys.exit(1)

cursor = db.cursor()