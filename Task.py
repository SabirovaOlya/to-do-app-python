import json


def get_tasks():
    try:
        with open('tasks.json') as file:
            tasks: list = json.load(file)
            return tasks
    except(FileNotFoundError, json.JSONDecodeError):
        with open('tasks.json', 'w') as file:
            json.dump([], file)
            return []


class Task:
    def __init__(self, text, expires_at, user_id):
        self.text = text
        self.expires_at = expires_at
        self.user_id = user_id

    def add_task(self):
        new_task = {
            'id': 1 if len(get_tasks()) == 0 else get_tasks()[-1]['id'] + 1,
            'text': self.text,
            'expires_at': self.expires_at,
            'user_id': self.user_id
        }

        tasks: list = get_tasks()
        tasks.append(new_task)

        try:
            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)
                print("Successfully created!!!")
                return True
        except(FileNotFoundError, json.JSONDecodeError):
            print("Error... try again!!!")
            return False
