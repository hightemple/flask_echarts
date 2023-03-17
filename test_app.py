import random

import requests



def test_add_persons():
    url = "http://127.0.0.1:5000/person"
    data = {'name': 'Mike', 'email': '111@163.com'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    print(response)
    print(response.status_code)
    print(response.content)


def test_get_persons():
    url = "http://127.0.0.1:5000/persons"
    response = requests.get(url)
    
    print(response.status_code)
    # print(response.content)

    data = response.json()
    for person in data['persons']:
        print(person['name'])
        print(person['email'])
        print(person['id'])
        print('-'*10)
    

# query person by id
def test_get_person_by_id():
    id = 3
    url = "http://127.0.0.1:5000/person/{}".format(id)
    response = requests.get(url)

    print(response.status_code)
    # print(response.content)

    data = response.json()
    print(data)


def test_get_person_by_name():
    url = "http://127.0.0.1:5000/person"
    name = "tester" + str(random.randint(1, 100))
    info = {'name': name, 'email': name + '@163.com'}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=info, headers=headers)
    assert response.status_code == 200

    query_url =  url + "/name/{}".format(info['name'])
    response = requests.get(query_url)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data['person']['name'] == info['name']
    assert data['person']['email'] == info['email']

    # delete person by name
    delete_url = url + "/{}".format(data['person']['id'])
    response = requests.delete(delete_url)
    assert response.status_code == 200











    
    
    

    


        
    
