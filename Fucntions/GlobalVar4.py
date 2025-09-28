a=10
b=20
c=30

def add():
    ans=0
    g=globals()
    g['a']+=5
    g['b']+=5
    g['c']+=5
    d=40
    ans=a+b+c+d
    print(ans)

add()