from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='player' user='samlin' host='localhost' password='dbpass'")
cur = conn.cursor()

@app.route('/stats')
def stats(Player_id):
  cur.execute("""SELECT EXP FROM Stats WHERE PLAYER_ID = Player_id""")
  exp = cur.fetchall()
  cur.execute("""SELECT LEVEL FROM Stats WHERE PLAYER_ID = Player_id""")
  lvl = cur.fetchall()
  cur.execute("""SELECT WIN FROM Stats WHERE PLAYER_ID = Player_id""")
  win = cur.fetchall()
  cur.execute("""SELECT LOSS FROM Stats WHERE PLAYER_ID = Player_id""")
  loss = cur.fetchall()
  cur.execute("""SELECT BOSS Stats WHERE PLAYER_ID = Player_id""")
  boss = cur.fetchall()
  
  
