from flask import Flask, render_template, request, session
from flask_table import Table, Col
import sqlite3


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

conn = sqlite3.connect('/home/thecsr/Documents/Shubham/DHT11/raspdata.sqlite')
c = conn.cursor()


class Results(Table):
    dati = Col('dati')
    temp = Col('Temperature')
    hum = Col('Humidity')

if (__name__ == "__main__"):
    app.run(debug=True)