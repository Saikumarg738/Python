class fact:
    def __init__(self,a):
        self.n=a
    def cal(self):
        fact=1
        for i in range(1,self.n+1):
            fact*=i
        print("Factorial of {} is {}".format(self.n,fact))

s=fact(5)
s.cal()