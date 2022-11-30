from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route('/')
def index():
    return b'Hello from Flask!'

def run():
  app.run(host='0.0.0.0', port=80)

t = Thread(target=run)
t.start()
