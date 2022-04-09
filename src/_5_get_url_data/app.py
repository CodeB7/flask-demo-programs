from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>/')
def index(name=''):
    if not name:
        return "<center><h1>Hi There!</h1></center>"
    return render_template('hello.html', name=name)

@app.route('/')
def default():
    return "<a href='/hello'>Click Here</a>"

if __name__ == '__main__':
    app.run(debug = True)
