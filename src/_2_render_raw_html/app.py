from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<center><h1>Sakkadankai namaskaru 🙏!<h1><h2>Flask shikkun kushi jalle!<h2><center>'

if __name__ == '__main__':
	# Try running this code by commentig this part!
    app.run(debug = True)
