class circle:
    def draw(self):
        print("Circle drawn")
class rect(circle):
    def draw(self):
        print("Rect drawn")
class square(rect):
    def draw(self):
        print("Square drawn")
        rect.draw(self)
        circle.draw(self)

s=square()
s.draw()
