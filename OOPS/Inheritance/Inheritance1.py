class a:
    def meth(self):
        print("Hello Sai!")
class b(a):
    def meth2(self):
        print("Good Morning")

obj=b()
obj.meth()
obj.meth2()