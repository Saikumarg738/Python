# Multilevel

class a:
    def disp1(self):
        print("Hello Sai!")
class b(a):
    def disp2(self):
        print("Good Morning")
class c(b):
    def disp3(self):
        print("How are you?")

obj=c()
obj.disp1()
obj.disp2()
obj.disp3()