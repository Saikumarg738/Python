#Conver to upper and lower
def convupper(bheem):
    def rrr():
        b=""
        line,a=bheem()
        for i in line:
            if(ord(i) in range(97,123)):
                b=b+chr(ord(i)-32)
            else:
                b=b+chr(ord(i))
        return line,a,b
    return rrr


def convlower(ram):
    def rrr():
        a=""
        line=ram()
        for i in line:
            if(ord(i) in range(65,97)):
                a=a+chr(ord(i)+32)
            else:
                a=a+chr(ord(i))
        return line,a
    return rrr


@convupper
@convlower
def takein():
    return input("Enter the line : ")

line,a,b=takein()

print("Original line is {}".format(line))
print("Lower case is {}".format(a))
print("Upper case is {}".format(b))