x=25
y=35
z=45

def sam():
    d=globals()
    for a,b in d.items():
        print("Key = {} | Value = {}".format(a,b))

sam()