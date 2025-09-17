class main:
    def advise(self):
        print("Hello Sai,",end="")
class sub1:
    def advise(self):
        main.advise(self)
        print("How are you?")
class sub2:
    def advise(self):
        main.advise(self)
        print("How was your day?")

s1=sub1()
s1.advise()
s2=sub2()
s2.advise()