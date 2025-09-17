#PolyEx8.py
class Circle:
    def __init__(self): # Original Constructor
        print("Circle--Drawing Circle-Default Constructor")
class Rect(Circle):
    def __init__(self):  # Overridden Constructor
        print("Rect--Drawing Rect-Default Constructor")
        super().__init__()
class Square(Rect):
    def __init__(self):  # Overridden Constructor
        print("Square--Drawing Square-Default Constructor")
        super().__init__()

#Main Program
s=Square() # Object Creation
