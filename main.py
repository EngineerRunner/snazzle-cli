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

def login():
    global session
    if exists("session.txt"):
        sessionfile = open("session.txt","r")
        details = sessionfile.read().split(",")
        session = attachlib.session_login(details[0],details[1])
    else:

# The code
if len(sys.argv) > 1:
    '''
    uhh i'll do this later.
    '''
