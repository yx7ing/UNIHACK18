from flask import Flask
import math
app = Flask(__name__)

@app.route("/projectile")
def projectile():
	num1 = random.randint(2,5)
	num2 = random.randint(2,5)
	answer = num2*(math.sqrt(2*num1/9.8))
	question = "What is the range of a ball shot horizontally off a %dm high cliff at %dm/s?,%2.2f" % (num1,num2,answer)
	return jsonify({"type":"proj", "params":question})