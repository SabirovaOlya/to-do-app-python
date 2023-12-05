from User import get_users
from functions import registration, login, add_new_task, show_all_tasks, show_expired_tasks, delete_task, edit_task, get_user_tasks


def single_options(user_id):
    while True:
        print("----------------")
        print("1. Edit task")
        print("2. Delete task")
        print("3. Back")

        ans_3 = int(input("Select: "))

        if ans_3 == 1:
            edit_ind = int(input("Enter index: "))
            edit_task(user_id, edit_ind)
        if ans_3 == 2:
            del_ind = int(input("Enter index: "))
            delete_task(user_id, del_ind)
        break


while True:
    print("1. Registration")
    if len(get_users()) != 0:
        print("2. Login")

    ans_1 = int(input("Select: "))
    user_id = 0
    registration_status = False

    if ans_1 == 1:
        registration_status = registration()
        if registration_status:
            print()
            print("You need login to enter to the system")
            user_id = login()
    if ans_1 == 2:
        user_id = login()

    if user_id == 0:
        print("Try again!!!")
        print()

    if user_id != 0:

        while True:
            print("------------------")
            print("1. Add new task")
            print("2. Show all my tasks")
            print("3. Show my expired tasks")
            print("4. Back")

            ans_2 = int(input("Select: "))

            if ans_2 == 1:
                add_new_task(user_id)
            if ans_2 == 2:
                arr = get_user_tasks(user_id)
                show_all_tasks(user_id)
                if len(arr) != 0:
                    single_options(user_id)
            if ans_2 == 3:
                show_expired_tasks(user_id)
            if ans_2 == 4:
                user_id = 0
                break
