#InhProg8.py
class GrandParent:
    def getGrandParentProperty(self):
        self.gp=float(input("\tEnter Grand Parent Property:"))
class Parent(GrandParent):
    def getParentProperty(self):
        self.pp=float(input("\tEnter Parent Property:"))
class Child(Parent):
    def getChildProperty(self):
        self.cp=float(input("\tEnter Child Property:"))
    def calTotalProperty(self):
        self.tp=self.gp+self.pp+self.cp
        print("\tGrand Parent Property:{}".format(self.gp))
        print("\tParent Property:{}".format(self.pp))
        print("\tChild Property:{}".format(self.cp))
        print("\tTotal Property:{}".format(self.tp))

#Main Program
co=Child()
co.getGrandParentProperty()
co.getParentProperty()
co.getChildProperty()
co.calTotalProperty()