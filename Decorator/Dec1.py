

def deco(form):
    def wrapper():
        print("Before statement")
        form()
        print("After statement")
    return wrapper


def add():
    a=10
    b=10
    c=a+b
    print("The value of addition is {}".format(c))

vardeco=deco(add)  # Wrapper func object is returned to vardeco

vardeco()          # This will call wrapper