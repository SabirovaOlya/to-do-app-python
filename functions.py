import hashlib
import json
from datetime import datetime
from User import User, get_users
from Task import Task, get_tasks


def registration():
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    email = input("Enter your email: ")
    password = sha256_hash(input("Enter your password: "))

    user = User(name, username, email, password)
    return user.register_user()


def login():
    users: list = get_users()
    username = input("Enter your username: ")
    password = sha256_hash(input("Enter your password: "))

    for user in users:
        if user['username'] == username:
            if user['password'] == password:
                print("Successfully Login!!!")
                return user['id']
            else:
                print("Wrong password!!!")
                return 0

    print("There no such user!!!")
    return 0


def add_new_task(user_id):
    text = input("Enter a text: ")
    expires_at = input("Enter deadline date(dd-mm-yyyy): ")

    task = Task(text, expires_at, user_id)
    return task.add_task()


def get_user_tasks(user_id):
    tasks: list = get_tasks()
    user_tasks = []
    for task in tasks:
        if task['user_id'] == user_id:
            user_tasks.append(task)
    return user_tasks


def show_all_tasks(user_id):
    user_tasks = get_user_tasks(user_id)
    ind = 0
    print("---------------")
    for task in user_tasks:
        ind += 1
        print(f"{ind}. {task['text']} ({task['expires_at']})")
    if ind == 0:
        print("There no tasks")


def show_expired_tasks(user_id):
    user_tasks = get_user_tasks(user_id)
    ind = 0
    print("---------------")
    for task in user_tasks:
        if not is_date_greater_than_today(task['expires_at']):
            ind += 1
            print(f"{ind}. {task['text']} ({task['expires_at']})")
    if ind == 0:
        print("There no tasks")


def delete_task(user_id, ind):
    tasks: list = get_user_tasks(user_id)
    all_tasks: list = get_tasks()

    if len(tasks) < ind:
        print("There no such task")
        return

    del_ind = 0
    count = 0
    for t in all_tasks:
        count += 1
        if t['id'] == tasks[ind-1]['id']:
            del_ind = count
    all_tasks.pop(del_ind-1)

    with open('tasks.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)
        print("Successfully deleted!!!")
        return True


def edit_task(user_id, ind):
    tasks: list = get_user_tasks(user_id)
    all_tasks: list = get_tasks()

    if len(tasks) < ind:
        print("There no such task")
        return

    edit_ind = 0
    count = 0
    for t in all_tasks:
        count += 1
        if t['id'] == tasks[ind - 1]['id']:
            edit_ind = count

    text = input("Enter a text: ")
    expires_at = input("Enter deadline date(dd-mm-yyyy): ")
    all_tasks[edit_ind-1]['text'] = text
    all_tasks[edit_ind-1]['expires_at'] = expires_at

    with open('tasks.json', 'w') as file:
        json.dump(all_tasks, file, indent=4)
        print("Successfully edited!!!")
        return True


def is_date_greater_than_today(date_string):
    input_date = datetime.strptime(date_string, "%d-%m-%Y").date()
    today = datetime.now().date()

    return input_date >= today


def sha256_hash(input_string):
    encoded_string = input_string.encode('utf-8')
    sha256_hash_object = hashlib.sha256()
    sha256_hash_object.update(encoded_string)
    hashed_string = sha256_hash_object.hexdigest()

    return hashed_string
