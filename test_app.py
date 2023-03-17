
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
    
    
    
    
    
    

    


        
    
