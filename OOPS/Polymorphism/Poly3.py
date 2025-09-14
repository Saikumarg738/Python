class circle:
    def draw(self):
        print("Circle is drawn")
class rect(circle):
    def draw(self):
        print("Rect is drawn")
        super().draw()
class square(rect):
    def draw(self):
        print("Circle is drawn")
        super().draw()
a=square()
a.draw()