from flask import Flask, request, Response 
from db import cursor

app = Flask(__name__)

@app.route("/")
def index():

    response = Response()
    response.set_data('Welcome to the Integer Sequence Database.\r\n')

    return response

@app.route("/viewseq")
def viewSeq():

    response = Response()
    cursor.execute(f'select seq from Sequences where name=\'{request.args.get("name")}\';')
    response.set_data(str([str(i) for i in cursor]))

    return response

if __name__ == '__main__':
    app.run()