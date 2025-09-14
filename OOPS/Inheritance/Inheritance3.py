# Hierarchical

class a:
    def disp1(self):
        print("Hello Sai")
class b(a):
    def disp2(self):
        print("Good Morning")
class c(a):
    def disp2(self):
        print("Good Night")

obj=b()
obj.disp1()
obj.disp2()
obj=c()
print(type(obj))
obj.disp1()
obj.disp2()