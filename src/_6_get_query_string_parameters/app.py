from flask import Flask
from flask import render_template, request

app = Flask(__name__)


# @app.route('/hello/', methods=['GET'])
# def index():
# 	first_name = request.args['fname']
# 	last_name = request.args['lname']
# 	return render_template('hello.html', fname=first_name, lname=last_name)

@app.route('/form_submission', methods=['GET'])
def form_submission():
	first_name = request.args['first_name']
	last_name = request.args['last_name']
	return render_template('success.html', first_name=first_name, last_name=last_name)

@app.route('/')
def home():
	return render_template('form.html')


if __name__ == '__main__':
    app.run(debug = True)

# http://127.0.0.1:5000/hello?fname=A&lname=B
