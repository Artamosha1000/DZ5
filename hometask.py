from flask import Flask

app = Flask(__name__)

users =[
    {
        "id": 1,
        "name": "Mike",
        "age": 7,
    },

    {
        "id": 2,
        "name": "Nick",
        "age": 17,
    },

    {
        "id": 3,
        "name": "Brian",
        "age": 27,
    },

    {
        "id": 4,
        "name": "Adam",
        "age": 37,
    }



]


@app.route('/users')
def get_all_users():
    global ALL_USERS
    response = ''
    for user in users:
        response += f'<a href="/user/{user["id"]}"><h1>{user["name"]},{user["id"]}</h1></a><p>{user["age"]}</p>'
    return response

@app.route('/users/<int:id>')
def get_users_id(id: int):
    for user in users:
        if user['id'] == id:
            return f'<h1>{user["name"]}</h1><p>{user["age"]}</p>'
    return '<p style="color:red;">Users not found</p>'

app.run("localhost",8000)



