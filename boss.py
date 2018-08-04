from flask import Flask
import ind as f
import fin as g
import lin as h
import basic as b
import random
app = Flask(__name__)

@app.route("/boss/<topic>")
def boss_battle(topic):
	ret = ""
	if topic == "ind":
		# choose a random topic within indices
		r_int = random.randint(1, 5)
		if r_int == 1:
			#ret = str(r_int)
			ret += f.ind_1()

		elif r_int == 2:
			#ret = str(r_int)
			ret += f.indm_2()

		elif r_int == 3:
			#ret = str(r_int)
			ret += f.indm_3()

		elif r_int == 4:
			#ret = str(r_int)
			ret += f.indd_2()

		elif r_int == 5:
			#ret = str(r_int)
			ret += f.indp_2()

	elif topic == "fin":
		r_int = random.randint(1, 3)
		if r_int == 1:
			#ret = str(r_int)
			ret += g.fin_1()

		elif r_int == 2:
			#ret = str(r_int)
			ret += g.fin_2()

		elif r_int == 3:
			#ret = str(r_int)
			ret += g.fin_3()

	elif topic == "lin":
		r_int = random.randint(1, 2)
		if r_int == 1:
			#ret = str(r_int)
			ret += g.equations()

		elif r_int == 2:
			#ret = str(r_int)
			ret += g.gradients()

	elif topic == "basic":
		ret += b.basic()

	return ret
