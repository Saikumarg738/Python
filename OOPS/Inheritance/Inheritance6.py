class parent:
    def parentproperty(self):
        self.pp=float(input("Enter parent property"))

class child(parent):
    def childproperty(self):
        self.cp=float(input("Enter child property"))
    def totalproperty(self):
        print("Parent property : ",self.pp)
        print("Child property : ",self.cp)
        print("Total property : ",self.pp+self.cp)

obj=child()
obj.parentproperty()
obj.childproperty()
obj.totalproperty()