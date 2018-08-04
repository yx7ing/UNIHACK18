from flask import Flask
import random

app = Flask(__name__)

@app.route("/basic")
def basic():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    ans = a + b

    return "basic," + str(a) + "," + str(b) + "," + str(ans)
