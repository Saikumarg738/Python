from ATM2Exception import *

bal=2000

def deposit():
    amount=float(input("Enter the deposit amount : "))
    if(amount<=0):
        raise DepositError
    else:
        global bal
        bal=bal+amount
    print("{} deposited".format(amount))

def withdraw():
    global bal
    amount=float(input("Enter amount to withdraw : "))
    if(amount<=0 or amount>bal):
        raise InsufficientFunds
    else:
        bal=bal-amount
    print("{} withdrawn".format(amount))
def balance():
    global bal
    print("Available balance is {}".format(bal))