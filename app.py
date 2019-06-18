from flask import Flask, render_template
import datetime
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    si_cumple = now.month==12 and now.day==27

    today = date.today()
    my_birthday = date(today.year, 6, 19)
    if my_birthday < today:
        my_birthday = my_birthday.replace(year=today.year + 1)
    time_to_birthday = abs(my_birthday - today)
    falta = time_to_birthday.days

    return render_template("index.html", si_cumple=si_cumple, falta=falta)

if __name__=="__main__":
    app.run()
