
def create(name,**dict):
    a={"hesaru":name}
    a.update(dict)
    print(a)

create("Sai",age="27",job="SE",loc="Hyd")