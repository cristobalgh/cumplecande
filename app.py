from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Fecha y hora real de nacimiento de Candelaria
NACIMIENTO = datetime.datetime(2018, 12, 27, 3, 3, 0)

MESES = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

@app.route('/')
def index():
    now = datetime.datetime.now()

    proximo_cumple = NACIMIENTO.replace(year=now.year)
    if proximo_cumple < now:
        proximo_cumple = proximo_cumple.replace(year=now.year + 1)

    edad = now.year - NACIMIENTO.year
    if (now.month, now.day, now.hour, now.minute) < (NACIMIENTO.month, NACIMIENTO.day, NACIMIENTO.hour, NACIMIENTO.minute):
        edad -= 1

    si_cumple = (now.month, now.day) == (NACIMIENTO.month, NACIMIENTO.day) and \
                (now.hour, now.minute) >= (NACIMIENTO.hour, NACIMIENTO.minute)

    dt = proximo_cumple - now

    days = dt.days
    falta = days
    s = dt.seconds
    hours = s // 3600
    horas = hours
    s -= hours * 3600
    minutes = s // 60
    seconds = s - minutes * 60

    intervals = (
        ('m', 2540160),
        ('S', 604800),
        ('d', 86400),
        ('h', 3600),
        ('m', 60),
        ('s', 1),
    )

    def display_time(seconds, granularity=6):
        result = []
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                result.append("{}{}".format(value, name))
        return ' '.join(result[:granularity])

    segs = display_time(round(dt.total_seconds()))

    nacio_str = "{} de {} de {} a las {:02d}:{:02d}".format(
        NACIMIENTO.day, MESES[NACIMIENTO.month - 1], NACIMIENTO.year,
        NACIMIENTO.hour, NACIMIENTO.minute
    )

    return render_template("index.html", edad=edad, si_cumple=si_cumple,
                            falta=falta, segs=segs, horas=horas, nacio_str=nacio_str)

if __name__ == "__main__":
    app.run()
