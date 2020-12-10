from flask import Flask, request, Response 
from db import cursor

app = Flask(__name__)

@app.route("/")
def index():
    cursor.execute('select name from Sequences;')

    response = Response()
    response.set_data(f'Welcome to the Integer Sequence Database.\r\n</br>Sequences: {str([*cursor])[1:-1]}')

    return response

@app.route("/viewseq")
def viewSeq():

    name = request.args.get("name")
    response = Response()
    cursor.execute(f'select seq from Sequences where name=\'{name}\';')
    response.set_data(str([str(i) for i in cursor]))

    return response

@app.route("/addseq")
def addSeq():

    id = request.args.get("id")
    name = request.args.get("name")
    seq = request.args.get("seq")

    response = Response()
    cursor.execute(f'insert into Sequences values({id},\'{name}\',\'{seq}\');')
    response.set_data(f'Added sequence {name}.')

    return response

if __name__ == '__main__':
    app.run()