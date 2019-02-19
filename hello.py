from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> <center> Welcome to CareBook !!! </center> </h1>'

if __name__ == "__main__":
	app.run()
