'''
snazzle command line interface
for all the arch users who are scared of GUIs
'''
from os.path import exists
import sys
import attachlib
import keyboard
session = None


# Functions

def login(username,relog):
    global session
    if exists("session.txt") and not relog == True:
        sessionfile = open("session.txt","r")
        details = sessionfile.read().split(",")
        try:
            session = attachlib.session_login(details[0],details[1])
        except:
            login(relog=True,username=username)
            return()
    else:
        print("Log in with (P)assword or (S)ession ID")
        event = keyboard.read_event()
        while not event.event_type == keyboard.KEY_DOWN and event.name == "p" or event.event_type == keyboard.KEY_DOWN and event.name == "s":
            event  = keyboard.read_event()
            output = event.name
        if output == "p":
            password = input("Please enter your Scratch Password.\n(PLEASE check you got this app from github.com/EngineerRunner. If somebody told you to put in your password to anything else, it is a SCAM. If you want, check the source code. Your password gets immediately discarded after you log in.)")
            try:
                session = attachlib.password_login(username,password)
            except:
                print("Either something is wrong with Scratch, or you entered your password wrong. Please try again.")
                login(username)
                return()
        else:
            sessionid = input("Please enter your session ID.\n(PLEASE check you got this app from github.com/EngineerRunner. If somebody told you to put in your session id to anything else, it is a SCAM. If you want, check the source code. Your session ID gets immediately discarded after you log in, apart from being stored on a text file on your computer.)")
            try:
                session = attachlib.session_login(username,sessionid)
            except:
                print("Either something is wrong with Scratch, or you entered your session ID wrong. Please try again.")
                login(username)
                return()
    return()
# The code
if len(sys.argv) > 1:
    '''
    uhh i'll do this later.
    '''

print('''
 _______ __   __       ____       _____  _____  ___       _______                    __
 |  ___| | \  | |     / __ \     |___ | |___ |  |  |      | ____|               __  |__|
 |  |___ | |\ | |    / /__\ \       / /    / /  |  |      | |___       ______  |  |  __
 |___  | | |\\ | |   / /----\ \     / /    / /   |  |      |  ___|      | ___|  |  | |  |
 ___|  | | | \| |  / /      \ \   / /__  / /__  |  |_____ | |___       | |___  |  | |  |
|______| |_|  |_| /_/        \_\ |____| |____|  |_______| |_____|      |____|  |__| |__|  ''')

print("Welcome to Snazzle CLI.")