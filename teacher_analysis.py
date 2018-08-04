from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='eduquest' user='samlin' host='localhost' password='dbpass'")
cur = conn.cursor()

@app.route('/analyse')
def analyse():
  student_name = '\'a\''
  analyse_funct(student_name)

#REQUIRES DEBUGGING: Works with NAME = 'test' but not with NAME = name;
def analyse_funct(name):
  topic_dict = {}
  subtopic_dict = {}

  test = name
  cur.execute("""SELECT EXP FROM Player WHERE NAME = %s""" % test)
  exp = cur.fetchone()[0]
  #print(str(exp))
  cur.execute("""SELECT LEVEL FROM Player WHERE NAME = %s""" % test)
  lvl = cur.fetchone()[0]
  #print(lvl)
  cur.execute("""SELECT QUESTS_COMPLETED FROM Player WHERE NAME = %s""" % test)
  quest_nos = cur.fetchone()[0]
  #print(quest_nos)

  for quest_id in quest_nos:

    #check which topic/subtopic this quest is in
    cur.execute("""SELECT TOPIC FROM Quests WHERE QUEST_ID = %s""" % quest_id)
    topic = cur.fetchone()[0]
    cur.execute("""SELECT SUBTOPIC FROM Quests WHERE QUEST_ID = %s""" % quest_id)
    subtopic = cur.fetchone()[0]

    #update topic count

    if topic in topic_dict.keys():
      (topic_dict[topic])[subtopic] = True
    else:
      topic_dict[topic] = {subtopic: True}

  ans = jsonify(topic_dict)
  return ans
