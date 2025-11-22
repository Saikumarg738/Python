class singleton:

    _ins=None

    def __new__(cls):
        if(cls._ins is None):
            cls._ins=super().__new__(cls)
        return cls._ins

obj1=singleton()

obj2=singleton()

print(obj1 is obj2)

