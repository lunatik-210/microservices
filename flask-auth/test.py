import requests

url = "http://localhost:5000/v1"

def post_users():
    for i in range(10):
        email = "andrew.d.lapin{0}@gmail.com".format(i)
        user = dict(email=email, password="root")
        requests.post(url+"/users", data=user)

    email = "andrew.d.lapin@gmail.com"
    user = dict(email=email, password="root")
    requests.post(url+"/users", data=user)

def get_users():
    users = requests.get(url+"/users")
    return users.json()['result']['data']

def delete_users(users):
    for user in users:
        requests.delete(url + "/users/" + str(user['id']))

if __name__ == "__main__":
    post_users()
    users = get_users()
    delete_users(users)
