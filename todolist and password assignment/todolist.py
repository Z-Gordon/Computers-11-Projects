from helpers import *
import datetime

# Gordon Zhou
# (Assignment 21)
class ToDoList:
    def __init__(self, username):
        self.username = username
        self.data = load_json()
        self.to_do_list = self.data[self.username]['todolist']
        # commands in element 0, descriptions in element 1
        self.commands = [ 
            ["add", "add a task"], 
            ["del", "delete a task"], 
            ["delall", "clear all tasks"],
            ["edit", "edit a task's subfield"],
            ["show", "shows your To Do list"],
            ["sort", "sorts your To Do list based on a specific subfield"],
            ["exit", "saves and exits the program"]
        ]
        self.help_text = "--COMMAND LIST--"
        for command in self.commands:
            self.help_text += f"\n<{command[0]}> - {command[1]} "

    def display_tasks(self):
        # makes to do list look prettier
        my_list = self.to_do_list
        display = ""
        for i, task in enumerate(my_list):
            if task["status"]:
                status = "completed"
            else:
                status = "uncompleted"
            display +=f"\n{i+1}. ({status}) --{task['title'].upper()}-- ({task['priority']}/5 priority)\n     -{task['description']}"
            if task["due_date"]:
                display += f"\n     -Due Date: {task['due_date']}"
        return display

    def sort_list(self, subfield):
        print("Sorting by " + subfield)
        sorted_list = sorted(self.to_do_list, key=lambda k: k[subfield])
        self.data[self.username]['todolist'] = sorted_list

    def add_task(self):
        #asks for task's name
        while True: 
            title = input("What's this task's title? ")
            if title != "": break

        # asks for description, defaults to "(none)" if no input
        description = input("Description? ") 
        if description == "": description == "(none)"

        # asks for priority, it must only be a number between 1 and 5
        while True:
            priority = ask_for_number("How important is this task? (1-5): ")
            if int(priority) in range(1,6):
                break

        new_task = { 
            "title": title, 
            "description": description, 
            "due_date": "", 
            "status": False, 
            "priority": priority
        }
        self.data[self.username]['todolist'].append(new_task)
        print(f"'{title}' has been added to your list.")

    def del_task(self, task_index):
        self.data[self.username]['todolist'].pop(task_index)              
        print("Task has been removed.")

    def edit_task(self, task_index, subfield):
        if subfield == "status":
            status = not self.to_do_list[task_index]["status"]
            self.data[self.username]['todolist'][task_index]["status"] = status
            print("changing status to " + str(status))

        elif subfield == "priority":
            while True:
                priority = ask_for_number("How important is this task? (1-5): ")
                if int(priority) in range(1,6):
                    break
            self.data[self.username]['todolist'][task_index]["priority"] = priority
            print("Priority has been updated.")

        elif subfield == "title":
            title = input("New title: ")
            self.data[self.username]['todolist'][task_index]["title"] = title
            print("Title updated.")

        elif subfield == "description":
            description = input("New description: ")
            self.data[self.username]['todolist'][task_index]["description"] = description
            print("Description updated.")

        elif subfield == "due_date":
            while True:
                year = ask_for_number("Year? ")
                month = ask_for_number("Month? ")
                day = ask_for_number("Day? ")
                try:
                    due_date = datetime.datetime(year, month, day).date()
                except:
                    print("Invalid date!")
                    continue
                break
            self.data[self.username]['todolist'][task_index]["due_date"] = str(due_date)
            print("Due Date updated.")

    def clear_all(self):
        response = input("respond with 'YES' to confirm you would like to delete ALL of your tasks: ")
        if response == "YES":
            self.data[self.username]['todolist'] == []
        print("deleting all tasks")
        return
    
    def select_a_subfield(self, prompt):
        sub_commands = [
            ['t', 'title'], 
            ['d', 'description'], 
            ['dd', 'due_date'], 
            ['s', 'status'], 
            ['p', 'priority']]
        text = ""
        for sub in sub_commands:
            text += f"\n'{sub[0]}' - {sub[1]}"

        while True: #asks for user to select a subfield by command
            subfield = input(text+"\n"+prompt)
            if subfield in [sub[0] for sub in sub_commands]:
                break

        # returns name of subfield
        index = [s[0] for s in sub_commands].index(subfield)
        return sub_commands[index][1]

    def select_a_task(self, prompt):
        if len(self.to_do_list) == 0: # doesn't do anything if to do list is empty
            print("You don't have any tasks!")
            return

        # displays task's title, along with their index
        task_names = [task["title"] for task in self.to_do_list]
        text = ""
        for i, name in enumerate(task_names):
            text += f"{i} - {name}\n"
        while True:
            task_index = ask_for_number(text+"\n"+prompt)
            if int(task_index) in range(0, len(task_names)): break

        # returns index of task in to do list
        return task_index
