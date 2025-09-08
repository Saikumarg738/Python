class Account:
    def __init__(self):
        self.__accno = 1234
        self.accname = "Sai"
        self.__accbal = "349"
        self.__accpin = 9424
        self.branch = "Hitech city"
    def getaccno(self):
        print("Account number is : ",self.__accno)
    def getpin(self):
        return self.__accpin

