class sample:
    def __init__(self,a=1,b=2):
        self.x=a
        self.y=b
        print(f"Value of x is : ",self.x)
        print(f"Value of y is : ",self.y)
        print("-------------------------")

s=sample()
s=sample(10,20)
s=sample(10)
s=sample(b=10)