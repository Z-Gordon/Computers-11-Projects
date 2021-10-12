import json
import random
import string
import getpass

from helpers import *
# Gordon Zhou
# 9/13/2021 (Assignment 13)

def auth_user():
    username = input("Please provide a new or existing username: ")
    data = load_json()
    if not username in data:
        while True: #asks for password creation
            print(
                "Welcome! please give me a password or type 'r' for a random password." +
                "(password must be at least 8 characters and must have at least 1 capital letter, number, and punctuation mark): "
            )
            password = getpass.getpass()
            if password == 'r':  #chosen to create custom password
                password = rand_pass(
                    ask_for_number("how many characters?: "),
                    ask_for_number("how many capital letters?: "),
                    ask_for_number("how many numbers?: "),
                    ask_for_number("how many punctuation marks?: "),
                )
                print("your password is: "+password)
                break
            # determines if password is valid
            elif len(password) > 8 and not any(item in ['"', '\\'] for item in list(password)) and any(item in list(string.punctuation) for item in list(password)) and any(i in list(string.ascii_uppercase) for i in list(password)) and any(i in list(string.digits) for i in list(password)): 
                print("password is valid.")
                break
            else:
                print("invalid password, please try again.")
        # saves valid password
        json_obj = { username: {"password": password, "todolist": [] }}
        data.update(json_obj)
        dump_json(data)
    else: # username already exists
        while True:
            response = getpass.getpass(f"Password for <{username}>: ")
            if response == data[username]["password"]:
                print("correct.")
                break
            else:
                print("please try again.")
    return username