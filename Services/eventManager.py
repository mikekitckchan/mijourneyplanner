from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world!'

@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		return redirect(url_for('create', startdate=startdate, enddate=enddate))


@app.route('/create', methods = ['GET', 'POST'])
def create():
	if request.method == 'GET':
		startdate=request.args.get("startdate")
		enddate=request.args.get("enddate")
		print(startdate)
		print(enddate)
		return render_template("create.html", startdate=startdate, enddate=enddate)
	else:
		data = request.get_json()
		print(data)
		return redirect(url_for('index'))
	

if __name__ == '__main__':
    app.run(debug=True, port=5001)