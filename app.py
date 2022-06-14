from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'why does everyone greet the world...\nthen just destroy it'

if __name__ == '__main__':
	app.run()