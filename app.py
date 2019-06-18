from flask import Flask
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.datetime.now()
    new_year = now.month == 12 and now.day==27
    return 'Si! esta funcionando aún.'

if __name__=="__main__":
    app.run()
