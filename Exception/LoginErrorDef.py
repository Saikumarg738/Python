from LoginException import *

def checkcred(user,passw):
    if(user!='admin' or passw!='root1234'):
        raise InvalidLoginException