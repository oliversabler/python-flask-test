from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host.docker.internal:5432/user_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

db = SQLAlchemy(app)

# User
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)
  created_date = db.Column(db.DateTime(), default=datetime.utcnow)

  def __repr__(self):
      return '<User %r>' % self.username

  @property
  def serialize(self):
    return {
      'id': self.id,
      'username': self.username,
      'password': self.password,
      'created_date': self.created_date
    }

# Create db
db.create_all()

# Endpoints
@app.route('/')
def index():
  return 'yo'

@app.route('/user/', methods=['POST'])
def create_user():
  user = User(username='test', password='test')
  db.session.add(user)
  db.session.commit()
  return '', 204

@app.route('/user/<string:username>')
def read_user(username):
  user = User.query.filter_by(username='test').first()
  return jsonify(user.serialize)

@app.route('/user/list')
def read_users():
  users = User.query.all() 
  return jsonify(json_list=[u.serialize for u in users])