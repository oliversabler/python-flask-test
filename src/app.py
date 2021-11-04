from flask import Flask, jsonify, request

app = Flask(__name__)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)

users = [
  {
    'username': 'Johnny',
    'password': 'Yo'
  },
  {
    'username': 'Abby',
    'password': 'Gale'
  }
]

@app.route('/')
def index():
  return 'yo'

@app.route('/user/', methods=['POST'])
def create_user():
  users.append(request.get_json())
  return '', 204

@app.route('/user/<string:username>')
def read_user(username):
  for user in users:
    if user['username'].lower() == username.lower():
      return jsonify(user)

@app.route('/user/list')
def read_users():
  return jsonify(users)