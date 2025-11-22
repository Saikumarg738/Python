def deco(fun):
    def wrap(time):
        for i in range(time):
            fun()

    return wrap


@deco
def hello():
    print("Hello Sai")

hello(3)