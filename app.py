from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/test'
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
  
# @app.route('/user/<name>')  
# def create_user(name):
#     # execute a SQL query
#   # user = User(name="John", email="john@example.com")
#   user = User(name=name, email=f'{name}@163.com')
#   print(user)
#   db.session.add(user)
#   db.session.commit()
  
  # users = User.query.all()
  # user = User.query.filter_by(name="John").first()
  # user.email = "new-email@example.com"
  # db.session.commit()
  
  # user = User.query.filter_by(name="John").first()
  # user.email = "new-email@example.com"
  # db.session.commit()
  
  
  # user = User.query.filter_by(name="John").first()
  # db.session.delete(user)
  # db.session.commit()
  
@app.route('/user')
def create_user_table():
  # if user table not exits, create it accroding to class User
  db.create_all()
  return 'User table created'

  


# run the app
if __name__ == '__main__':
  app.run(debug=True)
