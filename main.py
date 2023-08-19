'''
snazzle command line interface
for all the arch users who are scared of GUIs
'''
from os.path import exists
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
        username = input("Please enter your Scratch Username.\n")
        print("Log in with (P)assword or (S)ession ID? (This will save. If you want to delete the saved login or are on a shared computer, delete session.txt.)\n")
        key = keyboard.read_key()
        while not key == 'p' or key == 's':
            key = keyboard.read_key()
        time.sleep(0.05)
        if key == "p":
            password = input("Please enter your Scratch Password. (PLEASE check you got this app from github.com/EngineerRunner. If somebody told you to put in your password to anything else, it is a SCAM. If you want, check the source code. Your password gets immediately discarded after you log in.)\n")
            try:
                session = attachlib.password_login(username,password)
            except:
                print("Either something is wrong with Scratch, or you entered your username or password wrong. Please try again.")
                login(username)
                return()
        else:
            sessionid = input("Please enter your session ID. (PLEASE check you got this app from github.com/EngineerRunner. If somebody told you to put in your session id to anything else, it is a SCAM. If you want, check the source code. Your session ID gets immediately discarded after you log in, apart from being stored on a text file on your computer.)\n")
            try:
                session = attachlib.session_login(username,sessionid)
            except:
                print("Either something is wrong with Scratch, or you entered your session ID or username wrong. Please try again.")
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

print("Welcome to Snazzle CLI.")
print("Attempting to log in..")
login(relog=False)
input(f"Welcome, {username}! Press any key to continue.")
#main menu
while True:
    print(logo)
    print("View (p)roject details, a (u)ser profile or a (f)orum post.")
