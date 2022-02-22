from flask import Flask, render_template
from datetime import datetime, date
import calendar

app = Flask(__name__)

@app.get('/')
def index():
    currentdate = datetime.now()
    return render_template('index.html' ,mytime=currentdate.strftime("%A, %d %B %Y %H:%M:%S"))

