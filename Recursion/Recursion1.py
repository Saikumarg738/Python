import sys

def welcome(msg,n):
    if(n==0):
        sys.exit()
    print("Hello Sai",n)
    welcome("Sai",n-1)

welcome("Sai",5)