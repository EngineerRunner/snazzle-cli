'''
snazzle command line interface
for all the arch users who are scared of GUIs
'''
from os.path import exists
import dazzle
import sys
import attachlib
import keyboard
import time
import os
session = None

logo = '''
 _______ __   __       ____       _____  _____  ___       _______                    __
 |  ___| | \  | |     / __ \     |___ | |___ |  |  |      | ____|               __  |__|
 |  |___ | |\ | |    / /__\ \       / /    / /  |  |      | |___       ______  |  |  __
 |___  | | |\\ | |   / /----\ \     / /    / /   |  |      |  ___|      | ___|  |  | |  |
 ___|  | | | \| |  / /      \ \   / /__  / /__  |  |_____ | |___       | |___  |  | |  |
|______| |_|  |_| /_/        \_\ |____| |____|  |_______| |_____|      |____|  |__| |__|  '''

# Functions
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def login(relog):
    global session
    global username
    if exists("session.txt") and not relog == True:
        print("Found saved login!")
        sessionfile = open("session.txt","r")
        details = sessionfile.read().split(",")
        username = details[0]
        sessionfile.close()
        try:
            session = attachlib.session_login(details[0],details[1])
        except:
            login(relog=True)
            return()
    else:
        username = input("enter your Scratch username.\n")
        print("log in with (P)assword or (S)ession ID? (this will save. if you want to delete the saved login or are on a shared computer, delete session.txt when it is created.)\n")
        key = keyboard.read_key()
        while not key == 'p' or key == 's':
            key = keyboard.read_key()
        time.sleep(0.05)
        if key == "p":
            password = input("now enter your Scratch Password.\n")
            try:
                session = attachlib.password_login(username,password)
            except:
                print("either something is wrong with Scratch, or you entered your username or password wrong. please try again.")
                login(username)
                return()
        else:
            sessionid = input("now enter your session ID.\n")
            try:
                session = attachlib.session_login(username,sessionid)
            except:
                print("either something is wrong with Scratch, or you entered your session ID or username wrong. please try again.")
                login()
                return()
    return()
# The code
if len(sys.argv) > 1:
    '''
    uhh i'll do this later.
    '''

#login
print(logo)

print("welcome to Snazzle CLI.")
print("attempting to log in..")
login(relog=False)
input(f"welcome, {username}! press any key to continue.")
clear()
#main menu
while True:
    print(logo)
    #print("view (p)roject details, a (u)ser profile or a (f)orum post.")
    #options = ['p','u','f']
    #key = keyboard.read_key()
    #while not key in options:
        #key = keyboard.read_key()
    project_id = ''
    while True:
        project_id = input("enter a project id")
        try:
            int(project_id)
        except:
            print("invalid id")
            continue
        break
    info = dazzle.get_project_info(project_id)
