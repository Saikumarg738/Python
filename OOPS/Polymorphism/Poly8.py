#PolyEx10.py
class Circle:
    def __init__(self): # Original Constructor
        print("Circle--Drawing Circle-Default Constructor")
class Rect:
    def __init__(self):  # Original Constructor
        print("Rect--Drawing Rect-Default Constructor")

class Square(Rect,Circle):
    def __init__(self):  # Overridden Constructor
        print("Square--Drawing Square-Default Constructor")
        super().__init__()
        Circle.__init__(self)

#Main Program
s=Square() # Object Creation