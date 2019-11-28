from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()

    my_birthday = datetime.datetime(now.year, 12, 27, 0, 0, 0)
    #my_birthday = datetime.datetime(now.year, 12, 27, 3, 3, 0)
    #hora de nacimiento real
    #my_birthday = datetime.datetime(now.year, now.month, now.day)  #pruebas

    si_cumple = now.month==my_birthday.month and now.day==my_birthday.day

    if my_birthday < now:
        my_birthday = my_birthday.replace(year=now.year + 1)

    dt = abs(my_birthday - now)
    falta = dt.days
    segs = round(dt.total_seconds())
    horas = round(segs/60/60)
    segs = format(segs,',d')
    segs = str(segs)
    segs=segs.replace(",",".")

    return render_template("index.html", si_cumple=si_cumple, falta=falta, segs=segs, horas=horas)

if __name__=="__main__":
    app.run()
