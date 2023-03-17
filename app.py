from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from exts import db
from models import Person
import config

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root123456@localhost/test'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(config)
db.init_app(app)


# define a route
@app.route('/')
def index():
  return 'Hello World'  

# create person table
@app.route('/create_person_table')
def create_person_table():
    db.create_all()
    return 'Person table created'
  
# Get all persons 
@app.route('/persons')
def get_persons():
    persons = Person.query.all()
    output = []
    for person in persons:
        person_data = {'id': person.id, 'name': person.name, 'email': person.email}
        output.append(person_data)

    return jsonify({'persons': output})

# Get single person
@app.route('/person/<id>')
def get_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({'message': 'No person found'})
    else:
        person_data = {'id': person.id, 'name': person.name, 'email': person.email}
        return jsonify({'person': person_data})

#Get person by name
@app.route('/person/name/<name>')
def get_person_by_name(name):
    person = Person.query.filter_by(name=name).first()
    if not person:
        return jsonify({'message': 'No person found'})
    else:
        person_data = {'id': person.id, 'name': person.name, 'email': person.email}
        return jsonify({'person': person_data})

# Add new person
@app.route('/person', methods=['POST'])
def add_person():
    data = request.get_json()
    print(data)
    new_person = Person(name=data['name'], email=data['email'])
    db.session.add(new_person)
    db.session.commit()
    return jsonify({'message': 'New person added'})

# Update person
@app.route('/person/<id>', methods=['PUT'])
def update_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({'message': 'No person found'})
    
    data = request.get_json()
    
    person.name = data['name']
    person.email = data['email']
    
    db.session.commit()
    
    return jsonify({'message': 'Person updated'})



# Delete person
@app.route('/person/<id>', methods=['DELETE'])
def delete_person(id):
    person = Person.query.get(id)
    if not person:
        return jsonify({'message': 'No person found'})
    
    db.session.delete(person)
    db.session.commit()
    
    return jsonify({'message': 'Person deleted'})


# run the app
if __name__ == '__main__':
  app.run(debug=True)