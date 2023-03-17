from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123456@localhost/test'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))


# define a route
@app.route('/')
def index():
  return 'Hello World'
  
# Create a new user
@app.route('/user/<name>')
def create_user(name):  
  # execute a SQL query
  user = User(name=name,email=f'{name}@163.com')
  print(user)
  db.session.add(user)
  db.session.commit()
  return 'User created'

# Get all users
@app.route('/users')
def get_users():
  users = User.query.all()
  output = []
  for user in users:
    user_data = {'name': user.name, 'email': user.email}
    output.append(user_data)
  return {'users': output}

  
# filter a user by name
@app.route('/get_user/<name>')
def get_user(name):
  user = User.query.filter_by(name=name).first()
  if not user:
    return {'message': 'No user found!'}
  user_data = {'name': user.name, 'email': user.email}
  return {'user': user_data}

  
  # user = User.query.filter_by(name="John").first()
  # db.session.delete(user)
  # db.session.commit()
  
@app.route('/create_table')
def create_user_table():
  # if user table not exits, create it accroding to class User
  db.create_all()
  return 'User table created'

  


# run the app
if __name__ == '__main__':
  app.run(debug=True)