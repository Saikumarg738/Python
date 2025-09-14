class animal:
    def sound(self):
        print("Some sound")
class dog(animal):
    def sound(self):
        print("Bow")
class cat(animal):
    def sound(self):
        print("meon")

animals=[animal(),dog(),cat()]

for animal in animals:
    animal.sound()