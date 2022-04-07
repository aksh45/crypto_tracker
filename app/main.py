from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def calculate():
	import requests
	import subprocess as s
	url = "https://api.coindcx.com/exchange/ticker"
	r = requests.get(url)
	d = {'CKBINR': [919,0.978],'CAKEINR':[1.309,685],'SOLINR':[0.0900,9690],'ETHINR':[0.00850,261000],'BTCINR':[0.00063042,3540000]}
	portfolio_value = 0
	invested_amount = 0
	results = []
	for x in r.json(): 
		if(x['market'] in d):
			current_price = (d[x['market']][0]*float(x['last_price']))
			invested_price = (d[x['market']][0]*d[x['market']][1])
			portfolio_value += current_price
			invested_amount += invested_price
			profit = ((current_price - invested_price) / invested_price)*100
			results.append([x['market'],current_price,invested_price,profit])
	total_profit = (((portfolio_value - invested_amount) / invested_amount )*100)
	# results.append([portfolio_value,invested_amount,total_profit])
	return render_template("index.html", coins = [results,[portfolio_value,invested_amount,total_profit]])