from flask import Flask, render_template, request
app = Flask(__name__)


# main page

@app.route('/')
def main_page():
	return render_template('index.html', name=None)


# login page

@app.route('/login', methods=['POST', 'GET'])
def login():
	error = None
	if request.method == 'POST':
		if valid_login(request.form['username'], request.form['password']):
			return do_login(request.form['username'])
		else:
			error = 'Invalid username/password'
	return render_template('login.html', error=error)


