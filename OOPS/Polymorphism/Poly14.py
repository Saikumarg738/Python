#Write a Python Program for Cal area of different Figures by Using OOPs
#PolyEx18.py
class Circle:
    def __init__(self,r): # Original Constructor
        self.ac=3.14*r**2
        print("Area of Circle={}".format(self.ac))
class Square(Circle):
    def __init__(self,s): # Overridden Constructor
        self.sa=s**2
        print("Area of Square={}".format(self.sa))
        print("------------------------------------")
        super().__init__(float(input("Enter Radius:")))

class Rect(Square):
    def __init__(self,L,B): # Overridden Constructor
        self.ra=L*B
        print("Area of Rect={}".format(self.ra))
        print("------------------------------------")
        super().__init__(float(input("Enter Side Val:")))

#Main Program
r=Rect(float(input("Enter Length:")),float(input("Enter Breadth:"))) # Object Creation with Parameterized Const