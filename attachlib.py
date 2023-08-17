import scratchattach as scratch3
from os.path import exists


session = None

def session_login(username,sessionid):
    global session
    session = scratch3.Session(sessionid,username=username)
    #sessionfile = open("session.txt","w")
    #sessionfile.write( [session.session_id , username] )
    return session

def password_login(username,password):
    global session
    session = scratch3.login(username,password)
    sessionfile = open("session.txt","w")
    id = session.session_id
    sessionfile.write(f'{username},{id}')
    sessionfile.close()
    return session