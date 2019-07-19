from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world!'

'''Adding configuration for database'''
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="",
    hostname="127.0.0.1:3306",
    databasename="mijourneyevent",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Event(db.Model):
	__tablename__ = "events"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(80))
	start = db.Column(db.String(80))
	end = db.Column(db.String(80))
	
	def __init__(self, title, start, end):
		self.title = title
		self.start = start
		self.end = end

	@property
	def serialize(self):
		"""Return object data in easily serializable format"""
		return {
			'id': self.id,
			'title': self.title,
			'start': str(self.start),
			'end': str(self.end)
       }

@app.route('/createevent', methods = ['POST', 'GET'])
def createevent():
	if request.method == 'POST':
		data = request.get_json()
		event = Event(title=data["title"], start = data["start"], end = data["end"])
		db.session.add(event)
		db.session.commit()
		return redirect(url_for('createevent'))
	else:
		qryresult = Event.query.all()
		return jsonify([i.serialize for i in qryresult])
		
	

if __name__ == '__main__':
    app.run(debug=True, port=5001)