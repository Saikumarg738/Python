#Conver to upper and lower
def convupper(bheem):
    def rrr():
        line,lline=bheem()
        uline=line.upper()
        return line,lline,uline
    return rrr


def convlower(ram):
    def rrr():
        line=ram()
        lline=line.lower()
        return line,lline
    return rrr


@convupper
@convlower
def takein():
    return input("Enter the line : ")

line,lline,uline=takein()

print("Original line is {}".format(line))
print("Lower case is {}".format(lline))
print("Upper case is {}".format(uline))