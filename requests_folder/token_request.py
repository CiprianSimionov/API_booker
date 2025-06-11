import requests
# from requests.auth import HTTPBasicAuth

# response = requests.post('https://restful-booker.herokuapp.com/auth', auth=HTTPBasicAuth('admin', 'password123'))


def generate_token():
    data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", json=data)
    return response

