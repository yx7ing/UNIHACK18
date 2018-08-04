from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='player' user='samlin' host='localhost' password='dbpass'")
cur = conn.cursor()

@app.route('/stats')
def stats(Player_id):
  cur.execute("""SELECT EXP FROM Player WHERE PLAYER_ID = Player_id""")
  exp = cur.fetchone()
  cur.execute("""SELECT LEVEL FROM Player WHERE PLAYER_ID = Player_id""")
  lvl = cur.fetchone()
  cur.execute("""SELECT WIN FROM Player WHERE PLAYER_ID = Player_id""")
  win = cur.fetchone()
  cur.execute("""SELECT LOSS FROM Player WHERE PLAYER_ID = Player_id""")
  loss = cur.fetchone()
  cur.execute("""SELECT BOSS FROM Player WHERE PLAYER_ID = Player_id""")
  boss = cur.fetchone()
  
  
