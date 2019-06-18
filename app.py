from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    si_cumple = now.month == 12 and now.day==27
    return render_template("index.html", si_cumple=si_cumple)

if __name__=="__main__":
    app.run()
