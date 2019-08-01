from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world!'

'''Adding configuration for database'''
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="Fong1029$",
    hostname="127.0.0.1:3306",
    databasename="mijourneyevent",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Route(db.Model):
	__tablename__ = "routes"
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(80))
	create_route = db.Column(db.String(80))
	view_route = db.Column(db.String(80))
	
	def __init__(self, email, create_route, view_route):
		self.email = email
		self.create_route = create_route
		self.view_route = view_route

	@property
	def serialize(self):
		"""Return object data in easily serializable format"""
		return {
			'id': self.id,
			'email': self.email,
			'create_route': str(self.create_route),
			'view_route': str(self.view_route)
       }

@app.route('/routemanagement', methods = ['POST', 'GET'])
def createevent():
	if request.method == 'POST':
		data = request.get_json()
		route = Route(email=data["email"], create_route = data["create_route"], view_route = data["view_route"])
		db.session.add(route)
		db.session.commit()
		return redirect(url_for('routemanagement'))
	else:
		qryresult = Route.query.all()
		return jsonify([i.serialize for i in qryresult])
		
	

if __name__ == '__main__':
    app.run(debug=True, port=5002)