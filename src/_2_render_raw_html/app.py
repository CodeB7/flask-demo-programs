from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><h1>Namaste Everyone! 🙏<h1><h2>Let\'s learn Flask!<h2><center>'

if __name__ == '__main__':
    app.run(debug = True)
