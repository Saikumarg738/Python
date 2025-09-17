#Write a Python Program for Cal area of different Figures by Using OOPs
#PolyEx13.py
class Circle:
    def area(self,r): # Original Method
        self.ac=3.14*r**2
        print("Area of Circle={}".format(self.ac))
class Square(Circle):
    def area(self,s): # Overridden Method
        self.sa=s**2
        print("Area of Square={}".format(self.sa))
        print("------------------------------------")
        super().area(float(input("Enter Radius:")))

class Rect(Square):
    def area(self,L,B): # Overridden Method
        self.ra=L*B
        print("Area of Rect={}".format(self.ra))
        print("------------------------------------")
        super().area(float(input("Enter Side Val:")))

#Main Program
r=Rect()
r.area(float(input("Enter Length:")),float(input("Enter Breadth:")))
print(dir(r))
