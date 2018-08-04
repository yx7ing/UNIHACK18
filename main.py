from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='eduquest' user='samlin' host='localhost' password='dbpass'")
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
	cur.execute("""SELECT PASSWORD FROM Player WHERE USERNAME = username""")
	pw = cur.fetchone()
	if pw[0] == password:
		return True
	else:
		return False


# login

def do_login(username):
	bonus = 10
	cur.execute("""SELECT EXP FROM Player WHERE USERNAME = username""")
	exp = cur.fetchone()[0] + bonus
	update_sql = """UPDATE Player
			SET EXP = %s
			WHERE USERNAME = %s"""
	cur.execute(update_sql, (str(exp), username))
	conn.commit()
	return main_page()
