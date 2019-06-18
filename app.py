from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 12 and now.day==27
    return render_template("index.html", new_year=new_year)
    #return 'Si! esta funcionando aún.'

if __name__=="__main__":
    app.run()
