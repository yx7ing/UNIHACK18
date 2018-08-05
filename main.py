from flask import Flask, render_template, request, jsonify
import random
import ind as I
import fin as F
import lin as L
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

# transform SQL queries to JSON

def get_player():
	player_dict = {}
	cur.execute("""SELECT * FROM Player""")
	player_dict['player_id'] = []
	player_dict['username'] = []
	player_dict['password'] = []
	player_dict['name'] = []
	player_dict['exp'] = []
	player_dict['level'] = []
	player_dict['win'] = []
	player_dict['loss'] = []
	player_dict['boss'] = []
	player_dict['quests_completed'] = []
	all = cur.fetchall()
	for one in all:
		player_dict['player_id'].append(one[0])
		player_dict['username'].append(one[1])
		player_dict['password'].append(one[2])
		player_dict['name'].append(one[3])
		player_dict['exp'].append(one[4])
		player_dict['level'].append(one[5])
		player_dict['win'].append(one[6])
		player_dict['loss'].append(one[7])
		player_dict['boss'].append(one[8])
		player_dict['quests_completed'].append(one[9])
	return jsonify(player_dict)

def get_quests():
	quests_dict = {}
	cur.execute("""SELECT * FROM Quests""")
	quests_dict['quest_id'] = []
	quests_dict['topic'] = []
	quests_dict['subtopic'] = []
	all = cur.fetchall()
	for one in all:
		quests_dict['quest_id'].append(one[0])
		quests_dict['topic'].append(one[1])
		quests_dict['subtopic'].append(one[2])
	return jsonify(quests_dict)

def get_class():
	class_dict = {}
	cur.execute("""SELECT * FROM Class""")
	class_dict['player_id'] = []
	class_dict['class_id'] = []
	all = cur.fetchall()
	for one in all:
		class_dict['player_id'].append(one[0])
		class_dict['class_id'].append(one[1])
	return jsonify(class_dict)

@app.route("/add1")
def basic():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    ans = a + b

    return jsonify({"type": "add", "params": str(a) + "," + str(b) + "," + str(ans)})

@app.route("/available_routes")
def get_routes():
    return jsonify({"routes": ["ind1", "ind2", "ind3", "fin1", "fin2", "fin3", "lin1", "lin2"]})

@app.route("/ind1")
def ind_1():
    return I.ind_1()

@app.route("/ind2")
def ind_2():
    return I.ind_2()

@app.route("/ind3")
def ind_3():
    return I.ind_3()

@app.route("/fin1")
def fin_1():
    return F.fin_1()

@app.route("/fin2")
def fin_2():
    return F.fin_2()

@app.route("/fin3")
def fin_3():
    return F.fin_3()

@app.route("/lin1")
def lin_1():
    return L.gradients()

@app.route("/lin2")
def lin_2():
    return L.equations()
