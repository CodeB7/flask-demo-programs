from flask import Flask
from flask import render_template, request

app = Flask(__name__)


@app.route('/hello/', methods=['GET'])
@app.route('/')
def index():
	if not request.args:
		return "<h2>Please send First and Last Name in the query string.</h2>"
	first_name = request.args['fname']
	last_name = request.args['lname']
	return render_template('hello.html', fname=first_name, lname=last_name)

if __name__ == '__main__':
    app.run(debug = True)

# http://127.0.0.1:5000/hello?fname=A&lname=B
