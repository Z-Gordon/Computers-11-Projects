import random
import string
import json

PATH = "C:/Users/993192/OneDrive - Board of Education of SD 39 (Vancouver)/Computers 11/Python 1 projects/todolist and password assignment/accounts.json"

def rand_pass(num_chars, num_caps, num_numbers, num_punc):
    chars = []
    for i in range(num_chars): 
        chars.append(random.choice(string.ascii_lowercase))
    for i in range(num_caps): 
        chars.append(random.choice(string.ascii_uppercase))
    for i in range(num_numbers):  
        chars.append(random.choice(string.digits))
    for i in range(num_punc):
        punc = random.choice("@?><^&*+_$#@!~`|/.,;:=-()")
        chars.append(punc)
    random.shuffle(chars)
    return ''.join(chars)

def check_if_int(input):
    try:
        int(input)
    except:
        return False
    return True

def ask_for_number(prompt):
    response = input(prompt)
    if not check_if_int(response):
        ask_for_number(prompt)
    else:
        return int(response)

def dump_json(data):
    with open(PATH, 'w') as outfile:
        json.dump(data, outfile) 

def load_json():
    with open(PATH, "r") as f:
        return json.load(f)