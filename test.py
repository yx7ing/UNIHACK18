from flask import Flask, render_template, request, jsonify
import random
import ind as I
import fin as F
import lin as L

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html', name=None)

@app.route("/basic")
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
