from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='player' user='samlin' host='localhost' password='dbpass'")
cur = conn.cursor()

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


# check login credentials

def valid_login(username, password):
	cur.execute("""SELECT Password FROM Player WHERE Username = username""")
	pw = cur.fetchall()
	if pw == password:
		return true
	else:
		return false

