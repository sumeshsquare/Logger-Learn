from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return '<h2> Welcome to Reddiars Learning APP for kids </h2>  <img src="imag.png" alt="Smiley face" > '

if __name__ == "__main__":
	app.run()
