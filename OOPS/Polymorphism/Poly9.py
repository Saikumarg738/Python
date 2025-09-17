#Write a Python Program for Cal area of different Figures by Using OOPs
#PolyEx11.py
class Circle:
    def area(self): # Original Method
        self.r=float(input("Enter Radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle={}".format(self.ac))
class Square(Circle):
    def area(self): # Overridden Method
        self.s=float(input("Enter Side of Square:"))
        self.sa=self.s**2
        print("Area of Square={}".format(self.sa))
        print("----------------------------------")
        super().area()
class Rect(Square):
    def area(self): # Overridden Method
        self.L=float(input("Enter Length:"))
        self.B = float(input("Enter Breadth:"))
        self.ra=self.L*self.B
        print("Area of Rect={}".format(self.ra))
        print("----------------------------------")
        super().area()

#Main Program
r=Rect()
r.area()
