import json


def get_users():
    try:
        with open('users.json') as file:
            users: list = json.load(file)
            return users
    except(FileNotFoundError, json.JSONDecodeError):
        with open('users.json', 'w') as file:
            json.dump([], file)
            return []


class User:
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def user_exists(self):
        users: list = get_users()
        for user in users:
            if user['username'] == self.username or user['email'] == self.email:
                return True
        return False

    def register_user(self):
        if self.user_exists():
            print("User already exists")
            return False

        new_user = {
            'id': 1 if len(get_users()) == 0 else get_users()[-1]['id'] + 1,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }

        users: list = get_users()
        users.append(new_user)

        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)
            print("Successfully registered!!!")
            return True
