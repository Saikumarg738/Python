class circle:
    @classmethod
    def pidef(cls):
        cls.pi=3.14
    def getvalue(self):
        self.val=float(input("Enter number : "))
    def cal(self):
        circle.pidef()
        self.area=circle.pi*self.val**2


a=circle()
a.getvalue()
a.cal()
print("Area is {}".format(a.area))