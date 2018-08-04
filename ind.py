from flask import Flask
import random
app = Flask(__name__)

# Evaluate something to the power of something
@app.route("/ind1")
def qgen_ind_1():

	base = random.randint(0, 10)
	power = random.randint(0, 5)

	if base == 0 and power == 0:
		power = 1

	ans = base ** power

	ret = "ind1," + str(base) + "," + str(power) + "," + str(ans)
	return ret

# Creates questions for multiplication index law
# Simplify indices (base can be changed)
@app.route("/indm2")
def qgen_indm_2():

	base = random.randint(2, 10)
	power1 = random.randint(0, 20)
	power2 = random.randint(0, 20)

	ans = power1 + power2

	if base == 9:
		base_ans = 3
		ans *= 2
	elif base == 4:
		base_ans = 2
		ans *= 2
	else:
		base_ans = base

	ret = "indm2," + str(base) + "," + str(power1) + "," \
	+ str(base) + "," + str(power2) + "," + str(base_ans) + "," + str(ans)
	return ret

# Creates questions for multiplication index law
# Simplify indices (base can be changed)
@app.route("/indm3")
def qgen_indm_3():

	base = random.randint(2, 10)
	power1 = random.randint(0, 20)
	power2 = random.randint(0, 20)
	power3 = random.randint(0, 20)

	ans = power1 + power2 + power3

	if base == 9:
		base_ans = 3
		ans *= 2
	elif base == 4:
		base_ans = 2
		ans *= 2
	else:
		base_ans = base

	ret = "indm3," + str(base) + "," + str(power1) + "," \
	+ str(base) + "," + str(power2) + "," \
	+ str(base) + "," + str(power1) + "," \
	+ str(base_ans) + "," + str(ans)
	return ret

# Creates questions for division index law
# Simplify indices (keep base intact)
@app.route("/indd2")
def qgen_indd_2():

	base = random.randint(2, 10)
	power1 = random.randint(0, 20)
	power2 = random.randint(0, 20)

	ans = power1 - power2

	while power1 == power2:
		power2 = random.randint(0, 20)

	if base == 9:
		base_ans = 3
		ans *= 2
	elif base == 4:
		base_ans = 2
		ans *= 2
	else:
		base_ans = base

	ret = "indd2," + str(base) + "," + str(power1) + "," \
	+ str(base) + "," + str(power2) + "," + str(base_ans) + "," + str(ans)
	return ret

# Creates questions for power index law
@app.route("/indp2")
def qgen_indp_2():

	base = random.randint(2, 10)
	power1 = random.randint(0, 20)
	power2 = random.randint(0, 20)

	ans = power1 * power2

	if base == 9:
		base_ans = 3
		ans *= 2
	elif base == 4:
		base_ans = 2
		ans *= 2
	else:
		base_ans = base

	ret = "indp2," + str(base) + "," + str(power1) + "," \
	+ str(power2) + "," + str(base_ans) + "," + str(ans)
	return ret
