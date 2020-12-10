from flask import Flask, request, Response 
from db import cursor

app = Flask(__name__)

# display all integer sequence names"
@app.route("/")
def index():
    cursor.execute('select name from Sequences;')

    response = Response()
    response.set_data(f'Welcome to the Integer Sequence Database.\r\n</br>Sequences: {str([*cursor])[1:-1]}')

    return response

# view a sequence. e.g.: /viewseq?name=pi digits
@app.route("/viewseq")
def viewSeq():

    name = request.args.get("name") # get query string
    response = Response()
    cursor.execute(f'select seq from Sequences where name=\'{name}\';')
    response.set_data(str([str(i) for i in cursor])) # write to response

    return response

# add a sequence. e.g.: /addseq?id=1337&name=Natural Numbers&seq=1, 2, 3, 4, 5, 6, 7, 8, 9, 10
@app.route("/addseq")
def addSeq():

    # get id, name and seq query strings
    id = request.args.get("id")
    name = request.args.get("name")
    seq = request.args.get("seq")

    response = Response()
    cursor.execute(f'insert into Sequences values({id},\'{name}\',\'{seq}\');')
    response.set_data(f'Added sequence {name}.') # write response with new sequence name

    # to make changes persist
    # db.commit() (import db first)

    return response

if __name__ == '__main__':
    app.run()