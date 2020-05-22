from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World! I am Hardy'


if __name__ == '__main__':
    run = app.run(host="0.0.0.0", port=80)
