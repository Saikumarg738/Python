class Lion:
    def sound(self):
        print("Roarrrrrr")

class Elephant:
    def sound(self):
        print("ouuuhnnhhhh")
class Sai:
    def sound(self):
        print("Clean & Loud")

animal=[Lion(),Elephant(),Sai()]

for a in animal:
    a.sound()