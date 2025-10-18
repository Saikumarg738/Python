class main:
    def __init__(self):
        print("Hello Sai!",end="")
class sub1(main):
    def __init__(self):
        super().__init__()
        print("How are you?")
class sub2(main):
    def __init__(self):
        super().__init__()
        print("How is your day going?")

d=sub1()
e=sub2()