
def grandfather(gname):
    def gchild(cname):
        print("Hi i am {}, grandchild of {}".format(cname,gname))
    return gchild

child=grandfather("narayana")

child("Satish")
child("Raghav")
child("Dhruv")

