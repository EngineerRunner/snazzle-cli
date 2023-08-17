import scratchattach as scratch3
from os.path import exists
session = None
def session_login(username,sessionid):
    global session
    session = scratch3.Session(sessionid,username=username)
    sessionfile = open("session.txt","w")
    sessionfile.write( [session.session_id , username] )
    return session