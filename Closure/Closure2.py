# This is not a closure


def grandfather(gname):
    def gchild(cname):
        print("Hi i am {}, grandchild of {}".format(cname,gname))
    gchild("Satish")
    gchild("Raghav")
    gchild("Dhruv")

child=grandfather("narayana")



