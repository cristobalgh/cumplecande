import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    new_year = now.month == 12 and now.day==27
    return render_template("index.html", new_year=new_year)

if __name__== "__main__":
    app.run()
