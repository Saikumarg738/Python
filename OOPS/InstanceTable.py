class Table:
    def getvalue(self):
        i=0
        while(i<3):
            try:
                self.val=int(input("Enter number : "))
            except ValueError:
                print("Please enter only numbers")
            else:
                print("value given is {}".format(self.val))
                break

    def calculate(self):
        for i in range(1,11):
            print("{} * {} = {}".format(self.val,i,self.val*i))

t1=Table()
t1.getvalue()
t1.calculate()