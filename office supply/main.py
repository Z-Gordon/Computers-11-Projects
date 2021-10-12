from typing import Dict


file = open("office supply/officesupply.txt")

lines = file.readlines()

user_history = {}
for i, line in enumerate(lines):
    name = line.split(",")[6]
    if name not in user_history:
        user_history[name] = [i]
    else:
        user_history[name].append(i)

def get_lines(name):
    purchase_lines = user_history[name]
    return [lines[line_num] for line_num in purchase_lines]

def get_recommendations(name):
    purchases = get_lines(name)
    

while True:
    name = input("Welcome, what is your name?")
    if name in user_history.keys():
        get_recommendations(name)
        

    
