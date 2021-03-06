from flask import Flask, jsonify
import math
import random

app = Flask(__name__)

@app.route("/projectile")
def projectile():
    num1 = random.randint(2,5)
    num2 = random.randint(2,5)
    answer = num2*(math.sqrt(2*num1/9.8))
    question = "What is the range of a ball shot horizontally off a %dm high cliff at %dm/s?,%2.2f" % (num1,num2,answer)
    return jsonify({"type":"proj1", "params":question})

@app.route("/kinematics")
def kinematics():
    num1 = random.randint(2,5)
    num2 = random.randint(2,5)
    num3 = random.randint(2,5)
    answer = num2*num1 + 0.5*num3*num1*num1
    question = "How far does a block slide in %d seconds travelling at %dm/s with acceleration %dm/s/s?,%2.2f" % (num1,num2,num3,answer)
    return jsonify({"type":"kin1", "params":question})
