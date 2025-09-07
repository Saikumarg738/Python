#Calculating area but calling with nameless object

class circle:
    @classmethod
    def pi(cls):
        cls.piv=3.14
    def cal(self):
        self.getrad()
        circle.pi()
        val=circle.piv*self.r**2
        print(val)
    def getrad(self):
        self.r=float(input())

#circle().cal() # Nameless object

circle().cal()