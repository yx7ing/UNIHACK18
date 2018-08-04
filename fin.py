from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/fin1")
def fin_1():
    P = random.randint(100,40000)
    R = random.randint(2,9)
    N = random.randint(2,20)
    I = "%0.2f" % (P*R*N/100)
    time = random.randint(1,2)
    if time == 1:
        var_question = "Calculate the simple interest where the principal is $"+str(P)+" and the interest rate is "+str(R)+"% per month over "+str(N)+" months."
        return jsonify({"type":"fin", "params":var_question+","+str(I)})
    elif time == 2:
        var_question = "Calculate the simple interest where the principal is $"+str(P)+" and the interest rate is "+str(R)+"% per year over "+str(N)+" years."
        return jsonify({"type":"fin", "params":var_question+","+str(I)})


@app.route("/fin2")
def fin_2():
    R = random.randint(10,15)
    N = random.randint(10,20)
    I = random.randint(130,5000)
    P = "%0.2f" % (I*100/(R*N))
    time = random.randint(1,2)
    if time == 1:
        var_question = "Calculate the principal needed to earn interest of $"+str(I)+" when simple interest rate is "+str(R)+"% per month over "+str(N)+" months"
        return jsonify({"type":"fin", "params":var_question+","+str(P)})
    elif time == 2:
        var_question = "Calculate the principal needed to earn interest of $"+str(I)+" when simple interest rate is "+str(R)+"% per year over "+str(N)+" years"
        return jsonify({"type":"fin", "params":var_question+","+str(P)})

@app.route("/fin3")
def fin_3():
    P = random.randint(100,4000)
    R = random.randint(2,9)
    N = random.randint(2,20)
    A = "%0.2f" % (P*((1+(R/100))**N))
    time = random.randint(1,2)
    if time == 1:
        var_question = "Find the compound interest where $"+str(P)+" is the principal and "+str(R)+"% is the interest rate per compounding month and for "+str(N)+" months"
        return jsonify({"type":"fin", "params":var_question+","+str(A)})
    elif time == 2:
        var_question = "Find the compound interest where $"+str(P)+" is the principal and "+str(R)+"% is the interest rate per compounding year and for "+str(N)+" years"
        return jsonify({"type":"fin", "params":var_question+","+str(A)})
