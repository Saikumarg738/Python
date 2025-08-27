from NameException import ZeroLenght, InvalidName, EmptyName

def checkname(name):
    if (len(name)==0):
        raise ZeroLenght
    elif(name.isspace()):
        raise EmptyName
    else:
        ans=True
        a=name.split()
        for r in a:
            if (not r.isalpha()):
                ans=False
                break
        if(ans):
            return name
        else:
            raise InvalidName


