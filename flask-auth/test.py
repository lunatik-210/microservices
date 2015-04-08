import requests
from time import sleep
from base64 import b64encode

url = "http://localhost:5000/v1"

def post_users(token):
    headers = { 'Authorization': 'Basic {0}'.format(b64encode('{0}:'.format(token))) }
    for i in range(10):
        email = "andrew.d.lapin{0}@gmail.com".format(i)
        user = dict(email=email, password="root")
        requests.post(url+"/users", data=user, headers=headers)

def get_users(token):
    headers = { 'Authorization': 'Basic {0}'.format(b64encode('{0}:'.format(token))) }
    users = requests.get(url+"/users", headers=headers)
    return users.json()['result']['data']

def delete_users(token, users):
    headers = { 'Authorization': 'Basic {0}'.format(b64encode('{0}:'.format(token))) }
    for user in users:
        if user['email'] != "andrew.d.lapin@gmail.com":
            requests.delete(url + "/users/" + str(user['id']), headers=headers)

if __name__ == "__main__":
    headers = { 'Authorization': 'Basic {0}'.format(b64encode('andrew.d.lapin@gmail.com:root')) }
    r = requests.get(url+"/token", headers=headers)
    token = r.json().get('result').get('token')
    refresh_token = r.json().get('result').get('refresh_token')

    #headers = { 'Authorization': 'Basic {0}'.format(b64encode('{0}:{1}'.format(token, refresh_token))) }
    #r = requests.get(url+"/refresh_token", headers=headers)    
    #token = r.json().get('result').get('token')

    post_users(token)
    users = get_users(token)
    delete_users(token, users)
