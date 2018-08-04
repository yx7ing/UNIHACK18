from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def question():
    q_type = random.randint(1,4)
    var_question = ""
    if q_type == 1:
        P = random.randint(100,40000)
        R = random.randint(2,9)
        N = random.randint(2,20)
        I = "%0.2f" % (P*R*N/100)
        time = random.randint(1,3)
        if time == 1:
            var_question = "calculate simple interest where principal is $"+str(P)+" and the interest rate is "+str(R)+"% per month over "+str(N)+"months"
            return "fin,"+var_question+","+str(I)
        elif time == 2:
            var_question = "calculate simple interest where principal is $"+str(P)+" and the interest rate is "+str(R)+"% per year over "+str(N)+"years"
            return "fin,"+var_question+","+str(I)
    elif q_type == 2:
        R = random.randint(10,15)
        N = random.randint(10,20)
        I = random.randint(130,5000)
        P = "%0.2f" % (I*100/(R*N))
        time = random.randint(1,3)
        if time == 1:
            var_question = "calculate the principal needed to earn interest of $"+str(I)+" when simple interest rate is "+str(R)+"% per month over "+str(N)+"months"
            return "fin,"+var_question+","+str(P)
        elif time == 2:
            var_question = "calculate the principal needed to earn interest of $"+str(I)+" when simple interest rate is "+str(R)+"% per year over "+str(N)+"years"
            return "fin,"+var_question+","+str(P)
    elif q_type == 3:
        P = random.randint(100,4000)
        R = random.randint(2,9)
        N = random.randint(2,20)
        A = "%0.2f" % (P*((1+(R/100))**N))
        time = random.randint(1,3)
        if time == 1:
            var_question = "find compound interest where $"+str(P)+" is the principal and "+str(R)+"% is the interest rate per compounding month and for "+str(N)+"months"
            return "fin,"+var_question+","+str(A)
        elif time == 2:
            var_question = "find compound interest where $"+str(P)+" is the principal and "+str(R)+"% is the interest rate per compounding year and for "+str(N)+"years"
            return "fin,"+var_question+","+str(A)

    return "error"
