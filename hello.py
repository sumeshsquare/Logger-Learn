from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h1> <center> Welcome to CareBook !!! </center> </h1> <p></p> <h3> <center> A book for the regular checkups </center></h3>'

if __name__ == "__main__":
	app.run()
