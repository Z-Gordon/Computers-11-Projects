from accounts import auth_user
from todolist import ToDoList

from helpers import *

if __name__ == "__main__":
    username = auth_user()
    while True:
        my_list = ToDoList(username)

        if my_list.to_do_list == []:
            response = input("\nWelcome to 'TODOLIST'! to get started, type 'help' for a list of commands: ")
        else:
            response = input("\nGive me a command: ")

        if response == "help":
            print(my_list.help_text)
        elif response == my_list.commands[0][0]: 
            my_list.add_task()

        elif response == my_list.commands[1][0]:
            task_index = my_list.select_a_task("Respond with the number of the task you'd like to delete: ") 
            my_list.del_task(task_index)
            
        elif response == my_list.commands[2][0]: 
            my_list.clear_all()

        elif response == my_list.commands[3][0]:
            task_index = my_list.select_a_task("Respond with the number of the task you would like to edit: ")
            subfield = my_list.select_a_subfield("Give the command for the subfield you would like to edit: ") 
            my_list.edit_task(task_index, subfield)

        elif response == my_list.commands[4][0]:
            list_display = my_list.display_tasks()
            print(list_display)

        elif response == my_list.commands[5][0]: 
            subfield = my_list.select_a_subfield("Give the command for the subfield you would like to sort by: ")
            my_list.sort_list(subfield)

        elif response == my_list.commands[6][0]:
            exit()

        else:
            print("Command not found. (type 'help' for a list of commands?)")
        dump_json(my_list.data)


