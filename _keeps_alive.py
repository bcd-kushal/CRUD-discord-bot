from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "myDB bot is running right now...."


def run():
    app.run(host='0.0.0.0',port=8080)

def keeping_alive():
    t = Thread(target=run)
    t.start()