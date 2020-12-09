from flask import Flask, request, Response 
from db import cursor

app = Flask(__name__)

@app.route("/")
def index():

    response = Response()
    response.set_data('Welcome to the Integer Sequence Database.\r\n')

    return response

if __name__ == '__main__':
    app.run()