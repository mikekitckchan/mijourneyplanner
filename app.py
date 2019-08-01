from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from . import fullcalendartools as ft
import json
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world!'


@app.route('/', methods = ['GET', 'POST'])
def index():
	if request.method == 'GET':
		return render_template("index.html")
	else:
		email = request.form['email']
		startdate = request.form['startdate']
		enddate = request.form['enddate']
		return redirect(url_for('create', startdate=startdate, enddate=enddate))


@app.route('/create/<int:routeid>', methods = ['GET', 'POST'])
def create(routeid):
	if request.method == 'GET':
		startdate=request.args.get("startdate")
		enddate=request.args.get("enddate")
		return render_template("create.html", startdate=startdate, enddate=enddate)
	else:
		data = request.get_json()
		data= ft.getevent(data)
		for items in data:
			print(items)
			title = items['title']
			start = items['start']
			end = items['end']
			r = requests.post("http://127.0.0.1:5001/eventmanagement", json={"title": title, "start": start, "end": end})
		return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)