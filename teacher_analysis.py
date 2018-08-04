from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='player' user='samlin' host='localhost' password='dbpass'")
cur = conn.cursor()

@app.route('/analyse')
def analyse(student_name):
  topic_dict = {}
  subtopic_dict = {}
  cur.execute("""SELECT EXP FROM Player WHERE NAME = student_name""")
  exp = cur.fetchone()[0]
  cur.execute("""SELECT LEVEL FROM Player WHERE NAME = student_name""")
  lvl = cur.fetchone()[0]
  cur.execute("""SELECT QUESTS_COMPLETED FROM Player WHERE NAME = student_name""")
  quest_nos = cur.fetchone()[0]
  
  for quest_id in quests_nos:
  
    #check which topic/subtopic this quest is in
    cur.execute("""SELECT TOPIC FROM Quests WHERE QUEST_ID = quest_id""")
    topic = cur.fetchone()[0]
    cur.execute("""SELECT SUBTOPIC FROM Quests WHERE QUEST_ID = quest_id""")
    subtopic = cur.fetchone()[0]
    
    #update topic count
    if topic in topic_dict.keys():
      topic_dict[topic] = topic_dict[topic] + 1
    else:
      topic_dict[topic] = 1
    
    #subtopic boolean table
      subtopic_dict[subtopic] = True
    
  

  
  
