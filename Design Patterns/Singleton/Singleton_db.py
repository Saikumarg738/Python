class singleton_db:
    _insvar=None

    def __new__(cls):
        if cls._insvar is None:
            cls._insvar=super().__new__(cls)
        return cls._insvar

