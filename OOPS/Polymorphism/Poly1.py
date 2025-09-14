class Circle:
    def draw(self):
        print("Circle is drawn")
class Rect(Circle):
    def draw(self):
        print("Rect is drawn")
        super().draw()

o=Rect()
o.draw()