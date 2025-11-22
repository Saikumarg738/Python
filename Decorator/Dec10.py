def upp(sam):
    def wrap():
        val=sam()
        print(f"Upper case is name is {val.upper()}")
    return wrap

@upp
def word():
    return input("Enter name :")

word()