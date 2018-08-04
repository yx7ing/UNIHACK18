from flask import Flask
import random
app = Flask(__name__)

@app.route("/equations")
def equations():
	format = random.randint(1,8)
	num1 = random.randint(2,9)
	num2 = random.randint(2,9)
	num3 = random.randint(2,9)
	num4 = random.randint(2,9)
	num5 = random.randint(2,9)
	if format == 1:
		answer = (num5-num1*num2-num3*num4)/(num1+num3)
		question = "eq,%d(x + %d) + %d(x + %d) = %d,%2.2f" % (num1,num2,num3,num4,num5,answer)
	elif format == 2:
		answer = (num5-num1*num2+num3*num4)/(num1+num3)
		question = "eq,%d(x + %d) + %d(x - %d) = %d,%2.2f" % (num1,num2,num3,num4,num5,answer)
	elif format == 3:
		answer = (num5+num1*num2-num3*num4)/(num1+num3)
		question = "eq,%d(x - %d) + %d(x + %d) = %d,%2.2f" % (num1,num2,num3,num4,num5,answer)
	elif format == 4:
		answer = (num5+num1*num2+num3*num4)/(num1+num3)
		question = "eq,%d(x - %d) + %d(x - %d) = %d,%2.2f" % (num1,num2,num3,num4,num5,answer)
	elif format == 5:
		answer = (num1*num3+num5)/(num4-num1*num2)
		question = "eq,%d(%dx + %d) = %dx - %d,%2.2f" % (num1,num2,num3,num4,num5,answer)
	elif format == 6:
		answer = (num3*num5-num2)/(num1-num3*num4)
		question = "eq,%dx + %d = %d(%dx + %d),%2.2f" % (num1,num2,num3,num4,num5,answer)
	elif format == 7:
		answer = (num1*num3+num5)/(num1*num2-num4)
		question = "eq,%d(%dx - %d) = %dx + %d,%2.2f" % (num1,num2,num3,num4,num5,answer)
	elif format == 8:
		answer = (num2-num3*num5)/(num1-num3*num4)
		question = "eq,%dx - %d = %d(%dx - %d),%2.2f" % (num1,num2,num3,num4,num5,answer)
	return question
	
@app.route("/gradient")
def gradients():
	format = random.randint(1,4)
	num1 = random.randint(2,9)
	num2 = random.randint(2,9)
	num3 = random.randint(2,9)
	if format == 1:
		answer = num1
		question = "gr,y = %dx + %d,%d" % (num1,num2,answer)
	elif format == 2:
		answer = num1
		question = "gr,y = %dx - %d,%d" % (num1,num2,answer)
	elif format == 3:
		answer = num1/num2
		question = "gr,%dx - %dy + %d = 0,%2.2f" % (num1,num2,num3,answer)
	elif format == 4:
		answer = num1/num2
		question = "gr,%dx - %dy = %d,%2.2f" % (num1,num2,num3,answer)
	return question
	
	
	
	
	