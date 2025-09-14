class a:
    def disp1(self):
        print("Hello Sai")
class b(a):
    def disp2(self):
        print("Good Morning")
class c(b):
    def disp3(self):
        print("How are you?")
class d(b):
    def disp3(self):
        print("Are you good?")

obj1=c()
obj1.disp1()
obj1.disp2()
obj1.disp3()

obj2=d()
obj2.disp1()
obj2.disp2()
obj2.disp3()