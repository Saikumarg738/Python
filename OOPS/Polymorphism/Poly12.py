#PolyEx20.py
class FastFood:
    def rice(self):pass
class Rajesh(FastFood):
    def rice(self):
        print("Rajesh Taking Veg Munchira Rice")
class Pavan(FastFood):
    def rice(self):
        print("Pavan Taking Veg Jeera Rice")
class Shahu:
    def rice(self):
        print("Shahu Taking Curd Rice")

#Main Program
Rajesh().rice()
Pavan().rice()
Shahu().rice()